import plotly.express as px
import pandas as pd

print("--- Building Interactive Timeline ---")

# 1. The Project Data (TPM Style)
# We define Tasks, Start Dates, End Dates, and Status
data = [
    dict(Task="Job Search", Start='2026-01-01', Finish='2026-02-28', Status='Ongoing'),
    dict(Task="Learn Python", Start='2026-01-15', Finish='2026-03-15', Status='Ongoing'),
    dict(Task="PMP Certification", Start='2026-02-01', Finish='2026-02-28', Status='Critical'),
    dict(Task="Move to Seattle", Start='2026-03-01', Finish='2026-03-10', Status='Planned')
]

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Create the Gantt Chart
# x_start/x_end = Where the bar begins and ends
# y = The label on the left (Task Name)
# color = Color the bars based on 'Status'
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Status")

# 4. Invert the Y-axis (Otherwise it lists them bottom-to-top)
fig.update_yaxes(autorange="reversed")

# 5. Save as HTML (The Magic Step)
fig.write_html("project_timeline.html")

print("Success! Open 'project_timeline.html' in your browser.")