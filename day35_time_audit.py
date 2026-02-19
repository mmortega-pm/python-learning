import matplotlib.pyplot as plt

print("--- Generating Time Allocation Audit ---")

# 1. The Data (Your 24 Hours)
# Adjust these numbers to reflect your actual target schedule
categories = ['Sleep', 'Job Search', 'Python & Skills', 'Meals & Life', 'PMP Prep']
hours = [7.5, 6.0, 3.0, 5.5, 2.0]  # Total should equal 24

# 2. The "Explode" Strategy
# We want to highlight 'Job Search' (the 2nd item, index 1)
# 0.1 pulls that slice out by 10%. The zeros keep the rest anchored.
explode_settings = [0, 0.1, 0, 0, 0] 

# 3. Professional Color Palette
colors = ['#2c3e50', '#e74c3c', '#3498db', '#95a5a6', '#f39c12']

# 4. Draw the Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(hours, 
        labels=categories, 
        explode=explode_settings, 
        colors=colors, 
        autopct='%1.1f%%',    # Auto-calculate percentages to 1 decimal point
        startangle=140,       # Rotates the start of the pie for better readability
        shadow=True)

# 5. Formatting & Polish
plt.title('Daily Resource Allocation (Target State)', fontsize=14, fontweight='bold')
plt.axis('equal') # Forces the chart to be a perfect circle

# 6. Save the Output
filename = 'time_audit.png'
plt.savefig(filename)
print(f"Audit complete. Chart saved successfully as '{filename}'.")