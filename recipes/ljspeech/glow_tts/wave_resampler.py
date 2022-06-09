import os

import librosa
import soundfile

should_downsample = False
should_rename = True

new_rate = 22050
directory = os.path.join(os.path.dirname(os.getcwd()), 'training_data', 'wavs')
for file_name in os.listdir(directory):
    path = os.path.join(directory, file_name)
    if should_downsample:
        y, s = librosa.load(path, sr=new_rate)
        soundfile.write(path, y, new_rate)
    if should_rename:
        before_dot_wav, _ = file_name.split('.wav')
        _, track_number = before_dot_wav.split("Track ")
        if '_' in track_number:
            track_number, _ = track_number.split('_')  # remove redundant numbering from some files
        new_name = str(track_number) + '.wav'
        os.replace(path, os.path.join(directory, new_name))
