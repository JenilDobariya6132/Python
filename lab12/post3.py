# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 13:55:19 2025

@author: JENIL
"""
import numpy as np
import matplotlib.pyplot as plt
fs_c = 1000
t_c = np.linspace(0, 1, fs_c, endpoint=False)
original_sine = np.sin(2 * np.pi * 5 * t_c)
shifted_sine = np.sin(2 * np.pi * 5 * (t_c - 0.1))

plt.figure(figsize=(10, 4))
plt.plot(t_c, original_sine, label="Original 5Hz Sine")
plt.plot(t_c, shifted_sine, label="Shifted by 0.1s", linestyle="--")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("c) Time-Shifted 5Hz Sine Wave")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
