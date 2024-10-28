from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to get Chrome browser driver
def get_browser():
    return webdriver.Chrome()  # Ensure the correct WebDriver is installed and added to PATH

# Function to check responsiveness of the login page
def check_responsiveness(driver, resolutions):
    for width, height in resolutions:
        # Resize the browser window
        driver.set_window_size(width, height)
        time.sleep(2)  # Allow the page to adjust to the new size

        # Take a screenshot for each resolution
        screenshot_name = f"screenshot_{width}x{height}.png"
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved for resolution {width}x{height}: {screenshot_name}")

        # Check if the username field is displayed
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # Print the visibility status of key elements
        print(f"Username field visible: {username_field.is_displayed()}")
        print(f"Password field visible: {password_field.is_displayed()}")
        print(f"Login button visible: {login_button.is_displayed()}\n")

# Function to perform login test
def test_login(driver):
    # Locate the username field and enter the username
    driver.find_element(By.NAME, "username").send_keys("Admin")

    # Locate the password field and enter the password
    driver.find_element(By.NAME, "password").send_keys("admin123")

    # Click the login button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for the page to load after login
    time.sleep(5)

    # Verify the title of the page
    act_title = driver.title
    exp_title = "OrangeHRM"

    assert act_title == exp_title, "Login Test Failed"
    print("Login Test Passed")

# Function to perform logout test
def test_logout(driver):
    try:
        # Wait for the profile dropdown (username and image) to be clickable and then click it
        profile_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.oxd-userdropdown-tab"))
        )
        profile_dropdown.click()

        # Wait for the logout link to be clickable and then click it
        logout_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
        )
        logout_link.click()

        # Wait for the page to load after logout
        time.sleep(5)

        # Verify the title of the page
        act_title = driver.title
        exp_title = "OrangeHRM"  # Adjust this based on what the title should be after logout

        assert act_title == exp_title, "Logout Test Failed"
        print("Logout Test Passed")
    except Exception as e:
        print(f"Logout Test Failed: {str(e)}")
# Main function to run tests
def run_tests():
    # Initialize the Chrome WebDriver
    driver = get_browser()

    # Open the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)  # Wait for the page to load

    # Take an initial screenshot of the login page
    driver.save_screenshot("screenshot_initial.png")

    # Define resolutions to check
    resolutions = [
        (1920, 1080),  # Full HD
        (1366, 768),   # HD
        (1280, 800),   # WXGA
        (768, 1024),   # Tablet Portrait
        (360, 640),    # Mobile
    ]

    # Check responsiveness at defined resolutions
    check_responsiveness(driver, resolutions)

    # Perform the login test
    test_login(driver)

    # Perform the logout test
    test_logout(driver)

    # Close the browser
    driver.quit()

# Run the tests
run_tests()
