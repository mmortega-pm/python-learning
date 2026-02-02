import pandas as pd
import matplotlib.pyplot as plt

# 1. The Data (Sales Trajectory)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [30500, 32000, 45000, 28000, 51000]
}
df = pd.DataFrame(data)

print("--- Generating Professional Chart ---")

# 2. The Plotting Logic
# - marker='o': Puts dots on the data points
# - grid=True: Adds the background lines (Crucial for reading values)
df.plot(x='Month', y='Sales', kind='line', color='purple', marker='o', grid=True, title='2026 Sales Trajectory')

# 3. The Save (This creates the file)
output_filename = 'day18_sales_report.png'
plt.savefig(output_filename)

print(f"Success! Chart saved to: {output_filename}")