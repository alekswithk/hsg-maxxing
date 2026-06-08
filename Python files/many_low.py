import numpy as np
import matplotlib.pyplot as plt

# Define coordinates for the visualization
w0 = (10, 80)                 # Endowment point (No insurance)
separating_L = (50, 68)       # Separating contract for Low-risk
pooling_candidate = (65, 61)  # Theoretical pooling contract on the high average line

# Setting up the plot
plt.figure(figsize=(9, 7))
plt.plot([w0[0], 100], [w0[1], 30], color='black', fontweight='bold', label='Zero profit line for $p_H$ (Steep)')
plt.plot([w0[0], 100], [w0[1], 65], color='black', label='Zero profit line for $p_L$ (Flat)')
plt.plot([w0[0], 100], [w0[1], 55], color='black', linestyle='--', label='Zero profit line for ALL (High average)')

# Plotting the points
plt.scatter(*w0, color='white', edgecolor='black', s=100, zorder=5)
plt.text(w0[0]-4, w0[1]+2, r'$\vec{w}_0$', fontsize=12)

plt.scatter(*separating_L, color='green', s=80, zorder=5)
plt.text(separating_L[0]-2, separating_L[1]+3, r'$\alpha^L$ (Separating)', color='green', fontsize=11)

plt.scatter(*pooling_candidate, color='blue', s=100, zorder=5)
plt.text(pooling_candidate[0]+2, pooling_candidate[1]+2, 'Candidate\nPooling Contract', color='blue', fontsize=11, fontweight='bold')

# Sketching the L indifference curve passing through alpha^L
u_L_x = np.linspace(30, 90, 100)
u_L_y = 68 - 0.23 * (u_L_x - 50) - 0.002 * (u_L_x - 50)**2
plt.plot(u_L_x, u_L_y, color='green', alpha=0.7, label='$L$-type indifference curve')

# Highlighting the breakdown dynamics
plt.annotate('1. If separating: This pooling contract\nsits ABOVE the green curve,\nsiphoning everyone away.', 
             xy=pooling_candidate, xytext=(25, 42),
             arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10, color='blue')

plt.annotate('2. If pooling: A new competitor\ncreates a "lens" here to cream-skim\nonly the L-types away.', 
             xy=(73, 58), xytext=(55, 75),
             arrowprops=dict(facecolor='darkgreen', arrowstyle='->'), fontsize=10, color='darkgreen')

# Graph styling
plt.xlim(0, 100)
plt.ylim(20, 90)
plt.xlabel('$w_1$: wealth in bad state', fontsize=12)
plt.ylabel('$w_2$: wealth in good state', fontsize=12)
plt.title('The Non-Existence of Equilibrium (Rothschild-Stiglitz)', fontsize=14, pad=15)
plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.legend(loc='lower left')
plt.grid(alpha=0.2)
plt.show()