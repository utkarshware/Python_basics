import numpy as np
import matplotlib.pyplot as plt
import random

width, height = 1920, 1080

x = np.linspace(-10, 10, width)
y = np.linspace(-10, 10, height)
X, Y = np.meshgrid(x, y)

Z = np.sin(X**2 + Y**2) + np.cos(X * Y) + np.sin(X * Y / random.uniform(1, 10))

colormap = random.choice(['plasma', 'viridis', 'inferno', 'magma', 'cividis', 'turbo'])

plt.figure(figsize=(16, 9), dpi=120)
plt.axis('off')
plt.imshow(Z, cmap=colormap, extent=(-10, 10, -10, 10))
plt.tight_layout()

output_file = "abstract_art_wallpaper.png"
plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
plt.show()

print(f"Your abstract art has been saved as {output_file}. Use it as your wallpaper!")

