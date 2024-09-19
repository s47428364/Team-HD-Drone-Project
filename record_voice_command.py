import pyaudio
import wave
from faster_whisper import WhisperModel


def main():
    # initialize status
    status = True
    # execute the loop to record voice command and transcribe it,
    # the result will be saved in transcription.txt
    # as input to the LLM model
    while status:
        clear_command_file("audio.wav", "transcription.txt")
        audio_file = record_audio()
        transcribe_audio(audio_file)
        do_again = input("continue? type q to quit: ")
        if  do_again == "q":
            status = False
        else:
            status = True

# inspired by ChatGPT-o1-mini (OpenAI, www.chatgpt.com).
def clear_command_file(audio_file, transcription_file):
    with open(audio_file, "w") as f:
        pass
    # with open(transcription_file, "w") as f:
    #     pass

# inspired by https://www.geeksforgeeks.org/how-to-play-and-record-audio-in-python/
def record_audio():
    # Set up recording
    CHUNK = 1024
    FORMAT = pyaudio.paInt32
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 8
    WAVE_OUTPUT_FILENAME = "audio.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

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

# see https://github.com/SYSTRAN/faster-whisper
def transcribe_audio(audio_file):
    # Initial model
    model = WhisperModel("base")
    segments, _ = model.transcribe(audio_file)
    for segment in segments:
        print("Transcription: ")
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        with open("transcription.txt", "a") as f:
            f.write("%s" % segment.text)



if __name__ == "__main__":
    main()
