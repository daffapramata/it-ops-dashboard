import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config('IT Traffic Dashboard', page_icon='🌐', layout='wide')

# Load the data from CSV file
df = pd.read_csv('user_traffic.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['date'] = df['timestamp'].dt.date

# Sidebar - Date filter
st.sidebar.image('img/DLogo-removebg.png',width=150)
st.sidebar.title('⚙️ Dashboard Filters')


start_date = st.sidebar.date_input('Start date', df['date'].min())
end_date = st.sidebar.date_input('End date', df['date'].max())

# Filter the data
mask = (df['date'] >= start_date) & (df['date'] <= end_date)
filtered_df = df.loc[mask]

# Traffic Metrics
total_hits = filtered_df['hits'].sum()
average_hits = filtered_df['hits'].mean()

# Layout columns
col1, col2 = st.columns(2)
with col1:
    st.metric('📈 Total Hits', f'{total_hits:,} hits')
with col2:
    st.metric('📊 Average Hits', f'{average_hits:.2f} hits/hour')

# Traffic Alerts
st.subheader('## 🚨 Traffic Alert')

# Define thresholds for alerts
HIGH_TRAFFIC_THRESHOLD = 450
LOW_TRAFFIC_THRESHOLD = 100

# Check conditions
high_traffic_hours = filtered_df[filtered_df['hits'] > HIGH_TRAFFIC_THRESHOLD]
low_traffic_hours = filtered_df[filtered_df['hits'] < LOW_TRAFFIC_THRESHOLD]

if not high_traffic_hours.empty:
    st.warning(f'⚡ High traffic detected on {len(high_traffic_hours)} hour(s) above {HIGH_TRAFFIC_THRESHOLD} hits!')
else:
    st.success('✅ No high traffic detected.')

if not low_traffic_hours.empty:
    st.error(f'🔻 Low traffic detected on {len(low_traffic_hours)} hour(s) below {LOW_TRAFFIC_THRESHOLD} hits!')
else:
    st.success('✅ No low traffic detected.')

# Charts Section
st.markdown('## 📊 Traffic Charts')

# Line chart - hourly traffic
st.subheader('Hourly Traffic Over Time')
fig, ax = plt.subplots(figsize=(14, 5))
sns.lineplot(data=filtered_df, x='timestamp', y='hits', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Daily totals
st.subheader('Daily Total Hits')
daily_hits = filtered_df.groupby('date')['hits'].sum().reset_index()

fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.barplot(data=daily_hits, x='date', y='hits', palette='Blues_d', ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# Footer
st.markdown('---')
st.caption('Made by Daffa | IT Ops Dashboard - Apr 2025')