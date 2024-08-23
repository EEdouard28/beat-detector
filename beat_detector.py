# Python script where code is generated from

import librosa
import librosa.beat

# path to my audio file
audio_file = 'audio/Santorini - 11-4-23_Demo.mp3'

# load the audio file
y, sr = librosa(audio_file)

print(f"Audio loaded successfully: {audio_file}")
print(f"Sample rate: {sr}")

# Get tempo and beat frames
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print(f"Estimated tempo: {tempo} BPM")