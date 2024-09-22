from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    print(hello())

    # getting started tutorial
    # https://www.selenium.dev/documentation/webdriver/getting_started/first_script/

    # start driver session
    driver = webdriver.Chrome()

    # navigate to a web page
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    
    # There are a bunch of types of information about the browser you can request, including window handles, browser size / position, cookies, alerts, etc.
    title = driver.title

    # wait for an element to be loaded on the page before accessing it
    driver.implicitly_wait(0.5)
    
    # find an element to interact with
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # take an action on an element
    text_box.send_keys("Selenium")
    submit_button.click()

    # request an element's information
    message = driver.find_element(by=By.ID, value="message")

    # quit the driver session, also closing the browser
    driver.quit()

def hello() -> str:
    return "Hello from pizza-lever!"



if __name__ == "__main__":
    main()
