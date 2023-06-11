import numpy as np
import matplotlib.pyplot as plt
from perlin import *
n = 128
grid = np.ones((n,n), dtype=np.int32)

colors = np.array([[156, 212, 226], [138, 181, 73], [95, 126, 48], [186, 140, 93], [230, 206, 0] ], dtype=np.uint8)


def plot(grid):
 image = colors[grid.reshape(-1)].reshape(grid.shape+(3,))
 plt.imshow(image)

def start():
 noise = generate_fractal_noise_2d((n,n),(1,1),6)
 noise = (noise - noise.min()) / (noise.max() - noise.min())
 
 wthresh = 0.3 #wasser
 grid[noise<wthresh]=0


 potential = ((noise - wthresh) / (1 - wthresh))**2.5 * 0.7
 mask = (noise > wthresh) * (np.random.rand(n, n) < potential)
 grid[mask] = 2 #tree test

 potential = (1-((noise - wthresh) / (1 - wthresh)))**8 * 0.9
 mask = (noise<wthresh+0.2)*(noise > wthresh)*(np.random.rand(n, n) < potential)
 grid[mask]=4 #sand test

 plot(grid)
 plt.show()

start()