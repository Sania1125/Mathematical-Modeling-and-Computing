import matplotlib.pyplot as plt
import numpy as np

# Exponential population growth model
def population_growth(t, P0, r):
    return P0 * np.exp(r * t)

# Time points
t = np.linspace(0, 10, 100)
P0 = 100  # Initial population
r = 0.3   # Growth rate

# Population over time
P = population_growth(t, P0, r)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(t, P, label="Population Growth", color='green')
plt.title("Exponential Population Growth")
plt.xlabel("Time (years)")
plt.ylabel("Population")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
