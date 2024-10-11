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

parser = argparse.ArgumentParser()
parser.add_argument("--prompt", type=str, default="airsim_basic.txt")
parser.add_argument("--sysprompt", type=str, default="airsim_basic.txt")
args = parser.parse_args()

config_path = "config.json"
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Configuration file '{config_path}' not found.")

with open(config_path, "r") as f:
    config = json.load(f)

if "OPENAI_API_KEY" not in config:
    raise KeyError("OPENAI_API_KEY not found in the configuration file.")

rct.speak("Initializing ChatGPT...")
openai.api_key = config["OPENAI_API_KEY"]

with open(args.sysprompt, "r") as f:
    sysprompt = f.read()

chat_history = [
    {
        "role": "system",
        "content": sysprompt
    },
    {
        "role": "user",
        "content": "move 10 units up"
    },
    {
        "role": "assistant",
        "content": """```python
aw.fly_to([aw.get_drone_position()[0], aw.get_drone_position()[1], aw.get_drone_position()[2]+10])
```

This code uses the `fly_to()` function to move the drone to a new position that is 10 units up from the current position. It does this by getting the current position of the drone using `get_drone_position()` and then creating a new list with the same X and Y coordinates, but with the Z coordinate increased by 10. The drone will then fly to this new position using `fly_to()`."""
    }
]


def ask(prompt):
    chat_history.append(
        {
            "role": "user",
            "content": prompt,
        }
    )
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        temperature=0
    )
    chat_history.append(
        {
            "role": "assistant",
            "content": completion.choices[0].message.content,
        }
    )
    return chat_history[-1]["content"]


rct.speak(f"Done.")

code_block_regex = re.compile(r"```(.*?)```", re.DOTALL)


def extract_python_code(content):
    code_blocks = code_block_regex.findall(content)
    if code_blocks:
        full_code = "\n".join(code_blocks)

        if full_code.startswith("python"):
            full_code = full_code[7:]

        return full_code
    else:
        return None


rct.speak(f"Initializing AirSim...")
aw = AirSimWrapper()
rct.speak(f"Done.")

with open(args.prompt, "r") as f:
    prompt = f.read()

ask(prompt)
rct.speak("Welcome to the AirSim chatbot! I am ready to help you with your AirSim questions and commands.")



while True:
    audio_file = rct.record_audio()
    transcription = rct.transcribe_audio(audio_file)
    question = open("transcription.txt", "r").read().lower()
    print(question)

    if "quit" in question or "exit" in question:
        rct.speak("Thank you for using the AirSim chatbot! Goodbye!")
        break

    response = ask(question)
    print(response)
    if "question" in response:
        rct.speak(f"\n{response}\n")
    else:
        code = extract_python_code(response)
        if code is not None:
            rct.speak("Executing code:\n")
            exec(code)
            rct.speak("Done!\n")
