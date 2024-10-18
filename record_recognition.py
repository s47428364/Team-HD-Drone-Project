import pyaudio
import wave
import pyttsx3
from faster_whisper import WhisperModel


# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
# This is to set the voice to English
voices = engine.getProperty('voices')
for voice in voices:
    if "English" in voice.name:
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()


# Record the voice command
def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "command.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    speak("Recording 5 seconds.")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    speak("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return WAVE_OUTPUT_FILENAME


def transcribe_audio(audio_file):
    model = WhisperModel("base")
    segments, _ = model.transcribe(audio_file)
    for segment in segments:
        with open("transcription.txt", "w") as f: # Write the transcription to a text file
            f.write(f"{segment.text}" + "\n")
