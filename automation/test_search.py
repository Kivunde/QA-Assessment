from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the web application
    driver.get("https://your-app.com/albums")

    # Wait for the page to load
    time.sleep(2)

    # Locate the search box and enter a search term
    search_box = driver.find_element(By.NAME, "search") 
    search_term = "omnis"
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to appear
    time.sleep(2)

    # Validate that correct results appear
    results = driver.find_elements(By.CLASS_NAME, "omnis")  # Modify as per actual class name
    assert any(search_term in result.text for result in results), "Search results do not match query"

    print("Test Passed: Correct search results displayed.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    # Close the browser
    driver.quit()
