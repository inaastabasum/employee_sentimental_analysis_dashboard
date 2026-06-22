# Employee Sentiment Analysis Dashboard

## Overview

This project analyzes employee reviews from major technology companies and provides HR insights using Natural Language Processing (NLP) and Data Visualization.

The dashboard helps identify:

- Employee sentiment
- Workplace satisfaction drivers
- Common complaint themes
- Company rating comparisons
- HR recommendations

## Dashboard Preview

![Dashboard Screenshot](Dashboard_home.png)

## Technologies Used

- Python
- Pandas
- TextBlob
- Matplotlib
- Streamlit

## Dataset

Employee reviews dataset containing:

- Company
- Review Summary
- Pros
- Cons
- Advice to Management
- Employee Ratings

**Total Reviews:** 67,529

## Key Findings

### Sentiment Distribution

- Positive Reviews: 81.4%
- Neutral Reviews: 15.7%
- Negative Reviews: 2.9%

### Common Complaint Themes

- Work pressure
- Management issues
- Long working hours
- Work-life balance
- Organizational culture

### Strongest Satisfaction Drivers

- Culture & Values
- Senior Management
- Career Opportunities

## Dashboard Features

- Interactive KPI cards
- Company-wise comparison
- Sentiment analytics
- Complaint keyword analysis
- Correlation analysis
- HR recommendations
- Dynamic company selection

## Sample Insights

- Amazon has the highest negative review percentage in the dataset.
- Culture & Values is the strongest driver of employee satisfaction.
- Senior Management strongly influences employee ratings.
- Work-Life Balance remains a major employee concern.

## Project Structure

```text
employee_sentiment_analysis_dashboard/
│
├── app.py
├── employee_sentimental_analysis.py
├── employee_reviews.csv
├── requirements.txt
├── README.md
│
└── screenshots/
    └── dashboard.png
```

## Run Locally

Install dependencies:

```bash
pip install pandas textblob matplotlib streamlit
```

Or:

```bash
pip install -r requirements.txt
```

Run the analysis script:

```bash
python employee_sentimental_analysis.py
```

Run the dashboard:

```bash
streamlit run app.py
```

## Future Improvements

- Word Cloud Visualization
- Interactive Plotly Charts
- Sentiment Trend Analysis
- Department-Level Analytics
- Streamlit Cloud Deployment

## Author

**Inaas Tabasum**

HR Analytics & Employee Sentiment Analysis Project
```bash
streamlit run app.py
```

## Author

Data Science Student | HR Analytics Internship Project
