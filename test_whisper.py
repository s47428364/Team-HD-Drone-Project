import sounddevice as sd
import soundfile as sf
import numpy as np
from faster_whisper import WhisperModel

# Initial model
model = WhisperModel("base")

def record_and_transcribe(filename, duration=5, samplerate=16000):
    # set files
    file = sf.SoundFile(filename, mode='w', samplerate=samplerate, channels=1, subtype=None)

    def callback(indata, frames, time, status):
        if status:
            print("Status:", status)
        file.write(indata)

    try:
        with sd.InputStream(callback=callback, samplerate=samplerate, channels=1):
            print("Recording... Please speak into the microphone.")
            sd.sleep(duration * 1000)  # set 1 second
    finally:
        file.close()

    # voice recognition
    segments, info = model.transcribe(filename)
    for segment in segments:
        print(segment.text)

# 主循环
while True:
    record_and_transcribe('923.wav')

