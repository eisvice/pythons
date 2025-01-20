import random
import datetime
from selenium import webdriver
import matplotlib.pyplot as plt
import matplotlib.animation as anime
from two_windows import (
    get_rate_from_url,
    driver,
    driver_two,
    usd_to_rub_url,
    uzs_to_rub_url,
)


# FOR TESTING ONLY
def generate_data(
    base_value: float,
    rub_usd_rate_collection: list,
    precision: int = 2,
    collection_size: int = 25,
) -> list:
    if len(rub_usd_rate_collection) == 0:
        rub_usd_rate_collection.append(base_value)
        return rub_usd_rate_collection

    rand_num = random.uniform(-10, 10)
    num_to_append = round(rub_usd_rate_collection[-1] + rand_num, precision)

    rub_usd_rate_collection.append(num_to_append)
    if len(rub_usd_rate_collection) > collection_size:
        rub_usd_rate_collection.pop(0)

    return rub_usd_rate_collection


def get_data_from_web(
    interested_currency: str,
    rate_collection: list,
    driver: webdriver.Chrome,
    precision: int = 2,
    collection_size: int = 25,
) -> list:
    last_rate = get_rate_from_url(driver)

    # workaround for so'ms
    if interested_currency.lower() == "som":
        if last_rate > 1:
            last_rate /= 10000
        last_rate = 1 / last_rate

    rate_collection.append(round(last_rate, precision))
    if len(rate_collection) > collection_size:
        rate_collection.pop(0)

    return rate_collection


def generate_time_data(time_list: list, collection_size: int = 25):
    time_list.append(datetime.datetime.now().strftime("%H:%M:%S"))
    if len(time_list) > collection_size:
        time_list.pop(0)

    return time_list


def create_plot(i, time_list, rub_usd_rate_collection, som_rub_rate_collection):
    precision = 4
    collection_size = 25

    time_list = generate_time_data(time_list, collection_size)

    rub_usd_rate_collection = get_data_from_web(
        "usd", rub_usd_rate_collection, driver, precision, collection_size
    )
    som_rub_rate_collection = get_data_from_web(
        "som", som_rub_rate_collection, driver_two, precision, collection_size
    )

    ax.clear()
    ax.plot(
        time_list,
        rub_usd_rate_collection,
        label=f"RUB/USD - {rub_usd_rate_collection[-1]}",
        marker="o",
        linestyle="-",
        color="g",
    )
    ax.plot(
        time_list,
        som_rub_rate_collection,
        label=f"SO'M/RUB - {som_rub_rate_collection[-1]}",
        marker="x",
        linestyle="--",
        color="b",
    )

    plt.xticks(rotation=45, ha="right")
    plt.subplots_adjust(bottom=0.10)
    plt.title("Currency Exchange Rates Live Plot")
    plt.ylabel("Currency Rate")
    plt.xlabel("Time")
    plt.legend(bbox_to_anchor=(0.5, 1.28), loc="upper center")
    plt.tight_layout()


def start_scrapping():
    time_list = []
    rub_usd_rate_collection = []
    som_rub_rate_collection = []

    try:
        driver.get(usd_to_rub_url)
        driver_two.get(uzs_to_rub_url)

        global fig, ax
        fig = plt.figure(figsize=(12, 6), num="Rate Exchange")
        ax = fig.add_subplot()

        live_graph = anime.FuncAnimation(
            fig,
            create_plot,
            fargs=(time_list, rub_usd_rate_collection, som_rub_rate_collection),
            interval=1000 * 60 * 3,
            cache_frame_data=False,
        )

        plt.show()

    finally:
        driver.quit()
        driver_two.quit()
        print("Both drivers were stopped")


def main():
    start_scrapping()


if __name__ == "__main__":
    main()
