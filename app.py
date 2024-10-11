from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# LinkedIn login details


# Job search term
job_title = 'Software Engineer'
location = 'New York'

# Path to your Chrome WebDriver
driver_path = '/usr/local/bin/chromedriver'

# Initialize the WebDriver
driver = webdriver.Chrome(driver_path)

# Open LinkedIn login page
driver.get('https://www.linkedin.com/login')

# Find username and password fields and enter login info
email_elem = driver.find_element(By.ID, 'username')
email_elem.send_keys(username)

password_elem = driver.find_element(By.ID, 'password')
password_elem.send_keys(password)

# Submit login form
password_elem.send_keys(Keys.RETURN)

# Wait for login to complete
time.sleep(3)

# Navigate to the job search page
driver.get(f'https://www.linkedin.com/jobs/search/?keywords={job_title}&location={location}')

# Wait for the job search results to load
time.sleep(3)

# Scrape job posts
job_posts = driver.find_elements(By.CLASS_NAME, 'result-card__contents')

for job in job_posts:
    title = job.find_element(By.CLASS_NAME, 'result-card__title').text
    company = job.find_element(By.CLASS_NAME, 'result-card__subtitle').text
    location = job.find_element(By.CLASS_NAME, 'job-result-card__location').text
    link = job.find_element(By.TAG_NAME, 'a').get_attribute('href')
    
    print(f"Job Title: {title}")
    print(f"Company: {company}")
    print(f"Location: {location}")
    print(f"Link: {link}")
    print("-" * 40)

# Close the browser
driver.quit()
