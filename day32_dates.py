from datetime import datetime

print("--- SQL Logic in Python ---")

# 1. Get the current moment (Like SQL's NOW())
now = datetime.now()

# 2. The 'EXTRACT' Equivalent (For Math/Filtering)
# We just pull the property directly. It returns a NUMBER (2).
raw_month = now.month
raw_day = now.day

print(f"EXTRACT Logic (Raw Number): {raw_month}")

# 3. The 'TO_CHAR' Equivalent (For Pretty Reports)
# We use strftime (String Format Time). It returns TEXT ('February').
# %B = Full Month Name
# %A = Full Weekday Name
pretty_month = now.strftime("%B")
pretty_day = now.strftime("%A")

print(f"TO_CHAR Logic (Pretty Text): {pretty_month}, {pretty_day}")

# 4. The Logic Check
if raw_month == 2:
    print("Logic: We are in the second month (Math works).")
    
if pretty_month == "February":
    print("Logic: The calendar says February (Text works).")