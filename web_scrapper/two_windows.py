import time
import os
import datetime as dt
# import asciichartpy
from colorama import Fore
from colorama import Back
from colorama import Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_rate_from_url(driver):
    last_rate = driver.find_element(By.XPATH, "//div[@data-test='instrument-price-last']")
    last_rate_float = float(last_rate.text)
    return last_rate_float

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1"
]

uzs_to_rub_url = "https://www.investing.com/currencies/uzs-rub" 
usd_to_rub_url = "https://www.investing.com/currencies/usd-rub"

width = 50  # Width of the chart
height = 10  # Optional, controls scaling
history_uzs = []  # Store historical data
history_usd = []
ts = [] # Time data
max_points = 20  # Maximum number of points to display

options = Options()
options.add_argument("--headless")
options.add_argument(f"--user-agent={random.choice(user_agents)}")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

try:
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    driver_two = webdriver.Chrome(service=service, options=options)
except(NoSuchDriverException):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver_two = webdriver.Chrome(service=service, options=options)

try:

    driver.get(uzs_to_rub_url)
    driver_two.get(usd_to_rub_url)

    def animate(i, ts, history_usd):
        ts.append(dt.datetime.now().strftime('%H:%M:%S'))
        ts = ts[-max_points:]
        # uzs_to_rub = get_rate_from_url(driver)
        # if uzs_to_rub > 1:
        #     uzs_to_rub /= 10000

        # rub_to_uzs = round(1 / uzs_to_rub, 2)
        # history_uzs.append(rub_to_uzs)

        # if len(history_uzs) > max_points:
        #    history_uzs = history_uzs[-max_points:] 

        usd_to_rub = get_rate_from_url(driver_two)
        history_usd.append(round(float(usd_to_rub), 2))

        if len(history_usd) > max_points:
            history_usd = history_usd[-max_points:]

        ax.clear()
        ax.plot(ts, history_usd)
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('USD/RUB')
        plt.ylabel('RUB')
        # os.system('cls' if os.name == 'nt' else 'clear')

        # print(f"{Fore.BLUE}RUB/UZS:{Style.RESET_ALL} {Back.YELLOW}{Fore.MAGENTA}{Style.BRIGHT}{rub_to_uzs}{Style.RESET_ALL} so'ms for 1 ruble\t|\t{Fore.GREEN}USD/RUB:{Style.RESET_ALL} {Back.YELLOW}{Fore.MAGENTA}{Style.BRIGHT}{usd_to_rub}{Style.RESET_ALL} rubles for 1 usd")  # Fetch and print the current rate

        # chart = asciichartpy.plot([history_uzs, history_usd], {'height': height, 'offset': 3, 'colors': [asciichartpy.blue, asciichartpy.green]})
        # print(chart)
        # time.sleep(1)  # Sleep for 20 seconds

    ani = animation.FuncAnimation(fig, animate, fargs=(ts, history_usd), interval=1000, cache_frame_data=False)
    plt.show()

except KeyboardInterrupt:
    print("Program interrupted by user.")


finally:
    driver.quit()
    driver_two.quit()
    print("Both drivers were stopped")








# driver_two.get(usd_to_rub_url)
# first_tab = driver.current_window_handle

# search_input = driver.find_element(By.XPATH, '//form[@action="/search"]/input[1]')
# search_input.clear()
# search_input.click()
# search_input.send_keys("USD/RUB")
# time.sleep(5)
# wait = WebDriverWait(driver, 20)
# usd_rub_anchor = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="https://www.investing.com/currencies/usd-rub"]')))
# ActionChains(driver).key_down(Keys.LEFT_CONTROL).click(usd_rub_anchor).key_up(Keys.LEFT_CONTROL).perform()
# usd_rub_anchor.click()
# print(usd_rub_anchor)
# time.sleep(20)

# driver.switch_to.window(driver.window_handles[1])

# Open the second URL in a new tab
# driver.execute_script(f"window.open('{usd_to_rub_url}', '_blank');")
# driver.switch_to.window(driver.window_handles[1])
# driver.get(usd_to_rub_url)
# driver.get("https://pace.coe.int/en/aplist/committees/9/commission-des-questions-politiques-et-de-la-democratie")
# time.sleep(5)
# WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='Widget containing a Cloudflare security challenge']")))
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.ctp-checkbox-label"))).click()
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

# driver.switch_to.window(second_tab)
# usd_to_rub = get_rate_from_current_tab(driver)
# print(driver.page_source)
# print(driver.window_handles)
# print(search_input)
# Print results
# print(f"RUB/UZS: {rub_to_uzs} so'ms for 1 ruble")
# print(f"USD/RUB: {usd_to_rub} rubles for 1 USD")
# time.sleep(5)
# driver.quit()
# driver_two.quit()