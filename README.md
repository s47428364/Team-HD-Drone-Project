# Unreal Engine AirSim Drone Simulation with Gaze Tracking and LLaMA Speech Recognition 
## Overview

This project integrates __Unreal Engine__ using the __AirSim__ drone extension platform with __gaze tracking__, __LLaMA-based language models__, and __speech recognition__ functionality. The goal is to allow users to control a drone through both gaze tracking and voice commands, processed by the LLaMA 3.1 8B Instruct model.

## Features
__Drone Simulation__: Implemented via Unreal Engine with AirSim.<br>
__Gaze Tracking__: Allows drone control based on where the user is looking.<br>
__Speech Recognition__: Converts voice input to text and uses LLM model to processess into commands.<br>

## Setup Guide
### 1. Install Unreal Engine and AirSim
1. Download and install Unreal Engine (Recommended v4.27) from [Unreal Engine](https://www.unrealengine.com/en-US/download).
2. Clone and set up AirSim for Unreal Engine by https://github.com/microsoft/PromptCraft-Robotics/releases.
```
git clone https://github.com/microsoft/AirSim.git
cd AirSim
./setup.sh
./build.sh
```

### 2. Set Up Python Environment
1. Ensure that you have Python 3.8 or later installed. You can check your Python version by running:
```
python --version
```
2. Install Required Python Libraries: Run the following commands to install the necessary packages using pip:
```
pip install torch transformers sentencepiece
pip install pyaudio wave pyttsx3 faster-whisper
pip install opencv-python
pip install numpy
pip install dlib
```
### 3. Install OpenAi module
```
import openai
import re
import argparse
from airsim_wrapper import *
import math
import numpy as np
import os
import json
import time
import record_command_and_transcribe as rct
```
Set up an API key by visiting https://platform.openai.com/account/api-keys. Copy the API key and paste it in the OPENAI_API_KEY field of config.json.
```
openai.api_key = config["OPENAI_API_KEY"]
```

### 4.Run Drone Simulator
Before start to complie code, your file structure should be as similar with below<br>
<img width="203" alt="image" src="https://github.com/user-attachments/assets/dd27bb76-711b-4cfb-82c7-62d0dad42592">
1. Click on run.bat on the AirSimInspection directory to run simulator.<br>
2. Run chatgpt_airsim.py to start control the simulator.<br>
2. When you heard "Initializing AirSim..." and "Welcome to the AirSim chatbot! I am ready to help you with your AirSim questions and commands.", it means the simulator succesfully run.<br>
3. You can say commands for example "Take off", "Move forward 10 units and go right 2 units" after "Recording 5 seconds."<br>
4. If you would like to stop code running, you can say "Thank you, you can quit" or just "quit" to quit the project. The chatbot would response "Thank you for using the AirSim chatbot! Goodbye!" to ensure responsiveness.


### 5. Integration of Control Methods
Speech Recognition Integration<br>
To enable speech recognition, we use the faster-whisper library. You’ll also need pyaudio for capturing audio and pyttsx3 for text-to-speech feedback.

Gaze Tracking Integration<br>
To enable gaze tracking, we use the cv2 library. You'll also need numpy and dlib for assistance in the processing of camera data.

Gaze Control: Use gaze data to adjust the drone’s position and direction.
Speech Commands: Map commands like "move forward" or "go left" to drone controls.

## Usage
Run Unreal Engine with AirSim: Open your Unreal Engine project with AirSim integrated and start the drone simulation.<br>
Activate Speech and Gaze Tracking: Run the Python scripts for speech recognition and gaze tracking.<br>
Issue Voice and Gaze Commands: Speak into your microphone or use your gaze to control the drone’s movements in the AirSim simulation.<br>

## Acknowledgements
* Epic Games for Unreal Engine
* Microsoft AirSim for the drone simulator.
* Whisper for speech recognition.
* Meta AI for LLaMA models.
* Hugging Face for the transformers library.
