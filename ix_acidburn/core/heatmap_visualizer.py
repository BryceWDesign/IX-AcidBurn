"""
IX-AcidBurn Heatmap Visualizer

Provides dynamic system and process-level heatmap overlays to identify
high-load areas, thermal signatures, or vectorized AI resource distribution.
"""

import random
import numpy as np
import matplotlib.pyplot as plt

class HeatmapVisualizer:
    def __init__(self, grid_size=(10, 10)):
        self.grid_size = grid_size
        self.grid = np.zeros(grid_size)

    def generate_mock_data(self):
        self.grid = np.random.rand(*self.grid_size) * 100

    def inject_hotspot(self, x: int, y: int, intensity: float = 100.0):
        if 0 <= x < self.grid_size[0] and 0 <= y < self.grid_size[1]:
            self.grid[x][y] = intensity

    def display_heatmap(self, title="System Load Heatmap"):
        plt.imshow(self.grid, cmap='hot', interpolation='nearest')
        plt.title(title)
        plt.colorbar()
        plt.show()

# Example usage
if __name__ == "__main__":
    viz = HeatmapVisualizer()
    viz.generate_mock_data()
    viz.inject_hotspot(5, 5, 200)
    viz.display_heatmap()
