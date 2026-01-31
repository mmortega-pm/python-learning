import pandas as pd
import matplotlib.pyplot as plt

# 1. The Data
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [100, 120, 115, 150, 180]
}
df = pd.DataFrame(data)

# 2. The Plotting Logic
print("--- Generating Chart... ---")
# 'x' is the bottom axis, 'y' is the side axis
df.plot(x='Day', y='Revenue', kind='line', title='Weekly Revenue', marker='o')

# 3. The Reveal
plt.show()