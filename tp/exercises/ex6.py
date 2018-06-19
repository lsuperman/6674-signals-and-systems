import numpy as np

from util.signal import glottal_pulse

import matplotlib.pyplot as plt

if __name__ == "__main__":
    x, t = glottal_pulse(f0=200, Tp_pct=0.4, Tn_pct=0.16, P0=1, periods=10, fs=16000)

    plt.figure()
    plt.plot(t,x)
    plt.grid(linestyle='dashed')
    plt.title("Pulso Glótico")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.show()

    amplitude_spectrum = abs(np.fft.fft(x) / len(x))

    plt.figure()
    plt.plot(amplitude_spectrum)
    plt.show()