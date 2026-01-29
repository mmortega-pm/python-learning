import pandas as pd

data = {
    'Server_ID': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6'],
    'Status': ['Active', 'Down', 'Maintenance', 'Active', 'Down', 'Active'],
    'Region': ['US-East', 'US-West', 'EU-West', 'US-East', 'EU-West', 'US-East'],
    'Load_Percent': [45, 0, 0, 92, 0, 15]
}
df = pd.DataFrame(data)

print("\n")
print("--- Server Logs ---")
print("\n")
print(df)
print("\n")

print("--- Filter 1: Servers in East or West of US ---")
print("\n")
print(df[(df['Region'] == 'US-East') | (df['Region'] == 'US-West')])

print("\n")
print("--- Filter 2: Inactive Servers ---")
print("\n")
print(df[(df['Status'] != 'Active')])

print("\n")
print("--- Filter 3: Active Servers with Loads 90+ ---")
print("\n")
print(df[(df['Status'] == 'Active') & (df['Load_Percent'] > 90)])
print("\n")