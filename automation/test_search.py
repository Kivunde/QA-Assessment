from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def test_search_functionality():
    try:
        # Navigate to the photo/album listing page
        driver.get("https://jsonplaceholder.typicode.com/photos")

        # Find the search box and enter a search term
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("nature")
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load
        time.sleep(2)

        # Validate that the correct results appear
        results = driver.find_elements(By.CLASS_NAME, "photo-item")
        assert len(results) > 0, "No results found for the search term."

        print("Search functionality test passed!")
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_search_functionality()