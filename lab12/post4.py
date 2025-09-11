# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 13:57:16 2025

@author: JENIL
"""
import numpy as np
import matplotlib.pyplot as plt
fs_d = 1000
t_d = np.linspace(0, 1, fs_d, endpoint=False)
sine_10Hz_d = np.sin(2 * np.pi * 10 * t_d)
scaled_sine = 3 * sine_10Hz_d

plt.figure(figsize=(10, 4))
plt.plot(t_d, sine_10Hz_d, label="Original 10Hz Sine")
plt.plot(t_d, scaled_sine, label="Scaled (x3)", linestyle="--")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("d) Scaled 10Hz Sine Wave")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()