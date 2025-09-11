# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 13:54:43 2025

@author: JENIL
"""
import numpy as np
import matplotlib.pyplot as plt

fs_b = 500
t_b = np.linspace(0, 2, 2*fs_b, endpoint=False)
sine_5Hz_b = np.sin(2 * np.pi * 5 * t_b)
cosine_10Hz_b = np.cos(2 * np.pi * 10 * t_b)
multiplied_signal = sine_5Hz_b * cosine_10Hz_b

plt.figure(figsize=(10, 4))
plt.plot(t_b, multiplied_signal, label="Sine(5Hz) * Cosine(10Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("b) Product of 5Hz Sine and 10Hz Cosine")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()