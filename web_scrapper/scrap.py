import time
import os
import asciichartpy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_rate_from_url(driver, url):
    driver.get(url)
    last_rate = driver.find_element(By.XPATH, "//div[@data-test='instrument-price-last']")
    last_rate_float = float(last_rate.text)
    return last_rate_float

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

width = 50  # Width of the chart
height = 10  # Optional, controls scaling
history_uzs = []  # Store historical data
history_usd = []
max_points = 100  # Maximum number of points to display

#setup chrome webdriver
driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

try:
    # Load the web page
    # driver.get('https://www.investing.com/currencies/uzs-rub')

    # Locate the element
    # last_rate = driver.find_element(By.XPATH, "//div[@data-test='instrument-price-last']")
    os.system('cls' if os.name == 'nt' else 'clear')

    # Loop until interrupted
    while True:
        # last_rate_float = float(last_rate.text)
        uzs_to_rub = get_rate_from_url(driver, "https://www.investing.com/currencies/uzs-rub")
        rub_to_uzs = round(1 / uzs_to_rub, 2)
        history_uzs.append(rub_to_uzs)

        if len(history_uzs) > max_points:
           history_uzs = history_uzs[-max_points:] 

        usd_to_rub = get_rate_from_url(driver, "https://www.investing.com/currencies/usd-rub")
        history_usd.append(usd_to_rub)

        if len(history_usd) > max_points:
            history_usd = history_usd[-max_points]

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"RUB/UZS: {rub_to_uzs} so'ms for 1 ruble\t|\tUSD/RUB: 100 rubles for 1 usd")  # Fetch and print the current rate

        chart = asciichartpy.plot([history_uzs, history_usd], {'height': height, 'offset': 3, 'colors': [asciichartpy.blue, asciichartpy.green]})
        print(chart)
        time.sleep(1)  # Sleep for 20 seconds

except KeyboardInterrupt:
    print("Program interrupted by user.")

finally:
    # Close the driver
    driver.quit()
    print("WebDriver closed.")

