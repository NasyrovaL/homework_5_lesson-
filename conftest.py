import pytest
from selene import browser

@pytest.fixture(scope="function")
def setting_browser():
    browser.config.timeout=60
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield
    browser.quit()  # закрывает браузер после выполнения теста
    print("Закрываем браузер")