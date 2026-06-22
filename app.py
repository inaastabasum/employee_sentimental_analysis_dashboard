import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from employee_sentimental_analysis import get_dashboard_data

# =====================================
# LOAD DATA
# =====================================

data = get_dashboard_data()

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Employee Sentiment Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #334155
    );
}

h1,h2,h3 {
    color:white !important;
}

p, label {
    color:white !important;
}

[data-testid="stMetricValue"]{
    color:#22c55e;
}

[data-testid="stMetricLabel"]{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================

st.title("📊 Employee Sentiment Analysis & HR Insights Dashboard")

st.write(
    "Analyze employee reviews, workplace satisfaction, complaint themes, and HR analytics insights."
)

st.divider()

# =====================================
# KPI CARDS
# =====================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Total Reviews",
        f"{data['total_reviews']:,}"
    )

with c2:
    st.metric(
        "Positive %",
        f"{data['positive_reviews']}%"
    )

with c3:
    st.metric(
        "Neutral %",
        f"{data['neutral_reviews']}%"
    )

with c4:
    st.metric(
        "Negative %",
        f"{data['negative_reviews']}%"
    )

st.divider()

# =====================================
# NEGATIVE REVIEW CHART
# =====================================

st.header("📉 Negative Review Percentage by Company")

fig1, ax1 = plt.subplots(figsize=(8,4))

data["negative_rate"].plot(
    kind="bar",
    ax=ax1
)

ax1.set_ylabel("Percentage")
ax1.set_title("Negative Review Percentage by Company")

st.pyplot(fig1)

# =====================================
# COMPANY RATINGS TABLE
# =====================================

st.header("🏆 Company Ratings Comparison")

st.dataframe(
    data["company_ratings"],
    use_container_width=True
)

# =====================================
# COMPANY SELECTOR
# =====================================

st.header("🏢 Company Analysis")

companies = list(data["company_ratings"].index)

selected_company = st.selectbox(
    "Select Company",
    companies
)

st.subheader(f"Ratings for {selected_company.title()}")

company_data = data["company_ratings"].loc[selected_company]

fig2, ax2 = plt.subplots(figsize=(8,4))

company_data.plot(
    kind="bar",
    ax=ax2
)

ax2.set_ylabel("Rating")
ax2.set_title(
    f"{selected_company.title()} Employee Ratings"
)

st.pyplot(fig2)

# =====================================
# COMPLAINT THEMES
# =====================================

st.header("⚠️ Top Employee Complaint Themes")

complaints_df = pd.DataFrame(
    data["top_complaints"],
    columns=["Keyword", "Frequency"]
)

st.dataframe(
    complaints_df,
    use_container_width=True
)

# =====================================
# CORRELATION ANALYSIS
# =====================================

st.header("📈 Factors Influencing Employee Satisfaction")

corr_df = pd.DataFrame(
    data["correlation"]
)

st.dataframe(
    corr_df,
    use_container_width=True
)

fig3, ax3 = plt.subplots(figsize=(8,4))

data["correlation"].drop(
    "overall-ratings"
).plot(
    kind="bar",
    ax=ax3
)

ax3.set_title(
    "Drivers of Employee Satisfaction"
)

ax3.set_ylabel(
    "Correlation"
)

st.pyplot(fig3)

# =====================================
# KEY INSIGHTS
# =====================================

st.header("🔍 Key Insights")

st.success(
    "Culture & Values has the strongest impact on overall employee satisfaction."
)

st.success(
    "Senior Management quality is strongly associated with employee ratings."
)

st.success(
    "Work-Life Balance remains one of the most common complaint areas."
)

st.success(
    "Amazon shows the highest negative review percentage in the dataset."
)

# =====================================
# HR RECOMMENDATIONS
# =====================================

st.header("💡 HR Recommendations")

st.info(
    "Improve leadership and management training programs."
)

st.info(
    "Reduce excessive workload and long working hours."
)

st.info(
    "Strengthen organizational culture and employee engagement."
)

st.info(
    "Provide clearer career growth opportunities."
)

st.info(
    "Monitor employee sentiment continuously through review analytics."
)

# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "Built using Python, Pandas, TextBlob, Matplotlib and Streamlit."
)