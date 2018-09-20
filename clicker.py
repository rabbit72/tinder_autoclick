import random
import time

import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login(driver, phone_number):
    wait = WebDriverWait(driver, 100).until
    xpath = {
        "phone_login": "//div[@id='modal-manager']/div/div/div[2]/div/div[3]/div[2]/button/span/span",
        "continue_login": "//div[@id='modal-manager']/div/div/div[2]/button/span/span",
        "button_1": "//div[@id='content']/div/span/div/div/div/div/div/div/div/button/span",
        "button_2": "//div[@id='content']/div/span/div/div/div/div/main/div/div/button/span",
        "button_3": "//div[@id='content']/div/span/div/div/div/div/div[1]/div/div/button/span",
        "button_4": "//div[@id='content']/div/span/div/div[2]/div/div/div/div/div[3]/button/span/span",
    }
    phone_login_button = wait(
        EC.element_to_be_clickable((By.XPATH, xpath["phone_login"]))
    )
    phone_login_button.click()
    phone_field = wait(EC.element_to_be_clickable((By.NAME, "phone_number")))
    phone_field.send_keys(phone_number)
    continue_button = wait(
        EC.element_to_be_clickable((By.XPATH, xpath["continue_login"]))
    )
    continue_button.click()

    for b in ["button_1", "button_2", "button_3"]:
        wait(EC.element_to_be_clickable((By.XPATH, xpath[b]))).click()

    page = driver.find_element_by_tag_name("html")
    for button in [Keys.TAB, Keys.TAB, Keys.ENTER]:
        page.send_keys(button)

    wait(EC.element_to_be_clickable((By.XPATH, xpath["button_4"]))).click()


def click_like(driver, numbers=1):
    for _ in range(numbers):
        like_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "recsGamepad__button--like"))
        )
        like_button.click()
        pause = random.uniform(0.5, 2)
        time.sleep(pause)


@click.command()
@click.argument("phone_number")
@click.option("--likes", "-l", default=10, help="How many likes need to do?")
def enter_point(phone_number, likes):
    """
    This is autoclicker for Tinder.com We use authentication with mobile phone
    Format phone number 9121234567 (without country code)
    """
    driver = webdriver.Chrome()
    driver.get("https://tinder.com/")

    assert "Tinder" in driver.title

    login(driver, phone_number)
    click_like(driver, likes)

    driver.close()


if __name__ == '__main__':
    enter_point()
