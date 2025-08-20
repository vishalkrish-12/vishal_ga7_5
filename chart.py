import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data for seasonal revenue patterns
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create data for 3 years with seasonal patterns
years = [2022, 2023, 2024]
data = []

for year in years:
    base_revenue = 100000
    seasonal_multiplier = [0.8, 0.85, 0.95, 1.0, 1.1, 1.2, 1.3, 1.25, 1.15, 1.05, 0.95, 1.4]
    
    for i, month in enumerate(months):
        revenue = base_revenue * seasonal_multiplier[i] * (1 + np.random.normal(0, 0.1))
        revenue *= (1 + 0.05) ** (year - 2022)
        data.append({
            'Month': month,
            'Year': year,
            'Revenue': revenue
        })

# Create DataFrame
df = pd.DataFrame(data)

# Set up the plot style
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.7)

# Compute figure size in inches for exact 512x512 pixels at 100 DPI
fig_size = 5.12  # inches

plt.figure(figsize=(fig_size, fig_size))

# Create the lineplot
ax = sns.lineplot(
    data=df,
    x='Month',
    y='Revenue',
    hue='Year',
    marker='o',
    linewidth=2.5,
    markersize=6,
    palette='viridis'
)

# Customize the plot
plt.title(
    'Seasonal Revenue Trends by Year\n(Business Performance Analytics)',
    fontsize=14,
    fontweight='bold',
    pad=15
)
plt.xlabel('Month', fontsize=11, fontweight='semibold')
plt.ylabel('Revenue ($)', fontsize=11, fontweight='semibold')

# Format y-axis to show values in thousands
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K')
)

# Rotate x-axis labels for readability
plt.xticks(rotation=45, fontsize=9)
plt.yticks(fontsize=9)

# Customize legend
plt.legend(
    title='Year',
    title_fontsize=10,
    fontsize=9,
    loc='upper left'
)

# Add subtle gridlines
plt.grid(True, alpha=0.3)

# Tight layout with no padding
plt.tight_layout(pad=0)

# Save the chart with exact 512x512 pixel dimensions
plt.savefig(
    'chart.png',
    dpi=100,
    bbox_inches='tight',
    pad_inches=0,
    facecolor='white'
)

print("Chart saved as chart.png (512×512 pixels)")
