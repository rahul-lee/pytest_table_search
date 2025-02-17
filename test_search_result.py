from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")  # Headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--window-size=1920x1080")  # Ensure proper viewport size

# Initialize WebDriver with headless option
driver = webdriver.Chrome(options=chrome_options)

def test_search_functionality():
    try:
        driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)
        total_entries_text = wait.until(EC.presence_of_element_located((By.ID, "example_info"))).text
        total_entries = int(total_entries_text.split("of")[-1].split("entries")[0].strip())

        assert total_entries == 24, f"Expected total 24 entries before search, but found {total_entries}"

        search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
        search_box.send_keys("New York")

        # Wait for filtered results to appear
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#example tbody tr")) > 0)

        # Find table rows within tbody (filtered results)
        filtered_rows = driver.find_elements(By.CSS_SELECTOR, "#example tbody tr")
        filtered_count = len(filtered_rows)

        # Get updated total entries text after search
        updated_entries_text = driver.find_element(By.ID, "example_info").text
        updated_total_entries = int(updated_entries_text.split("of")[-1].split("entries")[0].strip())

        # Assert that filtered results show 5 entries
        assert filtered_count == 5, f"Expected 5 filtered entries, but found {filtered_count}"

        # Assert that the total number of displayed entries after search is 5
        assert updated_total_entries == 5, f"Expected total 5 entries after search, but found {updated_total_entries}"

        print("✅ Test Passed: Search results show 5 entries out of 24 total entries before search.")

    except AssertionError as e:
        print(f"❌ Assertion Failed: {e}")

    except Exception as e:
        print(f"❌ Test Failed: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_search_functionality()
