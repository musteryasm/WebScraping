
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver with options to ignore certificate errors
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)  # Use 'options' instead of 'chrome_options'

# URL of the website you want to scrape
url = "https://www.acemicromatic.net/product_cat/milling/"

# Navigate to the website
driver.get(url)

# Find all elements with the specified class
button_wrappers = driver.find_elements(By.CSS_SELECTOR, 'div.button-wrapper a')

# Initialize a list to store extracted data
data_list = []

# Loop through the button_wrappers and click each link
for i in range(len(button_wrappers)):
    button_wrappers = driver.find_elements(By.CSS_SELECTOR, 'div.button-wrapper a')
    button_wrappers[i].click()
    
    # Extract product specifications
    param_1 = None
    param_2 = None
    model_name = None
    travels_text = None

    elements = driver.find_elements(By.CSS_SELECTOR, 'div.product-details div.row')
    if len(elements) >= 3:
        param_1 = elements[0].text
        param_2 = elements[1].text
        model_name = driver.find_element(By.CSS_SELECTOR, 'h3').text
        travels_text = elements[2].text

    if travels_text:
        # Split the travels_text into x_travel, y_travel, and z_travel
        travels_values = travels_text.split('/')
        x_travel = travels_values[0].strip().split(' ')[-1]
        y_travel = travels_values[1].strip()
        z_travel = travels_values[2].strip()
        
        # Append the extracted data to the data_list
        data_list.append([param_1, param_2, model_name, x_travel, y_travel, z_travel])

        # Print the extracted data
        print("param_1\tparam_2\tmodel_name\tx_travel\ty_travel\tz_travel")
        for data in data_list:
            print('\t'.join(data))

    # Go back to the previous page
    driver.back()

# Close the WebDriver
driver.quit()

