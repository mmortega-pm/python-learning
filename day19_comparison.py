import pandas as pd
import matplotlib.pyplot as plt

# 1. The Data (Revenue vs Expenses)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Revenue': [30000, 35000, 40000, 45000, 50000],
    'Expenses': [25000, 27000, 50000, 28000, 30000]
}
df = pd.DataFrame(data)

print("--- Generating Comparison Chart ---")

# 2. The Plotting Logic
# y=['Revenue', 'Expenses'] tells Python to draw two lines
# We use the 'gca()' (Get Current Axis) trick to put them on the same graph
ax = df.plot(x='Month', y=['Revenue', 'Expenses'], kind='line', marker='o', grid=True, title='Q1-Q2 Financials')

# 3. Labeling (Context is King)
ax.set_ylabel("Amount ($)")
ax.set_xlabel("Time Period")

# 4. Save it
plt.savefig('day19_profit_loss.png', facecolor='white')
print("Comparison chart saved.")