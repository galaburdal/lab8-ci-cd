import shutil

# pylint: disable=unused-argument

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Jenkins Docker has Chromium + chromedriver installed system-wide.
    # On the local Mac, webdriver-manager supplies the driver.
    chromedriver = shutil.which("chromedriver")
    if chromedriver:
        service = Service(chromedriver)
        context.driver = webdriver.Chrome(service=service, options=options)
    else:
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=options)

    context.driver.implicitly_wait(5)


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
