from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:/Development/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&geoId=100456013&keywords=python%20developer&location=Finland")

sing_in = driver.find_element_by_link_text("Sign in")
sing_in.click()

sleep(5)

username = driver.find_element(by=By.ID, value="username")
username.click()
username.send_keys("EMAIL")

password = driver.find_element(by=By.ID, value="password")
password.click()
password.send_keys("PASSWORD")

log_in = driver.find_element_by_css_selector(".login__form_action_container  button")
log_in.click()
sleep(5)

job_list = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-list__title")
for job in job_list:
    job.click()
    sleep(2)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-apply-button")
        apply_button.click()
        sleep(5)

        submit = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit.get_attribute("aria-label") == "Continue to next step":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit.click()
        sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

        # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

sleep(5)
driver.quit()
