import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_w3schools_logo(browser):
    # Navigate to the W3Schools website
    browser.get("https://www.w3schools.com/")

    # Find the W3Schools logo element
    logo = browser.find_element(By.XPATH, "//i[@class='fa fa-logo ws-hover-text-green']")
    # Assert that the logo is present on the page
    assert logo is not None


if __name__ == "__main__":
    pytest.main()
