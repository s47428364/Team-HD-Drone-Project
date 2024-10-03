# Unreal Engine & AirSim Drone Simulation with LLaMA Speech Recognition Integration 
## Overview
This project integrates __Unreal Engine__ and the __AirSim__ drone simulation platform with __LLaMA-based language models__ and __speech recognition__ functionality. 
The goal is to allow users to control a drone through voice commands, processed by the LLaMA 3.1 8B Instruct model.

## Features
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
   a. Download and install Unreal Engine from [Unreal Engine Official Site](https://www.unrealengine.com/en-US/download).
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

5. Integrate Speech Commands into AirSim
Once you have the transcription of speech using Whisper and processed commands using the LLaMA model, you can map these to drone controls in AirSim.

For instance, map text commands like "move forward" or "go left" to AirSim drone control commands.

## Usage
Run Unreal Engine with AirSim: Open your Unreal Engine project with AirSim integrated and start the drone simulation.
Activate Speech Recognition: Run the Python script for speech recognition.
Issue Voice Commands: Speak into your microphone, and the system will process the voice command using Whisper and LLaMA to control the drone in the AirSim simulation.

## Acknowledgements
Meta AI for LLaMA models.
Microsoft AirSim for the drone simulation platform.
Whisper for speech recognition.
Hugging Face for the transformers library.
