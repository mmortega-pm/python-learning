import matplotlib.pyplot as plt

print("--- Generating Cycle Time Distribution ---")

# 1. The Data (How many days did each Jira ticket take to close?)
# Notice most take 2-4 days, but a few nasty ones took 12+ days.
cycle_times = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 8, 9, 12, 14, 15]

# 2. Draw the Histogram
plt.figure(figsize=(10, 6))

# bins=5 means we group the data into 5 distinct buckets (e.g., 1-3 days, 4-6 days, etc.)
# edgecolor='white' adds a clean line between the bars so they don't blur together
plt.hist(cycle_times, bins=5, color='#8e44ad', edgecolor='white')

# 3. Formatting (TPM Polish)
plt.title('Sprint Cycle Time Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Days to Close Ticket', fontsize=12)
plt.ylabel('Number of Tickets', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 4. Save the Output
filename = 'cycle_time_histogram.png'
plt.savefig(filename)
print(f"Analysis complete. Chart saved as '{filename}'.")