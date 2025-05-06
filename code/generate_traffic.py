import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Generate a list of hourly timestamps over the last 7 days
start_time = datetime.now() - timedelta(days=7)
end_time = datetime.now()
timestamps = pd.date_range(start=start_time, end=end_time, freq='H')

# 2. Simulate random user traffic for each hour
traffic = [random.randint(50, 500) for _ in range(len(timestamps))]

# 3. Create a DataFrame to hold the data
df = pd.DataFrame({
    'timestamp': timestamps,
    'hits': traffic
})

# 4. Show the first few rows of the DataFrame
print(df.head())

# 5. Optional: Save to CSV for later use
df.to_csv('user_traffic.csv', index=False)