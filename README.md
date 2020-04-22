# 19520-Fall-Detection-DVS
## 19520 Low Cost DVS Camera for Fall Detection System
## Project Abstract
The system detects if a person has fallen, communicates with them, and helps them receive the appropriate assistance without the need for a physical sensor or intrusive monitoring. This is performed by connecting a conventional camera sensor to an FPGA, which then finds the changes between frames. This data is then sent to a central server using Wi-Fi, where it is classified using a convolutional neural network as either a fall or not a fall  . If a fall has been detected, the system will use text-to-speech and voice recognition to communicate with the user, and call an appropriate form of help. 

## Voice Recognition - Kirsty Purden
Contains:
- Filtering.py - a python file containing functions to filter audio files
- RecordSpeech.py - a python file to record audio from a microphone
- TestFunctions.py - a python file with various functions to test the system (would not be part of the final product)
- TextToSpeech.py - a python file to create the necessary text to speech
- setup.py - a python file to take in name and phonenumber of user's named contact, and the user's addres, on first time setup
- voiceRecog.py - a python file using a HMM to determine what speech has been said in an audio clip
- q1,, q2, q3 .mp3 - files containing text to speech questions that the system will ask the fallen user
- r1, r2, r3, r4 .mp3 - files containing text to speech responses to user speaking

## Wireless DVS FPGA Subsystem - Lewis Brown, Daniel Nadejde and Graeme Fitzpatrick  
Contains:
- DVS IP Core
- Encoding Algorithm
- WiFi_transmission
- FAST_VivadoSDK.zip

Each of these Folders contains a major element of project, with FAST_VivadoSD.zip containing the final system design

## DVS IP Core - Lewis Brown
Contains:
- DVS.zip - contains 3 folders; DVS is a HLS project which can be loaded into Vivado HLS. DVS_IP is a Vivado IP repository which can be loaded into Vivado with the emulated DVS IP Core. Sourcefiles contains the C code manipulated in HLS
- Grey2RGB_ip_repo - an IP repository containing an IP which converts Greyscale DVS to RGB for display on a monitor

## Encoding Algorithm - Graeme Fitzpatrick
Contains:
- 3rdpic.png,floatingHead.png,Img_test.png,noMovement.png,noMovement2.png,sideview.png,sideview2.png,spooky.png,wave1.png, wave2.png, wave3.png, wave4.png - DVS images obtained from FPGA used for testing
- dvs2.png, dvs3.png,Encode1.png,Encode2.png,ThresholdBool1.png,ThresholdBool2.png - DVS images obtained from pre-processing script on video of people walking, used for testing
- DecodeDVSData.m - Script that takes encoded_BYTE{x}.txt file saved by TCP_Server.py from WiFi transmission, decodes and reconstructs the image.
- DVSEncodingHelpScripts.m - Script used in development of encoder, containing all small functionality items such as saving DVS images into a text file to be imported and used with the C algorithm. 
- encmain.c - C implemented encoder for DVS images.
- EncodeDecodeTest.m - Script for encoding and decoding 640x640 '.png.' DVS Test images.
- rledec.m = Run Length Encoding Decode function.
- rleenc.m Run Length Encoding Encode Function.
- readintoc.txt,encodeimage.txt - text file containing 1D DVS single channel image vector, importable for use with C algorithm.
- encoded_data_BYTE.txt,encoded_BYTE{x}.txt - Binary data containing 2 byte encdoded arrays sent from FPGA, for use with DecodeDVSData.m

## Wifi Transmission - Daniel Nadejde
Contains: 
-
-



## videoClassification - Andrew Burr
-
-
-


## Other
- 19520 Interim Report Group 1 Mentor Draft.pdf - a draft of the interim report
- Bill of Materials.xlsx - spreadsheet containing details of budget expenditure
- DVS_model_diagram.drawio - editable diagram of FPGA subsystem
- DVS_model_diagram.png - image version of above
- GitHubQRCode.png - QR code to lead here for reports
- ProjectGanttInitial.xlsx - Gantt chart of project progress
- SystemLeveldesign.drawio - editable diagram of whole system
- Systemleveldesign.png - image version of above
- dvsImages.zip - collection of shared DVS frames for use in reports/poster/video/presentation
- presentationSystemLevelDiagram.drawio - editable diagram of system design at interim project stage
- presentationSystemLevelDiagram.png - image version of above
