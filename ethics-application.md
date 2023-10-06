# Ethics Application 

## Project Title 

Building and Validating A Gaze-Aware AI System for Automatic Paragraph-Level Bookmarking

## Project Description 

The aim of this project is to investigate the use of machine learning & face images captured using in-built laptop/phone cameras to track reading progress within text in a web browser so as to enable bookmark of the last paragraph being read when browser tabs or windows are switched.

This project will involve building & evaluating machine learning models for gaze tracking & analysis based on 3 secondary datasets, GazeCapture, MPIIGaze, & ETHXGaze.The GazeCapture [1] dataset was captured from participants while they focused on marked points on their phone/tablet screen at home.This dataset includes face images, gaze target positions, & metadata, e.g. device screen orientation.It is accessible via a website (https://gazecapture.csail.mit.edu), a registration form, & adherence to a license that stipulates no sharing with any third party & research use only.

MPIIGaze [4] was also captured in similar settings as GazeCapture.However, the data was captured with the participant’s laptop, & the gaze focus tasks for this dataset appeared to the participant at random times during normal use of their laptop. The dataset includes cropped eye images, positions of eye landmarks, gaze target positions, associated head poses & directions, & camera parameters.It will be accessed via the website (https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/appearance-based-gaze-estimation-in-the-wild), & it comes with a license that requires non-commercial use only.

The ETHX-Gaze dataset [5] was captured in lab settings using multiple external cameras. The dataset includes face images, gaze target positions, & lighting conditions. The dataset will be accessed via the website (https://ait.ethz.ch/xgaze), a registration form, & agreement to a license that requires non-commercial use.

The machine learning model developed from these datasets will be used to build a software deployed on a local computer.The software will take face images via the device camera, triggered by events on the linked web browser (e.g. switching tabs), & send inference of the user’s gaze target location on the given web page to the browser for bookmarking.This web browser extension software will only be validated on myself & my supervisor; no tests with primary research participants will be carried out.

The datasets are well used in the research community, e.g. in [2, 3, 6, 7]. My use aligns with the purpose for which they were originally collected (gaze tracking). The datasets will be stored on an external hard drive, which will be software-encrypted & not shared with any third party, & on University of Sussex OneDrive. The data will also be stored & processed on my personal laptop, which is password protected & will not be shared with any third party, as well as on University of Sussex computers. Processing will be done using standard statistics & machine learning methods & software development kits.

[1] K. Krafka et al., Eye Tracking for Everyone. Proc. IEEE Conf. on computer vision & pattern recognition. 2016.

[2] S. Park et al., Few-Shot Adaptive Gaze Estimation. Proc. IEEE/CVF Int. Conf. on computer vision. 2019.

[3] N. Valliappan et al. Accelerating eye movement research via accurate & affordable smartphone eye tracking. Nat Commun 11, 4553 (2020).

[4] X. Zhang et al., “Appearance-based Gaze Estimation in the Wild,” in Proc. IEEE Conf. on Computer Vision & Pattern Recognition, 2015.

[5] X. Zhang et al., “ETH- XGaze: A Large Scale Dataset for Gaze Estimation under Extreme Head Pose & Gaze Variation,” CoRR, vol. abs/2007.15837, 2020

[6] Y. Wang et al., “Contrastive Regression for Domain Adaptation on Gaze Estimation,” in Proc. IEEE/CVF Conf. Computer Vision & Pattern Recognition, 2022.

[7] Y. Wang et al., “Contrastive Regression for Domain Adaptation on Gaze Estimation,” in Proc. IEEE/CVF Conf. Computer Vision & Pattern Recognition, 2022.