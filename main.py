#############################     MADE_BY_SAYAK     ###################################
import numpy as np
import pyaudio
import time

def generate_note(frequency, duration, volume=0.5, sample_rate=44100):
    """Generates a violin note with the given frequency, duration, and volume."""
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    wave = np.sin(2 * np.pi * frequency * t) * volume
    envelope = np.concatenate((np.linspace(0, 1, int(duration * sample_rate * 0.1)), 
                                np.linspace(1, 0.8, int(duration * sample_rate * 0.8)),
                                np.linspace(0.8, 0, int(duration * sample_rate * 0.1))))
    # Resize envelope array to match the length of the wave array
    envelope = np.resize(envelope, wave.shape)
    wave*= envelope
    return wave


def play_melody(melody):
    """Plays the given melody through the computer's speakers."""
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=True)
    for note in melody:
        stream.write(note.astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()
    

notes = [293.66, 349.23, 392, 523.25, 440, 349.23, 293.66, 293.66, 349.23, 392, 523.25, 440, 349.23, 293.66, 261.63]
durations = [0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 1]

melody = []
for i in range(len(notes)):
    frequency = np.random.choice(notes)
    duration = np.random.choice(durations)
    note = generate_note(frequency, duration)
    melody.append(note)

play_melody(melody)
