import pandas as pd
import matplotlib.pyplot as plt

# 1. The Data
data = {
    'Department': ['IT', 'HR', 'Sales', 'Ops'],
    'Budget': [50000, 20000, 85000, 42000]
}
df = pd.DataFrame(data)

# 2. The Plotting Logic
print("--- Generating Bar Chart... ---")
# 'kind=bar' makes the vertical columns
df.plot(x='Department', y='Budget', kind='bar', color='green', title='Department Budgets')

# 3. The Reveal
plt.tight_layout() # Keeps the labels from getting cut off
plt.show()