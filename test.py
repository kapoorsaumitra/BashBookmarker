from selenium import webdriver

# Start a browser session
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://www.example.com')

# Perform actions on the webpage
# ...

# Close the browser session
driver.quit()
