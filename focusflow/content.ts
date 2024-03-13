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

function captureFrame() {
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    return ctx.getImageData(0, 0, canvas.width, canvas.height);
}

function getVisibilityState() {
    return document.visibilityState; 
}
// Function to handle visibility change
function handleVisibilityChange() {
    // file deepcode ignore FunctionDeclarationInBlock: <please specify a reason of ignoring this>
    const visibilityState = getVisibilityState();

    if (visibilityState === "hidden") {
        const frame = captureFrame();
        console.log(frame);
        fetch('localhost:8000/get-gaze-location', {
            method: "post",

        }).then(res => {
            let gazeLocation = res['location'];
            let paragraphs = document.querySelectorAll('p'); 

            updateVisibleElements(paragraphs, paragraph => {
                const bbox = paragraph.getBoundingClientRect(); 

                if (
                    gazeLocation.x >= bbox.left && 
                    gazeLocation.x <= bbox.right && 
                    gazeLocation.y >= bbox.top && 
                    gazeLocation.y <= bbox.bottom 
                ) {
                    paragraph.style.border = '2px solid red';
                }
            })}
        );

    } else if (visibilityState === "visible") {
        
    }
    
}

// Set up the event listener for visibility change
document.addEventListener('visibilitychange', handleVisibilityChange);

// Initial check for visibility state
handleVisibilityChange();
