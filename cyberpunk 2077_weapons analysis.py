## cyberpunk 2077 weapons analysis

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/yoshili/Desktop/python shit/cyberpunk_weapons_data.csv')

print("Data loaded!")
print(f"Total weapons: {len(df)}")
print(f"\nFirst 5 Weapons")
print(df.head())

## calculating DPS (damage per second), DPS = damage per hit*attack speed
df['DPS'] = df['Damage_Per_Hit'] * df['Attack_Speed']

print("\n" + "="*50)
print("DPS CALCULATED!")
print("="*50)
print("\nTop 5 weapons by DPS")
print(df.nlargest(5,'DPS')[['Weapon_Name', 'Category', 'Damage_Per_Hit', 'Attack_Speed', 'DPS']])

## build type scoring
print("\n" + "="*50)
print("\nBUILD TYPE ANALYSIS")
print("="*50)

df_clean = df.fillna(0) # fill NAs with 0 so that calcs don't break

# NETRUNNER BUILD - loves smart weapons, range, moderate DPS
df_clean['Netrunner_Score'] = (
    (df_clean['DPS'] * 0.5) +
    (df_clean['Effective_Range'] * 2) +
    (df_clean['Tech_Type'].apply(lambda x:200 if x == 'Smart' else 0))
)

# SOLO BUILD - loves high DPS, attacks speed, big mag size
df_clean['Solo_Score'] = (
    (df_clean['DPS'] * 1.0) +
    (df_clean['Attack_Speed'] * 50) +
    (df_clean['Magazine_Capacity'] * 5)
)

# TECHIE BUILD - loves tech weapons, armor penetration, raw damage
df_clean['Techie_Score'] = (
    (df_clean['Damage_Per_Hit'] * 3) +
    (df_clean['Armor_Penetration'] * 10) +
    (df_clean['Tech_Type'].apply(lambda x:300 if x == 'Tech' else 0))
)

# TANK BUILD - loves raw damage and burst DPS, less concerned with other things
df_clean['Tank_Score'] = (
    (df_clean['Damage_Per_Hit'] * 5) + 
    (df_clean['DPS'] * 0.3)
)

# STEALTH BUILD - loves headshot multiplier and handling
df_clean['Stealth_Score'] = (
    (df_clean['Headshot_Multiplier'] * 5) +
    (df_clean['Weapon_Handling'] * 50)
)

print("Build scores calculated!")
print("\nLet's find the best weapon for each build of V...")

# shot top 3 weapons for each build
print("NETRUNNER BUILD - Top 3 Weapons:")
print(df_clean.nlargest(3, 'Netrunner_Score')[['Weapon_Name', 'Category', 'Tech_Type', 'Netrunner_Score']])

print("SOLO BUILD - Top 3 Weapons:")
print(df_clean.nlargest(3, 'Solo_Score')[['Weapon_Name', 'Category', 'DPS', 'Solo_Score']])

print("TECHIE BUILD - Top 3 Weapons:")
print(df_clean.nlargest(3, 'Techie_Score')[['Weapon_Name', 'Category', 'Tech_Type', 'Techie_Score']])

print("TANK BUILD - Top 3 Weapons:")
print(df_clean.nlargest(3, 'Tank_Score')[['Weapon_Name', 'Category', 'Damage_Per_Hit', 'Tank_Score']])

print("STEALTH BUILD - Top 3 Weapons:")
print(df_clean.nlargest(3, 'Stealth_Score')[['Weapon_Name', 'Category', 'Headshot_Multiplier', 'Stealth_Score']])

