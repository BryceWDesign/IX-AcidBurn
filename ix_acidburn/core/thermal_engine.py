"""
IX-AcidBurn Thermal Engine

Simulates and analyzes heat dynamics across an AI or hardware mesh system.
Can optimize cooling, redirect compute heat, or detect overload vectors.
"""

import numpy as np

class ThermalEngine:
    def __init__(self, width=10, height=10, ambient_temp=25.0):
        self.width = width
        self.height = height
        self.grid = np.full((height, width), ambient_temp)
        self.ambient_temp = ambient_temp
        self.diffusion_rate = 0.1

    def apply_heat(self, x, y, amount):
        if 0 <= x < self.height and 0 <= y < self.width:
            self.grid[x][y] += amount
            print(f"[+] Applied heat: {amount}°C at ({x},{y})")

    def diffuse_heat(self, steps=1):
        for step in range(steps):
            new_grid = self.grid.copy()
            for x in range(1, self.height - 1):
                for y in range(1, self.width - 1):
                    neighbors = [
                        self.grid[x - 1][y],
                        self.grid[x + 1][y],
                        self.grid[x][y - 1],
                        self.grid[x][y + 1]
                    ]
                    avg = sum(neighbors) / len(neighbors)
                    delta = (avg - self.grid[x][y]) * self.diffusion_rate
                    new_grid[x][y] += delta
            self.grid = new_grid

    def cool_system(self, target_temp=30.0):
        cooled_cells = np.where(self.grid > target_temp)
        self.grid[cooled_cells] -= 1.0
        print(f"[*] Cooling applied to {len(cooled_cells[0])} overheated cells.")

    def report_hotspots(self, threshold=70.0):
        coords = np.where(self.grid >= threshold)
        return list(zip(coords[0], coords[1]))

# Example usage
if __name__ == "__main__":
    engine = ThermalEngine()
    engine.apply_heat(4, 4, 60)
    engine.diffuse_heat(steps=5)
    engine.cool_system()
    print("Hotspots:", engine.report_hotspots())
