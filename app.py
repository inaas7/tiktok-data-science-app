import streamlit as st
import pandas as pd
from subprocess import call # to run tiktok script from command line
import plotly.express as px

# Set page width to wide
st.set_page_config(layout='wide')

# Input
hashtag = st.text_input('Search for a hashtag here', value="")

# Sidebar
st.sidebar.markdown("<div><img src='https://www.freepnglogos.com/uploads/tik-tok-logo-png/tik-tok-android-application-logos-3.png' width='120' alt = 'TikTok logo'/><h1 style='display:inline-block'>TikTok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This dashboard allows you to analyse trending 📈 tiktoks using Python and Streamlit.")
st.sidebar.markdown("To get started <ol><li>Enter the <i>hashtag</i> you wish to analyse</li> <li>Hit <i>Get Data</i>.</li> <li>Get analyzing</li></ol>",unsafe_allow_html=True)

# Button
if st.button('Get Data'):
    # Run get data function
    st.write(hashtag)
    call(['python', 'tiktok.py', hashtag])
    # Load data
    df = pd.read_csv('tiktokdata.csv')

    # Plotly visualization here
    fig = px.histogram(df, x='desc', hover_data=['desc'], y='stats_diggCount', height=300) 
    st.plotly_chart(fig, use_container_width=True)

    # Split columns
    left_col, right_col = st.columns(2)

    # First Chart - video stats
    scatter1 = px.scatter(df, x='stats_shareCount', y='stats_commentCount', hover_data=['desc'], size='stats_playCount', color='stats_playCount')
    left_col.plotly_chart(scatter1, use_container_width=True)

    # Second Chart
    scatter2 = px.scatter(df, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=['author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount')
    right_col.plotly_chart(scatter2, use_container_width=True)

    # Show tabular dataframe in streamlit
    df