# 🎬 Bollywood Movie Reviews Sentiment Analysis (2024--2026)

## 📌 Project Overview

This project focuses on scraping IMDb reviews of recent Bollywood movies
(2024--2026) and performing Sentiment Analysis using Machine Learning
and NLP techniques.

It demonstrates a complete end-to-end Data Science workflow: Web
Scraping → Data Cleaning → NLP → Modeling → Evaluation → Insights

------------------------------------------------------------------------

# 🎯 Why This Project Was Built

-   To apply real-world web scraping using Selenium
-   To implement Natural Language Processing (NLP)
-   To compare baseline ML models for text classification
-   To simulate an industry-level sentiment analysis pipeline

------------------------------------------------------------------------

# 🌐 Web Scraping Methodology

### Tools Used:

-   Selenium
-   Chrome WebDriver
-   webdriver_manager
-   Headless browser mode
-   Custom User-Agent

### Scraping Workflow:

1.  A headless Chrome browser was launched.
2.  IMDb movie review pages were accessed dynamically.
3.  "Load More" button was clicked once to fetch additional reviews.
4.  Reviews were extracted using CSS selectors.
5.  Reviews shorter than 30 characters were filtered out.
6.  Extracted fields:
    -   Movie Name
    -   Genre
    -   Review Text
7.  Final dataset saved as: bolly_reviews_2026.csv

------------------------------------------------------------------------

# 🎥 Movies Covered

Movies were selected across 5 major genres:

-   Action
-   Horror--Comedy
-   Drama / Real-Life
-   Thriller / Mystery
-   Sci-Fi / Fantasy

Selection Criteria: - Recent (2024--2026 releases) - High public
visibility - Adequate IMDb review volume - Multi-genre representation to
reduce bias

------------------------------------------------------------------------

# ⚠ Challenges Faced During Scraping

### 1. Dynamic Content Loading

IMDb loads reviews dynamically via JavaScript.

Solution: Used Selenium instead of static scraping tools.

### 2. Bot Detection Risk

Websites may block automated traffic.

Solution: - Used headless mode carefully - Added custom user-agent -
Limited number of reviews per movie

### 3. Inconsistent Review Length

Some reviews were too short.

Solution: Filtered reviews below 30 characters.

### 4. Load More Button Not Always Present

Solution: Handled using try-except blocks to avoid crashes.

------------------------------------------------------------------------

# 📊 Notebook Workflow (Step-by-Step)

## 1. Data Loading

-   Loaded CSV dataset
-   Checked shape and missing values

## 2. Data Cleaning

-   Removed duplicates
-   Converted text to lowercase
-   Removed punctuation and noise

## 3. NLP Processing

Yes, NLP was used.

### Why NLP?

Machine learning models cannot process raw text directly. Text must be
converted into numerical form.

Steps: - Tokenization - Stopword removal - Text normalization - TF-IDF
Vectorization

TF-IDF converts text into numerical feature vectors.

------------------------------------------------------------------------

## 4. Train-Test Split

Used 80% training and 20% testing.

Reason: - Sufficient data for model learning - Reliable evaluation on
unseen data

------------------------------------------------------------------------

# 🤖 Models Used

1.  Logistic Regression
2.  Naive Bayes

### Why These Models?

-   Strong baseline models for NLP
-   Perform well with TF-IDF features
-   Fast and computationally efficient
-   Easy to interpret

------------------------------------------------------------------------

# 📈 Evaluation Metrics

-   Accuracy
-   Precision
-   Recall
-   F1-Score
-   ROC-AUC

We did not rely only on accuracy.

Why? If dataset is imbalanced, accuracy can be misleading.

Recall and F1-score help measure real classification strength.

------------------------------------------------------------------------

# 🏆 Model Performance

Logistic Regression generally performed better due to: - Better decision
boundary handling - Robustness with balanced datasets

Naive Bayes: - Faster - Slightly less accurate in comparison

------------------------------------------------------------------------

# 👥 Who Benefits From This Project?

-   Movie Production Houses
-   Marketing Teams
-   OTT Platforms
-   Media Analysts

They can: - Understand audience sentiment - Detect negative feedback
trends - Compare genre performance - Improve marketing strategy

------------------------------------------------------------------------

# 🔮 Can Other Models Be Used?

Yes.

Possible Extensions: - Random Forest - XGBoost - Support Vector
Machine - LSTM (Deep Learning) - BERT (Transformer-based NLP)

Advanced models may improve performance but require more resources.

------------------------------------------------------------------------

# 🚀 Future Improvements

-   Increase number of reviews per movie
-   Perform aspect-based sentiment analysis
-   Use rating-based labeling
-   Deploy as a web application
-   Integrate real-time APIs

------------------------------------------------------------------------

# 🧠 Key Learnings

-   Handling dynamic websites using Selenium
-   Managing scraping challenges safely
-   Building an NLP pipeline
-   Comparing ML models properly
-   Evaluating beyond just accuracy

------------------------------------------------------------------------

# 🏁 Conclusion

This project reflects a practical, industry-style sentiment analysis
pipeline built from scratch.

It demonstrates real-world data collection, NLP implementation, machine
learning modeling, and evaluation techniques.
