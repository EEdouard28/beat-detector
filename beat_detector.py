# Python script where code is generated from

import librosa
import librosa.beat
import matplotlib.pyplot as plt
import librosa.display

# path to my audio file
audio_file = 'audio/Santorini - 11-4-23_Demo.mp3'

# load the audio file
y, sr = librosa.load(audio_file)

print(f"Audio loaded successfully: {audio_file}")
print(f"Sample rate: {sr}")

# Get tempo and beat frames
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print(f"Estimated tempo: {tempo} BPM")

# Convert beat frames to timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print("Beat times (in seconds):", beat_times)


# Plot the waveform
plt.figure(figsize=(14, 5))
librosa.display.waveshow(y, sr=sr, alpha=0.6)

#Plot the beat times on the waveform
plt.vlines(beat_times, ymin=-1, ymax=1, color='r', linestyle='--', label='Beats')

plt.xlabel('Time (S)')
plt.ylabel('Amplitude')
plt.title('Beat Detection')
plt.legend()
plt.show()

# Smooth signal w/ Fourier transform
tempo, beat_frames = librosa.beat.beat_track(y=librosa.effects.harmonic(y), sr=sr)


# Save the beat timestamps to a text file
with open('beat_times.txt', 'w') as f:
    for beat in beat_times:
        f.write(f"{beat}\n")
