"""
This code defines an AngleBuffer class that stores recent angle measurements
and computes their average to smooth out fluctuations in gaze tracking.
"""
import collections
import numpy as np

class AngleBuffer:
    def __init__(self, size=40):
        self.size = size
        self.buffer = collections.deque(maxlen=size)

    def add(self, angles):
        self.buffer.append(angles)

    def get_average(self):
        return np.mean(self.buffer, axis=0)
