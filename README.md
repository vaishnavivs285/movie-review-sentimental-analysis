# 🎬 Bollywood Movie Review Sentiment Analysis(WEB SCRAPING)

## 📌 Project Overview

This project builds a complete end-to-end Data Science pipeline to
analyze audience sentiment from Bollywood movie reviews scraped from
IMDb.

The objective is to understand how audience sentiment varies across
genres and to build machine learning models that can predict review
sentiment from text data.

------------------------------------------------------------------------

## 🚀 Project Workflow

### 1️⃣ Data Collection

-   Scraped 500 Bollywood movie reviews using Selenium automation.
-   Implemented dynamic "Load More" handling to extract multiple reviews
    per movie.
-   Built a structured dataset containing:
    -   Movie
    -   Genre
    -   Review Text
    -   Sentiment Label

### 2️⃣ Sentiment Labeling

-   Used VADER (rule-based NLP model) to classify reviews as Positive,
    Negative, or Neutral.

### 3️⃣ Exploratory Data Analysis (EDA)

-   Identified dataset imbalance (majority Positive reviews).
-   Analyzed genre-wise sentiment trends.
-   Found Drama received highest positive sentiment.
-   Observed Action genre had relatively more negative reviews.
-   Studied review length distribution.

### 4️⃣ Text Preprocessing

-   Lowercasing
-   Removing punctuation
-   Stopword removal
-   Lemmatization

### 5️⃣ Feature Engineering

-   Converted text into numerical format using TF-IDF vectorization.

### 6️⃣ Model Building

Trained and compared two models: - Logistic Regression - Naive Bayes

Used stratified train-test split due to class imbalance.

------------------------------------------------------------------------

## 🤖 Why Logistic Regression and Naive Bayes?

### Logistic Regression

-   Performs very well on high-dimensional sparse text data.
-   Does not assume feature independence.
-   Handles correlated TF-IDF features effectively.
-   Supports class balancing.
-   Strong and reliable baseline for NLP classification.

### Naive Bayes

-   Classic algorithm for text classification.
-   Very fast and computationally efficient.
-   Works well with word frequency features.
-   Provides a strong baseline comparison.

Logistic Regression outperformed Naive Bayes because real-world text
features are correlated, and Naive Bayes assumes independence between
words.

------------------------------------------------------------------------

## 📊 Model Performance

  Model                 Accuracy
  --------------------- ----------
  Logistic Regression   \~84%
  Naive Bayes           \~77%

Logistic Regression demonstrated better overall predictive performance.

------------------------------------------------------------------------

## 🔍 Other Models That Can Be Added

-   Support Vector Machine (SVM)
-   Random Forest
-   XGBoost
-   Gradient Boosting
-   LSTM (Deep Learning)
-   BERT / Transformer-based models

These advanced models may improve performance, especially for complex
contextual understanding.

------------------------------------------------------------------------

## ⚠ Problems Faced and How They Were Resolved

### 1️⃣ Dynamic Website Scraping

Problem: IMDb loads reviews dynamically. Solution: Implemented Selenium
automation with "Load More" handling.

### 2️⃣ Dataset Imbalance

Problem: Majority of reviews were Positive. Solution: Used stratified
train-test split and class_weight='balanced' in Logistic Regression.

### 3️⃣ Text Noise

Problem: Reviews contained punctuation, symbols, and stopwords.
Solution: Applied NLP preprocessing and cleaning techniques.

### 4️⃣ Rare Neutral Class

Problem: Very few Neutral samples caused low prediction for that class.
Solution: Focused evaluation on F1-score and class-based metrics rather
than only accuracy.

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python
-   Selenium
-   NLTK
-   Scikit-learn
-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn

------------------------------------------------------------------------

## 🏁 Conclusion

This project demonstrates a complete Data Science workflow from web
scraping to NLP preprocessing and machine learning modeling.

It shows how unstructured text data can be transformed into meaningful
insights and predictive models.
