import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="COVID-19 Tracker", layout="wide")
st.title("🦠 COVID-19 Global Data Tracker")
st.markdown("Get real-time COVID-19 stats by country. Powered by [disease.sh](https://disease.sh/)")

# Get global data
global_data = requests.get("https://disease.sh/v3/covid-19/all").json()
st.markdown(f"🌐 **Global Cases**: {global_data['cases']:,} | **Deaths**: {global_data['deaths']:,} | **Recovered**: {global_data['recovered']:,}")

# Get countries list
countries_data = requests.get("https://disease.sh/v3/covid-19/countries").json()
country_list = sorted([c['country'] for c in countries_data])
country = st.selectbox("Select a Country", country_list)

# Fetch selected country data
url = f"https://disease.sh/v3/covid-19/countries/{country}"
data = requests.get(url).json()

st.subheader(f" COVID-19 Stats for {country}")
col1, col2, col3 = st.columns(3)
col1.metric("Total Cases", f"{data['cases']:,}")
col2.metric("Recovered", f"{data['recovered']:,}")
col3.metric("Deaths", f"{data['deaths']:,}")

# Pie chart breakdown (Active, Recovered, Deaths)
st.subheader("📊 Case Distribution")
chart_data = pd.Series({
    'Active': data['active'],
    'Recovered': data['recovered'],
    'Deaths': data['deaths']
})
st.bar_chart(chart_data)

# Line chart of past 30 days
history_url = f"https://disease.sh/v3/covid-19/historical/{country}?lastdays=30"
history_data = requests.get(history_url).json()

if 'timeline' in history_data:
    cases = history_data['timeline']['cases']
    dates = list(cases.keys())
    values = list(cases.values())
    st.subheader(f"📈 COVID-19 Cases Over Last 30 Days in {country}")
    st.line_chart(pd.Series(values, index=pd.to_datetime(dates)))
else:
    st.warning("No historical data available for this country.")
