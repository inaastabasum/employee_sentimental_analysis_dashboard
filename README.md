# Employee Sentiment Analysis Dashboard

## Overview

This project analyzes employee reviews from major technology companies and provides HR insights using Natural Language Processing (NLP) and Data Visualization.

The dashboard helps identify:

- Employee sentiment
- Workplace satisfaction drivers
- Common complaint themes
- Company rating comparisons
- HR recommendations

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

Total Reviews: 67,529

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

## Project Structure

employee_sentimental_analysis.py
app.py
employee_reviews.csv
README.md

## Run Locally

Install dependencies:

```bash
pip install pandas textblob matplotlib streamlit
```

Run dashboard:

```bash
streamlit run app.py
```

## Author

Data Science Student | HR Analytics Internship Project
