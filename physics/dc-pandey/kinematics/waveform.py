import librosa
import librosa.display
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load the audio file
audio_file = 'speech.mp3'
y, sr = librosa.load(audio_file)

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(10, 4))
line, = ax.plot([], [])

# Function to update the waveform animation


def update(frame):
    ax.clear()
    ax.plot(y[:frame*1000])  # plot the waveform
    ax.set_title('Audio Waveform')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_xlim(0, len(y)/sr)
    ax.set_ylim(-1, 1)
    return ax,


# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=int(len(y)/1000), interval=1000, blit=True)  # add blit=True to optimize redrawing

# Save the animation as a GIF
ani.save('audio_waveform_animation.mp4', writer='ffmpeg')

plt.show()
