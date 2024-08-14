# -*- coding: utf-8 -*-
"""Ikeda_map_plot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OK6SDQ6xpHutD7J4rpDvgwbugdVkb45H
"""

import torch
import numpy as np
import matplotlib.pyplot as plt

# Confirm the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Parameters in Ikeda map
A = torch.tensor(0.9, device=device)
B = torch.tensor(0.9, device=device)
kappa = torch.tensor(0.4, device=device)
rho = torch.tensor(6.0, device=device)
iterations = 1000
num_points = 200  # the num of initial point

# The initial points are generated in the complex plane
np.random.seed(0)
x = torch.rand(num_points, device=device) * 8 - 4
y = torch.rand(num_points, device=device) * 8 - 4
z = torch.complex(x, y)

# Initialize the tensor to store the result of the computation
zs = z.clone()
trajectory = torch.zeros((num_points, iterations), dtype=torch.complex64, device=device)

# Ikeda Map Calculation
for i in range(iterations):
    # Calculate theta_n for all points
    theta_n = kappa - rho / (1 + torch.abs(zs)**2)
    # Update zs for all points: zs = A + B * zs * exp(1j * theta_n)
    zs = A + B * zs * torch.exp(1j * theta_n)
    # Store the new values
    trajectory[:, i] = zs

# Move the result to the CPU for plotting
trajectory_cpu = trajectory.cpu().numpy()

# Draw the main and inset images
fig, main_ax = plt.subplots(figsize=(12, 8))

# Plot the main trajectory
for i in range(num_points):
    main_ax.plot(trajectory_cpu[i].real, trajectory_cpu[i].imag, 'k-', lw=0.5)

# Set the main plot label and scope
main_ax.set_xlabel("Real")
main_ax.set_ylabel("Imaginary")
main_ax.set_xlim([-4, 4])
main_ax.set_ylim([-5, 5])

# Inset: Enlarged view of the main trajectory diagram
right_inset_ax = fig.add_axes([0.7, 0.7, 0.2, 0.2])
for i in range(num_points):
    right_inset_ax.plot(trajectory_cpu[i].real, trajectory_cpu[i].imag, 'k-', lw=0.5)
right_inset_ax.set_xlim([0, 2])
right_inset_ax.set_ylim([-2, 0])

plt.show()