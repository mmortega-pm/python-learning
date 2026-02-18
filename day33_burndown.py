import pandas as pd
import matplotlib.pyplot as plt

print("--- Generating Burndown Chart ---")

# 1. The Data (Dates vs Tasks Remaining)
data = {
    'Date': ['2026-02-01', '2026-02-05', '2026-02-10', '2026-02-15', '2026-02-20'],
    'Tasks_Left': [50, 42, 30, 15, 5] # Ideally, this hits 0 by deadline
}
df = pd.DataFrame(data)

# 2. THE CRITICAL STEP: Convert Text to Real Dates
# If you don't do this, Python sorts them alphabetically (bad).
# This is like casting to DATE in SQL.
df['Date'] = pd.to_datetime(df['Date'])

# 3. The Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Tasks_Left'], marker='o', color='red', linestyle='--')

# 4. Formatting
plt.title('Project Alpha Burndown')
plt.xlabel('Timeline')
plt.ylabel('Tasks Remaining')
plt.grid(True)
plt.axhline(y=0, color='black', linewidth=1) # The Finish Line

# 5. Save it
plt.savefig('burndown_chart.png')
print("Chart saved as 'burndown_chart.png'.")