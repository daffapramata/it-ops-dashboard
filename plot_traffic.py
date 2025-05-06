import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV file
df = pd.read_csv('user_traffic.csv')

# Convert the 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set the style for the plots
sns.set_theme(style="whitegrid")

# 1. Line chart of traffic over time
plt.figure(figsize=(14, 5))
sns.lineplot(x='timestamp', y='hits', data=df)
plt.title('Hourly User Traffic Over the Last 7 Days')
plt.xlabel('Time')
plt.ylabel('Hits')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Aggregate: total hits per day
df['date'] = df['timestamp'].dt.date
daily_hits = df.groupby('date')['hits'].sum().reset_index()

# Bar chart of daily traffic
plt.figure(figsize=(10, 4))
sns.barplot(x='date', y='hits', data=daily_hits, palette='Blues_d')
plt.title('Total Daily User Traffic')
plt.xlabel('Date')
plt.ylabel('Total Hits')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()