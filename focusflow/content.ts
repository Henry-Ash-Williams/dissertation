export {}

import updateVisibleElements from "~getVisibleElements";

console.log("FocusFlow Loaded 🎉 !!");

const video = document.createElement('video');
video.setAttribute('autoplay', 'true');
video.style.display = 'none'; // Hide the video element

// Create canvas element
const canvas = document.createElement('canvas');
canvas.width = 640;
canvas.height = 480;
canvas.style.display = 'none';

document.body.appendChild(video);
document.body.appendChild(canvas);

navigator.mediaDevices.getUserMedia({video: true})
    .then(stream => {
        video.srcObject = stream; 
    })
    .catch(err => {
        console.error(`Error accessing webcam: ${err}`);
    });

fetch('http://localhost:8000/sanity-check', { 'method': 'get' })
.then(res => res.json())
.catch(err => {
    if (err.status === 404) {
        console.log('ERROR: Could not communicate with server, is it running?')
    }
})

function captureFrame(callback) {
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(callback);
}

function getVisibilityState() {
    return document.visibilityState; 
}

function isDesktop() {
    return window.innerWidth >= 1024; // Adjust the width threshold as needed
}
  
// Function to handle visibility change
function handleVisibilityChange() {
    const visibilityState = getVisibilityState();

    if (visibilityState === "hidden") {
        captureFrame(frame => {
            const requestData = new FormData(); 
            requestData.append('method', isDesktop() ? 'desktop' : 'mobile');
            requestData.append('file', frame);

            fetch(
                'http://127.0.0.1:8000/predict-gaze-location', 
                {
                    method: "post", 
                    body: requestData,
                }
            )
            .then(res => res.json())
            .then(res => {
                let gazeLocation = res['location'];
                let paragraphs = document.querySelectorAll('p, div'); 

                console.group()
                console.log(`Gaze Location Predicted at ${gazeLocation.x}, ${gazeLocation.y}`);
                updateVisibleElements(paragraphs, paragraph => {
                    const bbox = paragraph.getBoundingClientRect(); 
                    console.log(bbox);
                    if (
                        gazeLocation.x >= bbox.left && 
                        gazeLocation.x <= bbox.right && 
                        gazeLocation.y >= bbox.top && 
                        gazeLocation.y <= bbox.bottom 
                    ) {
                        console.log(`Gaze location found in webpage, element: ${paragraph}`);
                        paragraph.style.border = '2px solid red';
                    }
                });
                console.groupEnd();
            });
        });
    } else if (visibilityState === "visible") {
        
    }
    
}

// Set up the event listener for visibility change
document.addEventListener('visibilitychange', handleVisibilityChange);

// Initial check for visibility state
handleVisibilityChange();
