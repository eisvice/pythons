import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service('/usr/bin/chromedriver')

# driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=service)
driver_two = webdriver.Chrome(service=service)
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# driver.get("https://www.investing.com/currencies/uzs-rub")
# driver.maximize_window()
# current_handle = driver.window_handles

# print(current_handle)

# driver.switch_to.window()
uzs_to_rub_url = "https://www.investing.com/currencies/uzs-rub" 
usd_to_rub_url = "https://www.investing.com/currencies/usd-rub"

driver.get(uzs_to_rub_url)
# driver.maximize_window()

driver_two.get(usd_to_rub_url)
# first_tab = driver.current_window_handle

# Open the second URL in a new tab
# driver.execute_script("window.open('', '_blank');")
# second_tab = [tab for tab in driver.window_handles if tab != first_tab][0]

# Switch to the first tab and get data
# driver.switch_to.window(first_tab)
# uzs_to_rub = get_rate_from_current_tab(driver)
# rub_to_uzs = round(1 / uzs_to_rub, 2)
# driver.switch_to.window(driver.window_handles[1])
# driver.get(usd_to_rub_url)
# Switch to the second tab and get data
# for _ in range(6):
#     driver.switch_to.window(driver.window_handles[0])
#     time.sleep(5)
#     driver.switch_to.window(driver.window_handles[1])
#     time.sleep(5)

# usd_to_rub = get_rate_from_current_tab(driver)

# Print results
# print(f"RUB/UZS: {rub_to_uzs} so'ms for 1 ruble")
# print(f"USD/RUB: {usd_to_rub} rubles for 1 USD")
time.sleep(5)
driver.quit()