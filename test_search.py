from selene.support.shared import browser
from selene import be, have
import pytest

def test_unsuccessful_search():
    browser.open('https://google.com')
    browser.element('[id="L2AGLb"]').click()
    browser.element('[name="q"]').should(be.blank).type('gfdgdefnnvfnvfdn').press_enter()
    browser.element('[id="result-stats"]').should(have.text('0'))

#def test_unsuccessful_search():
   # browser.open('https://google.com')
   # browser.element('[id="L2AGLb"]').click()
   # browser.element('[name="q"]').should(be.blank).type('vbvnbv').press_enter()
   # browser.element('[id="result-stats"]').should(have.text('0'))
def test_unsuccessful_search():
    browser.open('https://google.com')
    browser.element('[id="L2AGLb"]').click()
    browser.element('[name="q"]').should(be.blank).type('gfdgdefnnvdddddsssfnvfdn').press_enter()
    browser.element('[id="rimg_1"]').should(have.css_property('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDov…iIGRpc3BsYXk9ImJsb2NrIi8+PC9nPjwvZz48L2c+PC9zdmc+'))

    @pytest.fixture
    def browser_size():
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    def test_successful_search(browser_size):
        browser.open('https://google.com')
        browser.element('[id="L2AGLb"]').click()
        browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
        browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

    def test_unsuccessful_search(browser_size):
        browser.open('https://google.com')
        browser.element('[name="q"]').should(be.blank).type('gfdyg77][[]gdefnnvfwnvfdn').press_enter()
        browser.element('[id="result-stats"]').should(have.text('0'))