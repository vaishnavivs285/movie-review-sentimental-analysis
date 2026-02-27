import pandas as pd
import time
import nltk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# 1. SETUP
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

def get_driver():
    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    opts.add_argument("--blink-settings=imagesEnabled=false") 
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

# 2. THE ENGINE
def scrape_movie(movie, target_count=50):
    name, url, genre = movie['name'], movie['url'], movie['genre']
    print(f"🔍 Scraping {name}...")
    
    driver = get_driver()
    data = []
    
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        
        # --- LOAD MORE LOOP ---
        current_count = 0
        while current_count < target_count:
            try:
                load_more = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ipc-see-more__button")))
                driver.execute_script("arguments[0].click();", load_more)
                time.sleep(2) 
                current_elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='review-overflow']")
                current_count = len(current_elements)
                if current_count >= target_count: break
            except:
                break 

        # --- PROCESSING (Targeting Movie, Genre, Review, Sentiment) ---
        containers = driver.find_elements(By.CSS_SELECTOR, "[data-testid='review-overflow']")
        for container in containers[:target_count]:
            review_text = container.text.strip()
            if len(review_text) > 30:
                # NLP Analysis for Sentiment Label
                score = sia.polarity_scores(review_text)['compound']
                sentiment_label = "Positive" if score >= 0.05 else "Negative" if score <= -0.05 else "Neutral"
                
                # Appending only the requested columns
                data.append({
                    "Movie": name,
                    "Genre": genre,
                    "Review": review_text.replace('\n', ' '), # Keep review on one line
                    "Sentiment": sentiment_label
                })
        print(f"   [+] Successfully collected {len(data)} reviews.")
    except Exception as e:
        print(f"   [!] Error on {name}: {e}")
    finally:
        driver.quit()
    return data

# 3. CONFIG
movies_to_scrape = [
    {"genre": "Action", "name": "Dhurandhar", "url": "https://www.imdb.com/title/tt33014583/reviews/"},
    {"genre": "Action", "name": "Sikandar", "url": "https://www.imdb.com/title/tt31712434/reviews/"},
    {"genre": "Action", "name": "Kill", "url": "https://www.imdb.com/title/tt28259207/reviews/"},
    {"genre": "Horror-Comedy", "name": "Stree 2", "url": "https://www.imdb.com/title/tt27510174/reviews/"},
    {"genre": "Horror-Comedy", "name": "Munjya", "url": "https://www.imdb.com/title/tt27995594/reviews/"},
    {"genre": "Horror-Comedy", "name": "Thamma", "url": "https://www.imdb.com/title/tt28102562/reviews/"},
    {"genre": "Drama", "name": "Saiyaara", "url": "https://www.imdb.com/title/tt28037987/reviews/"},
    {"genre": "Drama", "name": "Laapataa Ladies", "url": "https://www.imdb.com/title/tt21626284/reviews/"},
    {"genre": "Thriller", "name": "Deva", "url": "https://www.imdb.com/title/tt27852049/reviews/"},
    {"genre": "Thriller", "name": "Raid 2", "url": "https://www.imdb.com/title/tt28089700/reviews/"}
]

# 4. RUN
if __name__ == "__main__":
    all_data = []
    for movie in movies_to_scrape:
        all_data.extend(scrape_movie(movie, target_count=50))

    if all_data:
        df = pd.DataFrame(all_data)
        # Exporting to CSV with requested columns
        df.to_csv("bollywood_reviews_dataset.csv", index=False)
        print(f"\n✅ SUCCESS! CSV created with {len(df)} reviews.")
        print(df.head()) # Preview the table