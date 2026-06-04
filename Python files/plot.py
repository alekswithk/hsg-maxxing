import numpy as np
import matplotlib.pyplot as plt

# 1. Sample data
X = np.array([1, 2, 3, 4, 5])
Y = np.array([1.5, 3.8, 4.2, 6.5, 7.0])

# 2. Linear regression calculations
mean_Y = np.mean(Y)
slope, intercept = np.polyfit(X, Y, 1)
Y_pred = slope * X + intercept

# 3. Create the plots matching the Econometrics standard
fig, axs = plt.subplots(1, 3, figsize=(16, 5), sharex=True, sharey=True)

# Plot 1: SST (Total)
axs[0].scatter(X, Y, color='black', s=80, zorder=5, label='Actual Data ($Y$)')
axs[0].axhline(mean_Y, color='blue', linestyle='--', linewidth=2, label=r'Mean ($\bar{Y}$)')
for xi, yi in zip(X, Y):
    axs[0].plot([xi, xi], [mean_Y, yi], color='red', linewidth=2, linestyle='-')
axs[0].set_title('SST (Total Sum of Squares)\nDistance: Actual Data to Mean', fontsize=12)
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
axs[0].legend(loc='upper left')
axs[0].grid(True, alpha=0.3)

# Plot 2: SSE (Explained Sum of Squares) - Regression line to Mean
axs[1].scatter(X, Y, color='black', alpha=0.2, s=80, zorder=5)
axs[1].plot(X, Y_pred, color='green', linewidth=2, label=r'Regression Line ($\hat{Y}$)')
axs[1].axhline(mean_Y, color='blue', linestyle='--', linewidth=2, label=r'Mean ($\bar{Y}$)')
for xi, y_pred_i in zip(X, Y_pred):
    axs[1].plot([xi, xi], [mean_Y, y_pred_i], color='orange', linewidth=2, linestyle='-')
axs[1].set_title('SSE (Explained Sum of Squares)\nDistance: Regression Line to Mean', fontsize=12)
axs[1].set_xlabel('X')
axs[1].legend(loc='upper left')
axs[1].grid(True, alpha=0.3)

# Plot 3: SSR (Residual Sum of Squares) - Actual data to Regression line
axs[2].scatter(X, Y, color='black', s=80, zorder=5, label='Actual Data ($Y$)')
axs[2].plot(X, Y_pred, color='green', linewidth=2, label=r'Regression Line ($\hat{Y}$)')
for xi, yi, y_pred_i in zip(X, Y, Y_pred):
    axs[2].plot([xi, xi], [y_pred_i, yi], color='purple', linewidth=2, linestyle='-')
axs[2].set_title('SSR (Residual Sum of Squares)\nDistance: Actual Data to Regression Line', fontsize=12)
axs[2].set_xlabel('X')
axs[2].legend(loc='upper left')
axs[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()