# Unreal Engine & AirSim Drone Simulation with LLaMA Speech Recognition Integration 
## Overview

This project integrates __Unreal Engine__ and the __AirSim__ drone simulation platform with __LLaMA-based language models__, __speech recognition__, and __gaze tracking__ functionality. The goal is to allow users to control a drone through both voice commands and gaze tracking, processed by the LLaMA 3.1 8B Instruct model and the gaze tracking system.

## Features
__Gaze Tracking__: Allows drone control based on where the user is looking.
__Drone Simulation__: Controlled via Unreal Engine with AirSim.
__Speech Recognition__: Converts voice commands to text and uses LLM model to processess texy commands.

## Prerequisites
Before getting started, make sure you have the following installed:

Unreal Engine (Recommand v4.27)
Microsoft AirSim  
Python 3.8 or later<br>
PyAudio<br>
LLaMA 3.1 8B Instruct Model<br>
Whisper Model for Speech Recognition<br>
Python Libraries: wave, pyttsx3, pyaudio, faster-whisper<br>

## Setup Guide
### 1. Install Unreal Engine and AirSim
   a. Download and install Unreal Engine from [Unreal Engine Official Site](https://www.unrealengine.com/en-US/download).<br>
   b. Clone and set up AirSim for Unreal Engine by following the steps in https://github.com/Microsoft/AirSim.

```
git clone https://github.com/microsoft/AirSim.git
cd AirSim
./setup.sh
./build.sh
```

### 2. Set Up Python Environment
1. Install Python: Ensure that you have Python 3.8 or later installed. You can check your Python version by running:
```
python --version
```
2. Install Required Python Libraries: Run the following commands to install the necessary packages:
```
pip install torch transformers sentencepiece
pip install pyaudio wave pyttsx3 faster-whisper
```
3. Install LLaMA 3.1 8B Instruct Model
```
from transformers import LlamaTokenizer, LlamaForCausalLM

# Load LLaMA 8B Model and Tokenizer
model_name = "facebook/llama-3.1-8B-instruct"  
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
```
4. Speech Recognition Integration
To enable speech recognition, we’ll use the faster-whisper library. You’ll also need pyaudio for capturing audio and pyttsx3 for text-to-speech feedback.

5. Gaze Tracking Integration

6. Integrate Speech and Gaze Tracking Commands into AirSim
Once you have speech transcription using Whisper and gaze tracking using your chosen SDK, integrate them with AirSim to control the drone.

Speech Commands: Map commands like "move forward" or "go left" to drone controls.
Gaze Control: Use gaze data to adjust the drone’s direction or camera view in real time.

## Usage
Run Unreal Engine with AirSim: Open your Unreal Engine project with AirSim integrated and start the drone simulation.<br>
Activate Speech and Gaze Tracking: Run the Python scripts for speech recognition and gaze tracking.<br>
Issue Voice and Gaze Commands: Speak into your microphone or use your gaze to control the drone’s movements in the AirSim simulation.<br>

## Acknowledgements
Meta AI for LLaMA models.<br>
Microsoft AirSim for the drone simulation platform.<br>
Whisper for speech recognition.<br>
Hugging Face for the transformers library.<br>
