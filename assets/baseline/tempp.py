import numpy as np



def Rx(theta: float):
    return np.array([
        [np.cos(theta/2), -1j * np.sin(theta/2)],
        [-1j * np.sin(theta/2), np.cos(theta/2)]
    ])

def Ry(theta: float):
    return np.array([
        [np.cos(theta/2), -np.sin(theta/2)],
        [np.sin(theta/2), np.cos(theta/2)]
    ])

def Rz(theta: float):
    return np.array([
        [np.exp(-1j * theta/2), 0],
        [0, np.exp(1j * theta/2)]
    ])



def CZ():
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, -1]
    ])


def A(theta):
    return np.array([
        [np.cos(theta/2), -1j * np.sin(theta/2)],
        [1j * np.sin(theta/2), np.cos(theta/2)]
    ])