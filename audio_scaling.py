import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
import sounddevice as sd

# ----------------------------------------
# AUDIO SETTINGS
# ----------------------------------------

sample_rate = 44100
block_size = 1024

# Scalar k
volume = 1.0

# Time tracker
t = 0

# ----------------------------------------
# CREATE FIGURE
# ----------------------------------------

fig, ax = plt.subplots(figsize=(12, 5))

plt.subplots_adjust(bottom=0.25)

x = np.arange(block_size)

line, = ax.plot(x, np.zeros(block_size))

ax.set_ylim(-1.5, 1.5)
ax.set_xlim(0, block_size)

ax.set_title("Live Audio Gain (Scalar Multiplication)")
ax.set_xlabel("Samples")
ax.set_ylabel("Amplitude")

ax.grid(True)

# ----------------------------------------
# SLIDER
# ----------------------------------------

slider_ax = plt.axes([0.2, 0.1, 0.6, 0.03])

volume_slider = Slider(
    slider_ax,
    'k (Volume Scalar)',
    0,
    3,
    valinit=1
)

# ----------------------------------------
# MUSIC GENERATOR
# ----------------------------------------

def generate_music(frames):

    global t
    global volume

    # Time vector
    time = (
        np.arange(frames) + t
    ) / sample_rate

    # --------------------------------
    # CREATE REAL MUSICAL NOTES
    # --------------------------------

    melody = (
        0.5 * np.sin(2 * np.pi * 261 * time) +   # C
        0.3 * np.sin(2 * np.pi * 329 * time) +   # E
        0.2 * np.sin(2 * np.pi * 392 * time)     # G
    )

    # --------------------------------
    # CREATE RHYTHM ENVELOPE
    # --------------------------------
    beat = (
        np.sin(2 * np.pi * 2 * time) > 0
    ).astype(float)
    signal = melody * beat

    # --------------------------------
    # SCALAR MULTIPLICATION
    # --------------------------------
    signal = signal * volume
    # Prevent clipping
    signal = np.clip(signal, -1, 1)
    t += frames
    return signal.astype(np.float32)

# ----------------------------------------
# AUDIO CALLBACK
# ----------------------------------------

latest_signal = np.zeros(block_size)

def audio_callback(outdata, frames, time_info, status):

    global latest_signal
    signal = generate_music(frames)
    latest_signal = signal
    outdata[:] = signal.reshape(-1, 1)

# ----------------------------------------
# START AUDIO STREAM
# ----------------------------------------

stream = sd.OutputStream(
    callback=audio_callback,
    channels=1,
    samplerate=sample_rate,
    blocksize=block_size
)

stream.start()

# ----------------------------------------
# UPDATE GRAPH
# ----------------------------------------

def animate(frame):

    line.set_ydata(latest_signal)

    return line,

ani = FuncAnimation(
    fig,
    animate,
    interval=30,
    blit=True
)

# ----------------------------------------
# UPDATE VOLUME
# ----------------------------------------

def update(val):
    global volume
    volume = volume_slider.val

volume_slider.on_changed(update)

# ----------------------------------------
# SHOW
# ----------------------------------------
plt.show()

# ----------------------------------------
# STOP STREAM
# ----------------------------------------
stream.stop()
stream.close()