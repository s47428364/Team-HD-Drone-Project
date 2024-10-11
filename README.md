# Unreal Engine AirSim Drone Simulation with Gaze Tracking and LLaMA Speech Recognition 
## Overview

This project integrates __Unreal Engine__ using the __AirSim__ drone extension platform with __gaze tracking__, __LLaMA-based language models__, and __speech recognition__ functionality. The goal is to allow users to control a drone through both gaze tracking and voice commands, processed by OpenAI Api module.

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
pip install openai
```
Set up an API key by visiting https://platform.openai.com/account/api-keys. Copy the API key and paste it in the OPENAI_API_KEY field of config.json.
```
openai.api_key = config["OPENAI_API_KEY"]
```

### 4.Run Drone Simulator
1. Start the Simulator:<br>
Navigate to the AirSimInspection directory and double-click run.bat to launch the simulator.<br>
2. Initialize Chatbot Control:<br>
Run chatgpt_airsim.py to enable the chatbot interface.<br>
You’ll hear “Initializing AirSim...” followed by “Welcome to the AirSim chatbot! I am ready to help you with your AirSim questions and commands.” This confirms that the simulator and chatbot are running successfully.<br>
3. Give Voice Commands:<br>
After the initialization, you can issue commands to the simulator, such as:<br>
"Take off" to lift the drone into the air.<br>
"Move forward 10 units and go right 2 units" to navigate in specified directions.<br>
You’ll receive feedback prompts, such as "Recording 5 seconds," to confirm the simulator is executing your command.<br>
4. End the Session:<br>
To stop the code and end the session, you can say, "Thank you, you can quit" or simply "quit."<br>
The chatbot will respond, “Thank you for using the AirSim chatbot! Goodbye!” to indicate a successful shutdown.<br>


### 5. Integration of Control Methods
Speech Recognition Integration<br>
To enable speech recognition, we use the faster-whisper library. You’ll also need pyaudio for capturing audio and pyttsx3 for text-to-speech feedback.

Gaze Tracking Integration<br>
To enable gaze tracking, we use the cv2 library. You'll also need numpy and dlib for assistance in the processing of camera data.

Gaze Control: Use gaze data to adjust the drone’s position and direction.
Speech Commands: Map commands like "move forward" or "go left" to drone controls.


## Acknowledgements
* Epic Games for Unreal Engine
* Microsoft AirSim for the drone simulator.
* Whisper for speech recognition.
* Meta AI for LLaMA models.
* Hugging Face for the transformers library.
