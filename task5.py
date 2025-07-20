# STEP 1: Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# STEP 2: Locate the file inside the Kaggle input directory
folder_path = '/kaggle/input/us-accidents'
files = os.listdir(folder_path)
print("📁 Files found:", files)

# STEP 3: Load the dataset using the correct file name
csv_file = [f for f in files if f.endswith('.csv')][0]  # take the first CSV file
file_path = os.path.join(folder_path, csv_file)
print("✅ Loading file:", file_path)

df = pd.read_csv(file_path, low_memory=False)

# STEP 4: Parse datetime and extract hour and weekday
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df['Hour'] = df['Start_Time'].dt.hour
df['Weekday'] = df['Start_Time'].dt.day_name()

# STEP 5: Plot accidents by hour
plt.figure(figsize=(12,6))
sns.countplot(x='Hour', data=df, palette='viridis')
plt.title("Accidents by Hour of the Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()

# STEP 6: Plot accidents by weekday
plt.figure(figsize=(12,6))
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(x='Weekday', data=df, order=weekday_order, palette='magma')
plt.title("Accidents by Day of the Week")
plt.xlabel("Weekday")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()