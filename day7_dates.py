import pandas as pd
from datetime import datetime

# 1. The Data (Dates are just 'Strings' right now)
data = {
    'Project': ['Alpha', 'Beta', 'Gamma'],
    'Start_Date': ['2025-01-01', '2025-01-10', '2025-01-15'],
    'Deadline': ['2025-02-01', '2025-03-01', '2025-02-15']
}
df = pd.DataFrame(data)

# 2. The Conversion
# ACTION: Tell Python these columns are actually Dates
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['Deadline'] = pd.to_datetime(df['Deadline'])

# 3. The Math
# How long is the project? (Deadline - Start)
df['Duration'] = df['Deadline'] - df['Start_Date']

# 4. Extracting Specifics
# "I just want to know the Month it starts"
df['Start_Month'] = df['Start_Date'].dt.month_name()

print("--- Project Timelines ---")
print(df)