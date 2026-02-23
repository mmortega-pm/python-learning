import pandas as pd
import matplotlib.pyplot as plt

print("--- Generating Velocity Trendline ---")

# 1. The Noisy Daily Data (A classic erratic sprint)
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Tickets_Closed': [2, 9, 1, 8, 3, 7, 2, 8, 4, 9] 
}
df = pd.DataFrame(data)

# 2. The Secret Weapon: Rolling Average
# window=3 means it takes the average of Day 1, 2, and 3, then 2, 3, and 4, etc.
df['3_Day_Trend'] = df['Tickets_Closed'].rolling(window=3).mean()

# 3. Plotting the Story
plt.figure(figsize=(10, 6))

# Plot the raw, noisy data in the background (faint gray)
plt.plot(df['Day'], df['Tickets_Closed'], marker='o', color='#bdc3c7', linestyle='--', label='Daily Output (Noise)')

# Plot the True Trend in the foreground (bold red)
plt.plot(df['Day'], df['3_Day_Trend'], color='#e74c3c', linewidth=3, label='3-Day Trend (Reality)')

# 4. Formatting & Polish
plt.title('Team Velocity: Noise vs. Trend', fontsize=14, fontweight='bold')
plt.xlabel('Sprint Day')
plt.ylabel('Tickets Closed')
plt.legend() # This adds the key showing what the colors mean
plt.grid(True, alpha=0.3)

# 5. Save the Output
filename = 'velocity_trend.png'
plt.savefig(filename)
print(f"Analysis complete. Chart saved as '{filename}'.")