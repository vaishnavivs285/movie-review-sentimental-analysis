import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# --- STEP 1: SETUP THE  (BROWSER) ---
def get_driver():
    opts = Options()
    opts.add_argument('--headless') # Runs in background without opening a window
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36") # Pretends to be a human user
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
# step 2 
def scrape_imdb(movie, target_reviews=30):
    driver = get_driver()
    data = []
    print(f"🔍 {movie['name']}...")

    try:
        driver.get(movie['url'])
        time.sleep(2) # Thoda sa wait

        # Load More: Sirf 1 baar click (approx 50 reviews mil jayenge)
        try:
            btn = driver.find_element(By.CSS_SELECTOR, "button.ipc-see-more__button")
            btn.click() 
            time.sleep(2)
        except: pass

        # Short extraction logic
        revs = driver.find_elements(By.CSS_SELECTOR, "[data-testid='review-overflow']")
        for r in revs[:target_reviews]:
            txt = r.text.strip().replace('\n', ' ')
            if len(txt) > 30:
                data.append({"Movie": movie['name'], "Genre": movie['genre'], "Review": txt})

    except Exception as e: print(f"❌ Error: {e}")
    finally: driver.quit()
    
    return data

# --- STEP 3: THE 25-27 MOVIE LIST (2024-2026) ---
movies_list = [
    # --- ACTION ---
    {"genre": "Action", "name": "Dhurandhar", "url": "https://www.imdb.com/title/tt33014583/reviews/"},
    {"genre": "Action", "name": "Sikandar", "url": "https://www.imdb.com/title/tt31712434/reviews/"},
    {"genre": "Action", "name": "Kill", "url": "https://www.imdb.com/title/tt28259207/reviews/"},
    {"genre": "Action", "name": "Deva", "url": "https://www.imdb.com/title/tt27852049/reviews/"},
    {"genre": "Action", "name": "War 2", "url": "https://www.imdb.com/title/tt27425164/reviews/"},
    {"genre": "Action", "name": "Fighter", "url": "https://www.imdb.com/title/tt13818368/reviews/"},
    
    # --- HORROR-COMEDY ---
    {"genre": "Horror-Comedy", "name": "Stree 2", "url": "https://www.imdb.com/title/tt27510174/reviews/"},
    {"genre": "Horror-Comedy", "name": "Munjya", "url": "https://www.imdb.com/title/tt27995594/reviews/"},
    {"genre": "Horror-Comedy", "name": "Bhool Bhulaiyaa 3", "url": "https://www.imdb.com/title/tt26932223/reviews/"},
    {"genre": "Horror-Comedy", "name": "Bhediya", "url": "https://www.imdb.com/title/tt14099334/reviews/"},
    {"genre": "Horror-Comedy", "name": "Thamma", "url": "https://www.imdb.com/title/tt28102562/reviews/"},
    {"genre": "Horror-Comedy", "name": "Roohi", "url": "https://www.imdb.com/title/tt10098288/reviews/"},

    # --- DRAMA / REAL-LIFE ---
    {"genre": "Drama", "name": "12th Fail", "url": "https://www.imdb.com/title/tt23849204/reviews/"},
    {"genre": "Drama", "name": "Laapataa Ladies", "url": "https://www.imdb.com/title/tt21626284/reviews/"},
    {"genre": "Drama", "name": "Saiyaara", "url": "https://www.imdb.com/title/tt28037987/reviews/"},
    {"genre": "Drama", "name": "Dunki", "url": "https://www.imdb.com/title/tt15428134/reviews/"},
    {"genre": "Drama", "name": "Animal", "url": "https://www.imdb.com/title/tt13751694/reviews/"},
    {"genre": "Drama", "name": "Chhava", "url": "https://www.imdb.com/title/tt27922706/reviews/"},

    # --- THRILLER / MYSTERY ---
    {"genre": "Thriller", "name": "Drishyam 2", "url": "https://www.imdb.com/title/tt15501640/reviews/"},
    {"genre": "Thriller", "name": "Raid 2", "url": "https://www.imdb.com/title/tt28089700/reviews/"},
    {"genre": "Thriller", "name": "Sector 36", "url": "https://www.imdb.com/title/tt21626774/reviews/"},
    {"genre": "Thriller", "name": "Merry Christmas", "url": "https://www.imdb.com/title/tt15392282/reviews/"},
    {"genre": "Thriller", "name": "Jigra", "url": "https://www.imdb.com/title/tt26733317/reviews/"},

    # --- SCI-FI / FANTASY ---
    {"genre": "Sci-Fi", "name": "Kalki 2898 AD", "url": "https://www.imdb.com/title/tt12735488/reviews/"},
    {"genre": "Sci-Fi", "name": "Brahmastra", "url": "https://www.imdb.com/title/tt6277462/reviews/"},
    {"genre": "Sci-Fi", "name": "2.0", "url": "https://www.imdb.com/title/tt5080556/reviews/"},
    {"genre": "Sci-Fi", "name": "Rocketry", "url": "https://www.imdb.com/title/tt9263550/reviews/"}


]

# --- STEP 4: EXECUTION ---
if __name__ == "__main__":
    final_dataset = []
    
    for m in movies_list:
        results = scrape_imdb(m, target_reviews=30)
        final_dataset.extend(results)
    
    # Save the results to CSV
    df = pd.DataFrame(final_dataset)
    df.to_csv("bolly_reviews_2026.csv", index=False)
    
    print("\n✅ DONE! Your dataset is ready in 'bolly_reviews_2026.csv'")
        