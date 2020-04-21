# 19520-Fall-Detection-DVS
## 19520 Low Cost DVS Camera for Fall Detection System
## Project Abstract
The system detects if a person has fallen, communicates with them, and helps them receive the appropriate assistance without the need for a physical sensor or intrusive monitoring. This is performed by connecting a conventional camera sensor to an FPGA, which then finds the changes between frames. This data is then sent to a central server using Wi-Fi, where it is classified using a convolutional neural network as either a fall or not a fall  . If a fall has been detected, the system will use text-to-speech and voice recognition to communicate with the user, and call an appropriate form of help. 

# Project Files
## PYNQ-DVS - [author(s)]
Contains: 
-

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

## Zybo DVS - [author(s)]
-
-
-

## videoClassification - Andrew Burr
-
-
-

## Other



(Graeme can we remove the below link?)
CSI to 24Pin FPC Connector Pinout
http://www.myirtech.com/list.asp?id=611
