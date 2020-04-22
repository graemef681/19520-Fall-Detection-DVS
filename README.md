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

## Wifi Transmission - [author(s)]
Contains: 
-
-

## Zybo DVS - Lewis Brown, Daniel Nadejde, Graeme Fitzpatrick 
Contains:
- DVS-Comparison-Images - a folder containing Example DVS images
- DVS.zip - contains 3 folders; DVS is a HLS project which can be loaded into Vivado HLS. DVS_IP is a Vivado IP repository which can be loaded into Vivado with the emulated DVS IP Core. Sourcefiles contains the C code manipulated in HLS
- Grey2RGB_ip_repo - an IP repository containing an IP which converts Greyscale DVS to RGB for display on a monitor
- encmain.c - a C file which encodes DVS frames using Run Length Encoding

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



(Graeme can we remove the below link?)
CSI to 24Pin FPC Connector Pinout
http://www.myirtech.com/list.asp?id=611
