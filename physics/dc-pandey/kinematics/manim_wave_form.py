from manim import *
import numpy as np
import librosa


class AudioWaveform(Scene):
    def construct(self):
        # Load the audio file
        audio_file = 'speech.mp3'
        y, sr = librosa.load(audio_file)

        # Generate waveform points
        t = np.linspace(0, len(y) / sr, len(y))
        waveform_points = [(t[i], y[i]) for i in range(len(y))]

        # Create the waveform
        waveform = VGroup(*[
            Line(start=(p1[0], p1[1], 0), end=(p2[0], p2[1], 0), color=BLUE)
            for p1, p2 in zip(waveform_points[:-1], waveform_points[1:])
        ])

        # Scale the waveform to fit the screen
        waveform.scale(3)
        self.add(waveform)

        # Play the audio
        self.play(AudioObject(file_path=audio_file))

        # Animate the waveform
        self.play(ShowCreation(waveform), run_time=len(y) / sr)
