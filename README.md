
# Selenium Search Functionality Test

This repository contains a Python script to test the search functionality of a table on the LambdaTest website using Selenium WebDriver. The script verifies that the search functionality filters the results correctly and checks the total number of displayed entries before and after performing a search.

---

## Approach

1. **Setup WebDriver**:  
   The script uses Selenium WebDriver with the Chrome browser in headless mode (no GUI).

2. **Page Interaction**:  
   It navigates to the "Selenium Playground" page and interacts with the search input field.

3. **Assertions**:
   - Verifies that the total number of entries on the page before the search is **24**.
   - After performing a search, it checks that the number of displayed entries is **5**.

4. **WebDriver Cleanup**:  
   The browser window is closed after the test completes, regardless of whether the test passes or fails.

---

## Requirements

- Python 3.10 or higher
- Selenium WebDriver
- ChromeDriver installed

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rahul-lee/pytest_table_search.git
   cd pytest_table_search
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Note**: Ensure you have ChromeDriver installed and available in your system `PATH`. For detailed installation instructions, refer to the [Additional Setup Instructions](#additional-setup-instructions).

---

## Running the Script

After setting up the environment and dependencies, you can run the script using the following command:

```bash
python test_search_functionality.py
```

The script will launch a headless Chrome browser, perform the test, and output the result in the terminal.

---

## Results

- If the assertions pass, it will print:
  ```
  ✅ Test Passed: Search results show 5 entries out of 24 total entries before search.
  ```

- If an assertion fails, it will print an error message explaining the failure.

---

## Additional Setup Instructions

For detailed steps on installing ChromeDriver or using `webdriver-manager`, refer to the [Additional Setup Instructions](#additional-setup-instructions) section.

---


### Additional Setup Instructions

#### Installing ChromeDriver

To run the Selenium script, you need to have **ChromeDriver** installed and properly configured. Follow these steps:

1. **Download ChromeDriver**:
   - Visit the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/).
   - Download the version of ChromeDriver that matches your installed version of Google Chrome.

2. **Install ChromeDriver**:
   - **Windows**:
     1. Extract the downloaded `chromedriver.exe` file.
     2. Move the `chromedriver.exe` file to a directory included in your system's `PATH` (e.g., `C:\Windows\`).
   - **macOS/Linux**:
     1. Extract the downloaded `chromedriver` file.
     2. Move the `chromedriver` file to `/usr/local/bin/` (or another directory in your `PATH`).
        ```bash
        sudo mv ~/Downloads/chromedriver /usr/local/bin/
        ```

3. **Verify Installation**:
   - Open a terminal or command prompt and run:
     ```bash
     chromedriver --version
     ```
   - If installed correctly, this will display the ChromeDriver version.

Thanks for visiting 😊
