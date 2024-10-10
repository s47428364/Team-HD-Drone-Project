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
2. Clone and set up AirSim for Unreal Engine by following the steps from [AirSim](https://github.com/Microsoft/AirSim).
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
3. Install LLaMA 3.1 8B Instruct Model
```
from transformers import LlamaTokenizer, LlamaForCausalLM

# Load LLaMA 8B Model and Tokenizer
model_name = "facebook/llama-3.1-8B-instruct"  
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
```

### 3. Integration of Control Methods
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
