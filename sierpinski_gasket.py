# -*- coding: utf-8 -*-
"""Sierpinski-Gasket.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D2EI6P0ETGZO-CxxBgr6E2AWVh74Qt78
"""

import torch
import matplotlib.pyplot as plt

def sierpinski_gasket(iterations, points_per_iteration):
    # Define the three vertices of the Sierpinski triangle
    vertices = torch.tensor([[0.0, 0.0], [1.0, 0.0], [0.5, torch.sqrt(torch.tensor(3.0))/2.0]])

    # Randomly select an initial point inside the triangle
    points = torch.zeros((points_per_iteration, 2))

    # Iterate and generate points
    for i in range(iterations):
        # Randomly select one of the vertices for each point
        selected_vertices = vertices[torch.randint(0, 3, (points_per_iteration,))]

        # Move each point halfway towards the selected vertex (this creates the fractal pattern)
        points = (points + selected_vertices) / 2.0

    return points

# Parameters
iterations = 10
points_per_iteration = 10000

# Generate the fractal using PyTorch
points = sierpinski_gasket(iterations, points_per_iteration)

# Visualize the fractal
plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1], s=0.1, color="black")
plt.title("Sierpinski Gasket using PyTorch")
plt.show()