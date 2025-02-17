import os
import yaml
import eyed3
import time

def format_duration(seconds):
    # Convert seconds to HH:MM:SS format
    return time.strftime('%H:%M:%S', time.gmtime(seconds))

def get_audio_files():
    audio_files = []
    # Iterate over all files in the 'audio' directory
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            # Load the audio file using eyed3
            audio_file = eyed3.load(os.path.join('audio', file))
            comments = ''
            # Extract comments from the audio file if available
            if audio_file.tag.comments:
                comments = ' '.join(comment.text for comment in audio_file.tag.comments)
            file_path = os.path.join('audio', file)
            # Append audio file details to the list
            audio_files.append({
                'title': audio_file.tag.title,
                'description': comments,
                'file': f'/audio/{file}',  # Prefixed filename
                'duration': format_duration(audio_file.info.time_secs),  # Duration in HH:MM:SS format
                'length': f"{os.path.getsize(file_path):,}"  # Size in bytes with commas
            })
    return audio_files

with open('episodes.yaml', 'w') as file:
    yaml.dump(get_audio_files(), file, sort_keys=False)