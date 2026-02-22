import matplotlib.pyplot as plt
import seaborn as sns

print("--- Generating Issue Hotspot Heatmap ---")

# 1. The Data Matrix (Number of critical tickets)
# Rows: Frontend, Backend, Database, Mobile
# Cols: Mon, Tue, Wed, Thu, Fri
bug_data = [
    [2, 0, 1, 4, 1], # Frontend
    [5, 9, 2, 0, 3], # Backend (Ouch, Tuesday was rough)
    [0, 1, 0, 0, 0], # Database
    [3, 4, 6, 2, 5]  # Mobile
]

teams = ['Frontend', 'Backend', 'Database', 'Mobile']
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

# 2. Draw the Heatmap
plt.figure(figsize=(8, 5))

# cmap='Reds' uses a white-to-red color scale. 
# annot=True puts the numbers inside the squares.
sns.heatmap(bug_data, annot=True, cmap='Reds', xticklabels=days, yticklabels=teams, linewidths=1)

# 3. Formatting (TPM Polish)
plt.title('Weekly Bug Hotspots by Team', fontsize=14, fontweight='bold')
plt.tight_layout()

# 4. Save the Output
filename = 'bug_heatmap.png'
plt.savefig(filename)
print(f"Hotspot analysis complete. Chart saved as '{filename}'.")