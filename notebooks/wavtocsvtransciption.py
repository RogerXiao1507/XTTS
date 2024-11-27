import speech_recognition as sr
import pandas as pd

def transcribe_audio_to_csv(wav_file, csv_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(wav_file) as source:
        print("Loading audio file...")
        audio_data = recognizer.record(source)

    try:
        # Transcribe the audio
        print("Transcribing audio...")
        transcription = recognizer.recognize_google(audio_data)
        
        # Save the transcription to a CSV file
        data = {"Transcription": [transcription]}
        df = pd.DataFrame(data)
        df.to_csv(csv_file, index=False)
        print(f"Transcription saved to {csv_file}")
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Example usage
wav_file = "/Users/rogerxiao/Downloads/XTTS/notebooks/ruan_mei_data_wav/VO_Archive_Ruan_Mei_1 (1).wav"  # Replace with your WAV file path
csv_file = "/Users/rogerxiao/Downloads/XTTS/notebooks/transcription1.csv"  # Output CSV file
transcribe_audio_to_csv(wav_file, csv_file)

