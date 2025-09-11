# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 13:53:16 2025

@author: JENIL
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------- a. Add two sine waves (5Hz + 10Hz) ----------
fs_a = 1000  # Sampling frequency
t_a = np.linspace(0, 1, fs_a, endpoint=False)
sine_5Hz = np.sin(2 * np.pi * 5 * t_a)
sine_10Hz = np.sin(2 * np.pi * 10 * t_a)
added_signal = sine_5Hz + sine_10Hz

plt.figure(figsize=(10, 4))
plt.plot(t_a, added_signal, label="5Hz + 10Hz Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("a) Sum of 5Hz and 10Hz Sine Waves")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
