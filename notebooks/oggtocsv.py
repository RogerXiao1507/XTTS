import os
from pydub import AudioSegment

def convert_all_ogg_to_wav(input_folder, output_folder):
    try:
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Iterate over all files in the input folder
        for file_name in os.listdir(input_folder):
            if file_name.endswith(".ogg"):  # Process only .ogg files
                input_path = os.path.join(input_folder, file_name)
                output_file_name = os.path.splitext(file_name)[0] + ".wav"  # Change extension to .wav
                output_path = os.path.join(output_folder, output_file_name)
                
                # Convert and save the file
                print(f"Converting {file_name} to {output_file_name}...")
                audio = AudioSegment.from_ogg(input_path)
                audio.export(output_path, format="wav")
        
        print("All files converted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_folder = "/Users/rogerxiao/Downloads/XTTS/notebooks/ruanmei_data/ruan_mei_data_ogg"  # Replace with your input folder
output_folder = "/Users/rogerxiao/Downloads/XTTS/notebooks/ruanmei_data/wavs/ruan_mei_data_wav"  # Replace with your output folder

convert_all_ogg_to_wav(input_folder, output_folder)
