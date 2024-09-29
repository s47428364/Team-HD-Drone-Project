import pyaudio
import wave
import pyttsx3
from faster_whisper import WhisperModel




# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
# This is to set the voice to English, inspired by https://stackoverflow.com
# /questions/44858120/how-to-change-the-voice-in-pyttsx3
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
    if "English" in voice.name:
        engine.setProperty('voice', voice.id)
        break

# Define function for text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# The Main Entry
def main():
    # initialize status
    status = True
    speak("Welcone! The system is ready to listen to your voice commands.")

    
    while status:
        clear_command_file("command.wav")
        audio_file = record_audio()
        transcribe_audio(audio_file)
        
        speak("Do you want to continue?")
        user_response = record_audio_check_continue()  # Use voice for continue/stop decision
        transcription = transcribe_audio_for_command(user_response).lower()
        
        if "no" in transcription:
            status = False
        else:
            status = True
            speak("Continuing to the next command.")

    speak("Stopping the voice command interaction. Goodbye.")



# inspired by ChatGPT-o1-mini (OpenAI, www.chatgpt.com).
def clear_command_file(audio_file):
    with open(audio_file, "w") as f:
        pass


def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 8
    WAVE_OUTPUT_FILENAME = "command.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    speak("Recording now. Please speak your command in 8 seconds.")

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


def record_audio_check_continue():
    # Shorter recording duration for confirming continue/stop decision
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "continue.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    speak("Recording your response. Please say yes or no.")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

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
        speak(f"Transcription: {segment.text}")
        with open("transcription.txt", "a") as f:
            f.write(f"{segment.text}" + "\n")

def transcribe_audio_for_command(audio_file):
    # Same transcription function but with a shorter audio clip (for user commands)
    model = WhisperModel("base")
    segments, _ = model.transcribe(audio_file)
    transcription = ''
    for segment in segments:
        transcription += segment.text
    return transcription

if __name__ == "__main__":
    main()
