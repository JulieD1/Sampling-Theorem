import numpy as np
import matplotlib.pyplot as plt



# Constants
# Sampling Frequency 
fs = 1000

t = np.arange(0, 2, 1/fs)
x = np.cos(2 * np.pi * 12 * t)

# Sampling frequencies
fs_list = [100, 21, 11]

# Plotting
for i, fs_i in enumerate(fs_list):
    # Sampling
    t_i = np.arange(0, 2, 1/fs_i)
    x_i = np.cos(2 * np.pi * 12 * t_i)

    # Reconstruction
    t_recon = np.arange(0, 2, 1/fs)
    x_recon = np.interp(t_recon, t_i, x_i)

    # Plotting
    plt.figure()
    plt.subplot(3, 1, 1)
    plt.plot(t, x)
    plt.xlabel('Time')
    plt.ylabel('Voltage')
    plt.title('Original Signal')

    plt.subplot(3, 1, 2)
    plt.stem(t_i, x_i)
    plt.xlabel('Time')
    plt.ylabel('Voltage')
    plt.title('Discrete signal at fs = {} Hz'.format(fs_i))

    plt.subplot(3, 1, 3)
    plt.plot(t_recon, x_recon)
    plt.xlabel('Time')
    plt.ylabel('Voltage')
    plt.title('Reconstructed signal at fs = {} Hz'.format(fs_i))
    plt.subplots_adjust(hspace=1) 

plt.show()
