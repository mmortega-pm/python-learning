import pandas as pd

# Create a simple dataset
data = {
    'Name': ['Mauricio', 'Wil', 'Derick'],
    'Role': ['TPM', 'Strategist', 'Tech Lead'],
    'City': ['NYC', 'NYC', 'NYC']
}

# Turn it into a DataFrame (Excel-style table)
df = pd.DataFrame(data)

# Print it to the screen
print("--- My First Data Team ---")
print(df)