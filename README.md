# AI based Unmanned Entrance Control System for COVID-19 Protection
### Project Outline

1. Facial Mask Detection
2. Measure body temperature with a thermal imaging camera
3. Record of COVID-19 epidemiological investigation App

* If one of the three is not satisfied, warning sound is generated and entrance is blocked.


<img width="461" src="https://user-images.githubusercontent.com/1857075/152288805-4696ca50-7c8c-4e24-977a-befa3fdd1dff.JPG">
<img width="461" src="https://user-images.githubusercontent.com/1857075/152288811-2e7e2a5e-2f93-42ab-b32a-ab179a8ffa68.JPG">

<hr>

### YouTube Video

[![Video Label](http://img.youtube.com/vi/INJaqVwoJR4/0.jpg)](https://youtu.be/INJaqVwoJR4)

[![Video Label](http://img.youtube.com/vi/kuV5g9euzrI/0.jpg)](https://youtu.be/kuV5g9euzrI)

<hr>

### Dataset
* Data Source : https://github.com/prajnasb/observations
* Without Mask : 667
* With Mask : 690

<img width="461" src="https://user-images.githubusercontent.com/1857075/152646158-df1772fb-d250-42fa-86fb-d1bc5442aa4d.jpg">

* Visualizing Data Samples
<img width="461" src="https://user-images.githubusercontent.com/1857075/152664417-0eeb838f-e51d-4ecc-903b-f28f3ae71eae.png">
<img width="461" src="https://user-images.githubusercontent.com/1857075/152664483-4857809d-52dc-4f1f-bf72-f6cdea8e70c6.png">

<hr>

### Performance Metrics of Facial Mask Classification Model

* Transfer Learning for facial mask classification : MobileNet v2.1
<img width="350" src="https://user-images.githubusercontent.com/1857075/152664724-0b8a82d2-3fbf-422a-85b3-6b9feac1902f.png">
<img width="410" src="https://user-images.githubusercontent.com/1857075/152670337-1770ddb7-fd00-4068-a1c2-96e17eca63cc.jpg">
<img width="410" src="https://user-images.githubusercontent.com/1857075/152670369-fa661aaf-e079-430e-bc66-d217119ae5c2.jpg">
<img width="460" src="https://user-images.githubusercontent.com/1857075/152645586-488426bb-867f-4634-8cec-3ae96c22c201.png">
<img width="400" src="https://user-images.githubusercontent.com/1857075/152645590-849ef781-a40f-4db2-90f9-48023aea67d4.png">

* OpenCV's caffe model(SSD/ResNet10) for recognizing frontal faces : https://github.com/sr6033/face-detection-with-OpenCV-and-DNN
<hr> 

### Things used in this project
* Jetson nano 4G / Intel WiFi & Bluetooth module : https://developer.nvidia.com/embedded/jetson-nano-developer-kit
* Teledyne FLIR Lepton 3.0 & 3.5 Micro Thermal Camera Modules : https://www.flirkorea.com/products/lepton/
<img width="400" src="https://user-images.githubusercontent.com/1857075/152665483-f199aa47-290e-4a92-bfb0-cea1f08c7188.jpg">

* Raspberry Pi, Camera Module , CSI-2 with 3280 x 2464 pixels Resolution
<img width="400" src="https://user-images.githubusercontent.com/1857075/152665492-f273b23e-065a-4d56-835b-26235006640d.jpg">

* Warning Light System : https://bit.ly/3L5ZM6h
* NodeMCU/ Ardunio Realy : https://www.nodemcu.com/index_en.html
* Google Firebase Realtime Database : https://firebase.google.com/
* Tensorflow 2.3, OpenCV Python 4.4

<hr>

### Mobile App for the COVID-19 Epidemiological Investigation

<img width="350" src="https://user-images.githubusercontent.com/1857075/152669936-edb601c0-1c80-49c1-9a50-0c33a711754c.jpg">
<img width="350" src="https://user-images.githubusercontent.com/1857075/152669930-197bb505-6e55-45b7-ba79-610ac9a9dec1.jpg">

<hr>

### The Photos

<img width="461" src="https://user-images.githubusercontent.com/1857075/152282023-fcfd4fdd-33b4-4897-8b25-3f5b5bac85a3.jpg">
<img width="461" src="https://user-images.githubusercontent.com/1857075/152669390-b04d0584-3a9e-47e3-8774-ba893cb0a475.jpeg">
<img width="461" src="https://user-images.githubusercontent.com/1857075/152282037-41352841-f5fd-45d3-8343-e71ff90d5dc2.jpg">
<img width="461" src="https://user-images.githubusercontent.com/1857075/152282032-8faa7fff-7324-41a6-9a1d-92b92e7be036.jpg">
<img width="461" src="https://user-images.githubusercontent.com/1857075/152282035-16208534-4b2d-4d18-8db8-80c8dbd8bbf3.jpg">


<hr>

### References

* https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/
* https://github.com/prajnasb/observations
* https://github.com/sr6033/face-detection-with-OpenCV-and-DNN
* https://youtube.com/playlist?list=PL7GibveZmIwFrmBbDMYPRRc2PyG96TCdi




