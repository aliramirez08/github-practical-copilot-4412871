import os
import yaml
from mutagen.easyid3 import EasyID3

# create a function that reads audio files in the mp3 format form
# the 'audio' directory and returns a list of them.

def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_files.append(file)
    return audio_files

print(get_audio_files())

def get_audio_files_with_metadata():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_file_path = os.path.join('audio', file)
            try:
                audio_metadata = EasyID3(audio_file_path)
                audio_files.append({
                    'file': file,
                    'title': audio_metadata.get('title', ['Unknown'])[0],
                    'comment': str(audio_metadata.get('comment', ['No comment'])[0])
                })
            except Exception as e:
                print(f"Error reading metadata for {file}: {e}")
    return audio_files

# Print audio files in YAML format
audio_files_with_metadata = get_audio_files_with_metadata()
print(yaml.dump(audio_files_with_metadata, default_flow_style=False))
