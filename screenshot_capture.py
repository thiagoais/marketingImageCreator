from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Define the target URL and file paths for screenshots
desktop_screenshot = "desktop_screenshot.png"
tablet_screenshot = "tablet_screenshot.png"
phone_screenshot = "phone_screenshot.png"

# extra window sizes on the borders of the image
extra_window_width_ignore = 44
extra_window_height_ignore = 183

# Function to take a screenshot with specified dimensions and hide scrollbar
def take_screenshot(driver, width, height, file_name):
    # Set window size
    driver.set_window_size(width, height)

    # Hide the scrollbar using JavaScript
    driver.execute_script("document.body.style.overflow = 'hidden';")
    time.sleep(2)  # Allow time for page to load fully

    # Take the screenshot
    driver.save_screenshot(file_name)
    print(f"Screenshot saved as {file_name}")

    # Restore scrollbar after taking the screenshot
    driver.execute_script("document.body.style.overflow = '';")


def capture_website_screenshots(url):
    # Set up Selenium with headless Chrome
    options = Options()
    options.headless = True  # Run in headless mode (no GUI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Path to your ChromeDriver
    driver = webdriver.Chrome(options=options)

    try:
        # Load the URL
        driver.get(url)

        # Take Desktop Screenshot (1920x1080)
        take_screenshot(driver, 1920 + extra_window_width_ignore, 1202 + extra_window_height_ignore, desktop_screenshot)

        # Take Tablet Screenshot (768x1024)
        take_screenshot(driver, 840 + extra_window_width_ignore, 1203 + extra_window_height_ignore, tablet_screenshot)

        # Take Phone Screenshot (1080x1920)
        take_screenshot(driver, 480 + extra_window_width_ignore, 1037 + extra_window_height_ignore, phone_screenshot)

        # Return the paths to the saved screenshots
        return desktop_screenshot, tablet_screenshot, phone_screenshot
    finally:
        # Close the browser
        driver.quit()

# Uncomment below if you want to run this script directly
# capture_website_screenshots("https://www.example.com")