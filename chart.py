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
    # Base revenue with seasonal variation
    base_revenue = 100000
    seasonal_multiplier = [0.8, 0.85, 0.95, 1.0, 1.1, 1.2, 1.3, 1.25, 1.15, 1.05, 0.95, 1.4]  # Holiday boost in Dec
    
    for i, month in enumerate(months):
        # Add some random variation
        revenue = base_revenue * seasonal_multiplier[i] * (1 + np.random.normal(0, 0.1))
        # Add year-over-year growth
        revenue *= (1 + 0.05) ** (year - 2022)  # 5% annual growth
        
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

# Create figure with size calculated for exact 512x512 output at dpi=64
fig_size = 512 / 64  # 8 inches
plt.figure(figsize=(fig_size, fig_size))

# Create the lineplot
ax = sns.lineplot(data=df, x='Month', y='Revenue', hue='Year', 
                  marker='o', linewidth=2.5, markersize=6,
                  palette='viridis')

# Customize the plot
plt.title('Seasonal Revenue Trends by Year\n(Business Performance Analytics)', 
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=11, fontweight='semibold')
plt.ylabel('Revenue ($)', fontsize=11, fontweight='semibold')

# Format y-axis to show values in thousands
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, fontsize=9)
plt.yticks(fontsize=9)

# Customize legend
plt.legend(title='Year', title_fontsize=10, fontsize=9, loc='upper left')

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Tight layout to ensure everything fits
plt.tight_layout()

# Save the chart with exact specifications for 512x512 pixels
plt.savefig('chart.png', dpi=64, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("Chart saved as chart.png with 512x512 dimensions")