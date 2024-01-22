from selene import browser, be, have, Config
import pytest

@pytest.fixture
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser
    browser.quit()

def test_google_search_with_pytest_qa(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_search_with_pytest_qa_not_info(browser_size, eager=None):
    browser.open('https://google.com')
    #Config.pageLoadStrategy = eager
    browser.element('[name="q"]').should(be.blank).type('12345qwerty0077gfyjtfyjtfyt555444333').press_enter()
    browser.element('[id="search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))
