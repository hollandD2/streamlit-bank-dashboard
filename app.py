import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('bank01.csv')

# Data cleaning steps
# Convert columns to numeric where needed
df['demog_homeval'] = pd.to_numeric(df['demog_homeval'], errors='coerce')
df['rfm1'] = pd.to_numeric(df['rfm1'], errors='coerce')
df['demog_age'] = df['demog_age'].fillna(df['demog_age'].median())
df['rfm3'] = df['rfm3'].fillna(df['rfm3'].median())
df = df.dropna()

# Streamlit app
st.title("📊 Bank Campaign Response Dashboard")
st.markdown("""
This dashboard explores factors influencing whether a customer responded to a campaign, focusing on income, homeownership, and customer behavior.
""")

# Sidebar filter
ho_filter = st.sidebar.selectbox("Filter by Homeownership:", options=['All', 'yes', 'no'])

if ho_filter != 'All':
    df = df[df['demog_ho'] == ho_filter]

# Visualization 1: Histogram of Income
st.subheader("Income Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(df['demog_inc'], bins=50, kde=True, ax=ax1)
st.pyplot(fig1)

# Visualization 2: Income vs Campaign Response
st.subheader("Income by Campaign Response")
fig2, ax2 = plt.subplots()
sns.boxplot(x='int_tgt', y='demog_inc', data=df, ax=ax2)
ax2.set_xlabel("Responded (0 = No, 1 = Yes)")
st.pyplot(fig2)

# Visualization 3: Response by Homeownership
st.subheader("Response Count by Homeownership")
fig3, ax3 = plt.subplots()
sns.countplot(x='demog_ho', hue='int_tgt', data=df, ax=ax3)
ax3.set_xlabel("Homeownership")
ax3.legend(title="Responded")
st.pyplot(fig3)

# Footer summary
st.markdown("""
### Key Insights:
- Responders tend to have slightly higher income.
- Homeowners show a higher response rate.

**Hypothesis:** Customers with higher income and homeownership are more likely to respond.
""")
