import matplotlib.pyplot as plt

print("--- Generating Year of the Horse Strategy ---")

# 1. The Initiatives
# We list them out so we can label the dots later
projects = [
    "Learn Python", 
    "PMP Certification", 
    "Find a Job", 
    "Learn French", 
    "Watch 50 Movies", 
    "Visit Nevada"
]

# 2. The Scores (1-10 Scale)
# Effort: 1 = Easy, 10 = Impossible
# Impact: 1 = Useless, 10 = Life Changing
effort = [8, 9, 9, 3, 2, 5]  
impact = [10, 7, 10, 2, 4, 6] 

# 3. The Scatter Plot
plt.figure(figsize=(10, 8))

# We use 'scatter' instead of 'plot'. 
# c='red' and s=100 (size) for that Chinese New Year energy.
plt.scatter(effort, impact, color='red', s=100)

# 4. The Magic: Labeling the Dots
# We loop through the data and write the project name next to each dot
for i, project in enumerate(projects):
    # (x, y, text) -> We add +0.2 to x so the text doesn't sit ON TOP of the dot
    plt.text(effort[i] + 0.2, impact[i], project, fontsize=9)

# 5. Draw the "Quadrants" (The Crosshair)
# A vertical line at Effort=5 and horizontal at Impact=5
plt.axvline(x=5, color='gold', linestyle='--')
plt.axhline(y=5, color='gold', linestyle='--')

# 6. Formatting
plt.title('Year of the Horse: Priority Matrix', fontsize=14, fontweight='bold')
plt.xlabel('Effort (Cost)', fontsize=12)
plt.ylabel('Impact (Value)', fontsize=12)
plt.grid(True, alpha=0.3)

# Set the range to 0-11 so the dots aren't squished against the edge
plt.xlim(0, 11)
plt.ylim(0, 11)

# 7. Save it
plt.savefig('priority_matrix.png')
print("Strategy map saved as 'priority_matrix.png'.")