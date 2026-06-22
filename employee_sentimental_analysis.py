import pandas as pd
from textblob import TextBlob
from collections import Counter
import matplotlib.pyplot as plt
import re

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("employee_reviews.csv")

# ==========================
# Create Review Text
# ==========================

df["review_text"] = (
    df["summary"].fillna("") + " " +
    df["pros"].fillna("") + " " +
    df["cons"].fillna("") + " " +
    df["advice-to-mgmt"].fillna("")
)

# ==========================
# Sentiment Analysis
# ==========================

df["sentiment_score"] = df["review_text"].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity
)

def get_sentiment(score):
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    else:
        return "Neutral"

df["sentiment"] = df["sentiment_score"].apply(get_sentiment)

# ==========================
# Complaint Analysis
# ==========================

negative_text = " ".join(
    df[df["sentiment"] == "Negative"]["cons"].astype(str)
)

words = re.findall(r"\b[a-zA-Z]+\b", negative_text.lower())

stop_words = {
    "the", "and", "to", "of", "a", "is", "in",
    "for", "on", "with", "that", "are", "be",
    "you", "it", "have", "has", "this", "at",
    "an", "as", "not", "but", "can", "will",
    "they", "your", "very", "about", "there",
    "like", "company", "people"
}

filtered_words = [
    word for word in words
    if word not in stop_words and len(word) > 3
]

word_counts = Counter(filtered_words)

# ==========================
# Negative Review Percentage
# ==========================

total_reviews = df.groupby("company").size()

negative_reviews = (
    df[df["sentiment"] == "Negative"]
    .groupby("company")
    .size()
)

negative_rate = (
    (negative_reviews / total_reviews) * 100
).sort_values(ascending=False)

# ==========================
# Company Ratings Analysis
# ==========================

rating_cols = [
    "overall-ratings",
    "work-balance-stars",
    "culture-values-stars",
    "carrer-opportunities-stars",
    "comp-benefit-stars",
    "senior-mangemnet-stars"
]

for col in rating_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

company_ratings = (
    df.groupby("company")[rating_cols]
    .mean()
    .round(2)
)

# ==========================
# Correlation Analysis
# ==========================

correlation = df[rating_cols].corr()

# ==========================
# Dashboard Function
# ==========================

def get_dashboard_data():
    return {
        "df": df,

        "total_reviews": len(df),

        "positive_reviews":
        round((df["sentiment"] == "Positive").mean() * 100, 1),

        "neutral_reviews":
        round((df["sentiment"] == "Neutral").mean() * 100, 1),

        "negative_reviews":
        round((df["sentiment"] == "Negative").mean() * 100, 1),

        "negative_rate": negative_rate,

        "company_ratings": company_ratings,

        "top_complaints": word_counts.most_common(10),

        "correlation":
        correlation["overall-ratings"]
        .sort_values(ascending=False)
    }
# ==========================
# Run Only When Executed Directly
# ==========================

if __name__ == "__main__":

    print("Dataset Shape:", df.shape)

    print("\nSentiment Distribution")
    print(df["sentiment"].value_counts())

    print("\nTop Complaint Keywords")
    print(word_counts.most_common(20))

    print("\nNegative Review Percentage")
    print(negative_rate)

    print("\nAverage Ratings by Company")
    print(company_ratings)

    print("\nCorrelation with Overall Rating")
    print(
        correlation["overall-ratings"]
        .sort_values(ascending=False)
    )

    # Chart 1
    negative_rate.plot(kind="bar")
    plt.title("Negative Review Percentage by Company")
    plt.ylabel("Percentage")
    plt.tight_layout()
    plt.show()

    # Chart 2
    company_ratings["work-balance-stars"].sort_values().plot(
        kind="bar",
        title="Work-Life Balance by Company"
    )
    plt.ylabel("Rating")
    plt.tight_layout()
    plt.show()

    # Chart 3
    company_ratings["overall-ratings"].sort_values().plot(
        kind="bar",
        title="Overall Employee Rating by Company"
    )
    plt.ylabel("Rating")
    plt.tight_layout()
    plt.show()
    