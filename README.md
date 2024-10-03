# Unreal Engine & AirSim Drone Simulation with LLaMA Speech Recognition Integration #
## Overview ##
This project integrates __Unreal Engine__ and the __AirSim__ drone simulation platform with __LLaMA-based language models__ and __speech recognition__ functionality. 
The goal is to allow users to control a drone through voice commands, processed by the LLaMA 3.1 8B Instruct model.

## Features ##
__Drone Simulation__: Controlled via Unreal Engine with AirSim.
__Speech Recognition__: Converts voice commands to text and uses LLM model to processess texy commands.

## Prerequisites ##
Before getting started, make sure you have the following installed:

Unreal Engine (Recommand v4.27)
Microsoft AirSim  
Python 3.8 or later<br>
PyAudio<br>
LLaMA 3.1 8B Instruct Model<br>
Whisper Model for Speech Recognition<br>
Python Libraries: wave, pyttsx3, pyaudio, faster-whisper<br>

## Setup Guide##
1. Install Unreal Engine and AirSim
   a. Download and install Unreal Engine from Unreal Engine Official Site.
   b. Clone and set up AirSim for Unreal Engine by following the steps in their GitHub Repository.

```
git clone https://github.com/microsoft/AirSim.git
cd AirSim
./setup.sh
./build.sh
```
