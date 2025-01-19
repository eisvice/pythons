import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchDriverException

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
]

uzs_to_rub_url = "https://www.investing.com/currencies/uzs-rub"
usd_to_rub_url = "https://www.investing.com/currencies/usd-rub"

options = Options()
options.add_argument("--headless")
options.add_argument(f"--user-agent={random.choice(user_agents)}")

try:
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    driver_two = webdriver.Chrome(service=service, options=options)
except NoSuchDriverException:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver_two = webdriver.Chrome(service=service, options=options)


def get_rate_from_url(driver: webdriver.Chrome) -> float:
    last_rate = driver.find_element(
        By.XPATH, "//div[@data-test='instrument-price-last']"
    )
    last_rate_float = float(last_rate.text)
    return last_rate_float
