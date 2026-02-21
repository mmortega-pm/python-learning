import matplotlib.pyplot as plt

print("--- Generating Executive Dashboard ---")

# 1. The Data
# Left Chart Data: Sprint Burndown
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
tasks_left = [40, 32, 25, 15, 5]

# Right Chart Data: Ticket Status
statuses = ['To Do', 'In Progress', 'Review', 'Done']
ticket_counts = [5, 10, 8, 22]

# 2. Create the Dashboard Canvas
# 1 row, 2 columns. figsize=(12, 5) makes it wide enough to fit both.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 3. Build Chart 1 (Left Side - Burndown)
ax1.plot(days, tasks_left, color='#e74c3c', marker='o', linewidth=2)
ax1.set_title('Sprint Burndown', fontweight='bold')
ax1.set_ylabel('Tasks Remaining')
ax1.grid(True, linestyle='--', alpha=0.6)

# 4. Build Chart 2 (Right Side - Status)
ax2.bar(statuses, ticket_counts, color=['#d3d3d3', '#3498db', '#f39c12', '#2ecc71'])
ax2.set_title('Current Ticket Status', fontweight='bold')
ax2.set_ylabel('Ticket Count')

# 5. Polish and Save
# tight_layout() ensures the charts don't overlap or squish together
plt.tight_layout() 

filename = 'sprint_dashboard.png'
plt.savefig(filename)
print(f"Success! Dashboard saved as '{filename}'.")