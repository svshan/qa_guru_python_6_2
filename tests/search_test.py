from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_search_with_valid_values(browser_size):
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="r1-0"] .EKtkFWMYpwzMKOYr0GYm').should(
        have.text('User-oriented Web UI browser tests in Python'))
    print("List of results for request with valid values")


def test_search_with_invalid_values(browser_size):
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type('"cats and dogs dgvgjnnnfЕРВЫuhИСТИ"').press_enter()
    browser.element('.deB7ubqmD22Y2q4Hxlgr').should(have.text('No results found for'))
    print("No results for request with invalid values")