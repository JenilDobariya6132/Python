# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 13:58:08 2025

@author: JENIL
"""
import numpy as np
import matplotlib.pyplot as plt
fs_e = 1000
t_e = np.linspace(0, 1, fs_e, endpoint=False)
sine_5Hz_e = np.sin(2 * np.pi * 5 * t_e)
reversed_sine = sine_5Hz_e[::-1]

plt.figure(figsize=(10, 4))
plt.plot(t_e, sine_5Hz_e, label="Original 5Hz Sine")
plt.plot(t_e, reversed_sine, label="Reversed Signal", linestyle="--")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("e) Time-Reversed 5Hz Sine Wave")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()