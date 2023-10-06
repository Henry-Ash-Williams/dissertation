# Ethics Application 

## Project Title 

Building and Validating A Gaze-Aware AI System for Automatic Paragraph-Level Bookmarking

## Project Description 


~~The aim of this project is to investigate the possibility of using machine learning and face images captured using cameras (in-built laptop/phone cameras) to track a user’s reading progress within a piece of text in a web browser so as to help the user bookmark the last paragraph that they were looking when they switch browser tabs or program windows.~~

~~This project will involve building machine models for gaze tracking and analysis. I will make use of three secondary datasets, GazeCapture, MPIIGaze, and ETHXGaze, to build and evaluate these models. GazeCapture [1] is a crowdsourced dataset where face images were captured from participants while they focused on marked points on their phone screen in their home environments. This dataset includes a set of frames of each participants, taken while they were focussing on the gaze points, the location of the gaze points on the screen, as well as additional metadata such as information from their gyroscope, which tracks the rotational information of their device, and the kind of device they are using to complete the task (smartphone/tablet). The GazeCapture dataset is well used in the research community, e.g. [2] [3]. It is accessible via a website for the dataset (https://gazecapture.csail.mit.edu). I will need to complete a user registration form and adhere to the dataset license in order to download the data. The license (https://github.com/CSAILVision/GazeCapture/blob/master/LICENSE.md) stipulates that the data can be used for research purposes only and must not be shared with any third party.~~

~~MPIIGaze [4] was also captured in similar settings as the GazeCapture dataset. However, the data was captured using the participant’s laptop. Further, the gaze focus tasks for this dataset appeared to the participant at random times during their normal use of their laptops. Use of both datasets can enable validation of the machine learning model for both mobile devices and laptops or desktop computers. The dataset includes images of the users while using focussing on the gaze points, and the location of these points. The MPIIGaze dataset is also well used in the research community, e.g. [6] [8]. It will be accessed via the website (https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine- learning/research/gaze-based-human-computer-interaction/appearance-based- gaze-estimation-in-the-wild). This dataset is licensed under the Creative Commons Attribution NonCommercial ShareAlike 4.0 International License [7] that only requires me not to use it for commercial purposes.~~

~~The ETHX-Gaze dataset [5] was captured in lab settings using multiple external cameras. The dataset includes images taken from 18 different cameras, each with a unique perspective of the participant, the location of the gaze point they were asked to focus on, and the lighting information for the relevant capture. The ETHX-Gaze dataset is also well used in the research community, e.g. [6] [8]. The dataset will be accessed via the website (https://ait.ethz.ch/xgaze). I will need to complete a user form and agree to a license agreement. This dataset is also licensed under the Creative Commons Attribution NonCommercial ShareAlike license [7], which only demands use that is non-commercial.~~

~~The machine learning model built from this dataset will run locally on a secure application which a web browser plugin can interact with using an API (Applications Programming Interface). Because the machine model will be locally hosted on the same device the plugin operates on, external users will not be able to access the model. When the user takes the page on the web browser out of focus, for example by switching tabs, or switching to a different window on their device, a photograph will be taken from the users webcam. Then, the image will be encrypted and transferred to the local server running the model, and decrypted to ensure no other applications running on the users device can view the image. The model will use this image to predict where on the screen the user was last looking at before the text went out of focus. This location will then also be securely sent back to the web browser extension and used to determine which paragraph the user was last looking at. When the user installs this web browser extension, they will be taken to a page where they will be informed that this extension will take pictures from their webcam, and used for the functionality of the application. They will then be asked  to give their consent and asked by their web browser to allow the ad-on to use the camera, and if they decline, they will be prompted to uninstall the application as it will not function without both their informed consent, and the necessary permissions from the web browser. The software will be evaluated on myself and my supervisor, Temitayo Olugbade (https://profiles.sussex.ac.uk/p272464-temitayo-olugbade), no tests with primary research participants will be carried out.~~

~~The three secondary datasets will be stored on an external hard drive which will be software-encrypted and not shared with any third party. In addition, the data will be stored on University of Sussex OneDrive. The data will also be stored and processed on my personal laptop, which is password protected using a password of sufficient strength and will not be shared with any other third parties, as well as University of Sussex computers. Processing will be done using standard statistics and machine learning methods.~~

~~[1] K. Krafka et al., Eye Tracking for Everyone. 2016.~~

~~[2] S. Park, S. D. Mello, P. Molchanov, U. Iqbal, O. Hilliges, and J. Kautz, Few-Shot Adaptive Gaze Estimation. 2019.~~

~~[3] Valliappan, N., Dai, N., Steinberg, E. et al. Accelerating eye movement research via accurate and affordable smartphone eye tracking. Nat Commun 11, 4553 (2020). https://doi.org/10.1038/s41467-020-18360-5~~

~~[4] X. Zhang, Y. Sugano, M. Fritz, and A. Bulling, “Appearance-based Gaze Estimation in the Wild,” in Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Jun. 2015, pp. 4511–4520.~~

~~[5] X. Zhang, S. Park, T. Beeler, D. Bradley, S. Tang, and O. Hilliges, “ETH- XGaze: A Large Scale Dataset for Gaze Estimation under Extreme Head Pose and Gaze Variation,” CoRR, vol. abs/2007.15837, 2020, [Online]. Available: https://arxiv.org/abs/2007.15837~~

~~[6] Y. Wang et al., “Contrastive Regression for Domain Adaptation on Gaze Estimation,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Jun. 2022, pp. 19376–19385.~~

~~[7] https://creativecommons.org/licenses/by-nc-sa/4.0/~~

~~[8] Y. Liu, R. Liu, H. Wang, and F. Lu, “Generalizing Gaze Estimation With Outlier-Guided Collaborative Adaptation,” in Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), Oct. 2021, pp. 3835–3844.~~

The aim of this project is to investigate the use of machine learning and face images captured using (in-built laptop/phone) cameras to track reading progress within text in a web browser so as to enable bookmark of the last paragraph being read when browser tabs or windows are switched.

This project will involve building and evaluating machine learning models for gaze tracking and analysis based on 3 secondary datasets, GazeCapture, MPIIGaze, and ETHXGaze. The GazeCapture [1] dataset was captured from participants while they focused on marked points on their phone/tablet screen at home. This dataset includes face images, gaze target positions, and metadata, e.g. device screen orientation. It is accessible via a website (https://gazecapture.csail.mit.edu), a registration form, and adherence to a license that stipulates no sharing with any third party and research use only.

MPIIGaze [4] was also captured in similar settings as the GazeCapture. However, the data was captured with the participant’s laptop, and the gaze focus tasks for this dataset appeared to the participant at random times during their normal use of their laptop. The dataset includes cropped eye images, positions of eye landmarks, gaze target positions, associated head poses and directions, and camera parameters. It will be accessed via the website (https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/appearance-based- gaze-estimation-in-the-wild), and it comes with a license that requires non-commercial use only.

The ETHX-Gaze dataset [5] was captured in lab settings using multiple external cameras. The dataset includes face images, gaze target positions, and lighting conditions. The dataset will be accessed via the website (https://ait.ethz.ch/xgaze), a registration form, and agreement to a license that requires non-commercial use.

The machine learning model developed from these datasets will be used to build a software deployed on a local computer. The software will take (face) images via the device camera, triggered by events on the linked web browser (e.g. switching tabs), and send inference of the user’s gaze target location on the given web page to the browser for bookmarking. This (web browser extension) software will only be validated on myself and my supervisor; no tests with primary research participants will be carried out.

The datasets are well used in the research community, e.g. in [2] [3] [6] [8]. My use aligns with the purpose for which they were originally collected (gaze tracking). The datasets will be stored on an external hard drive, which will be software-encrypted and not shared with any third party, and on University of Sussex OneDrive. The data will also be stored and processed on my personal laptop, which is password protected and will not be shared with any third party, as well as on University of Sussex computers. Processing will be done using standard statistics and machine learning methods and software development kits.

[1] K. Krafka et al., Eye Tracking for Everyone. Proc. IEEE Conf. on computer vision and pattern recognition. 2016.

[2] S. Park et al., Few-Shot Adaptive Gaze Estimation. Proc. IEEE/CVF Int. Conf. on computer vision. 2019.

[3] N. Valliappan et al. Accelerating eye movement research via accurate and affordable smartphone eye tracking. Nat Commun 11, 4553 (2020).

[4] X. Zhang et al., “Appearance-based Gaze Estimation in the Wild,” in Proc. IEEE Conf. on Computer Vision and Pattern Recognition, 2015.

[5] X. Zhang et al., “ETH- XGaze: A Large Scale Dataset for Gaze Estimation under Extreme Head Pose and Gaze Variation,” CoRR, vol. abs/2007.15837, 2020

[6] Y. Wang et al., “Contrastive Regression for Domain Adaptation on Gaze Estimation,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, 2022.

[7] Y. Liu et al., “Generalizing Gaze Estimation With Outlier-Guided Collaborative Adaptation,” in Proc. IEEE/CVF Int. Conf. on Computer Vision, 2021

[8] Y. Wang et al., “Contrastive Regression for Domain Adaptation on Gaze Estimation,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, 2022.

[9] Y. Liu et al., “Generalizing Gaze Estimation With Outlier-Guided Collaborative Adaptation,” in Proc. IEEE/CVF Int. Conf. on Computer Vision, 2021
