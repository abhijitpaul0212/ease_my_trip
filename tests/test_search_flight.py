from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
# from libraries.common import Utils

# utils = Utils()

def cleanse_data(data):
        date_list = []
        price_list = []
        for item in data:
            x = item.split('\n')
            if len(x) > 1:
                date_list.append(x[0])
                price_list.append(x[1])
            else:
                date_list.append(x[0])
                price_list.append(x[0])
        return date_list, price_list


def find_min_value_index(data):
    """
    This function finds the minumum value from the given list
    :param data: list of data
    :return: minimum value, list of indexes contains minimum valuue
    """
    smallest = min(data)
    return smallest, [index for index, element in enumerate(data)
                    if smallest == element]


def process_data(data):
    """
    This function reads the data provided and process it into required fashion
    :param data: data list
    :return: list which doesnt contains weekend and blank data
    """
    outer_list = []
    inner_list = []
    inner_list_without_empty_data = []
    final_list = []
    memory_count = 0
    counter = 0
    while len(data) > 0:
        for index, pos in enumerate(range(memory_count, len(data))):
            counter += 1
            inner_list.append(data[pos])
            if (index == 6) or (counter == len(data)):
                if len(inner_list) == 7:
                    inner_list = inner_list[1:-1]
                else:
                    inner_list = inner_list[1:]
                for val in inner_list:
                    if val != '':
                        inner_list_without_empty_data.append(val)
                outer_list.append(inner_list_without_empty_data)
                inner_list = []
                inner_list_without_empty_data = []
                memory_count = pos + 1
                break
        if len(data) == counter:
            break
    for val in outer_list:
        final_list.extend(val)
    return final_list


def test_easemytrip_select_departure_date(driver):
    """
    Test case for the scenario of selecting lowest fare departure date
    :param driver: driver object
    :return:
    """
    print("Program begins...")

    test_url = "https://www.easemytrip.com/"
    month = "Sep 2021"

    # provide the path of geckodriver in executable_path arg of Firefox
    # browser = webdriver.Firefox(executable_path=r"F:\Studies\Python\SeleniumFramework\Executables\geckodriver64bit.exe")
    # driver = webdriver.Firefox(executable_path="F:\\Studies\\Python\\LearnGitHub\\ease_my_trip\\resources\\geckodriver64bit.exe")
    driver.get(test_url)

    departure_date = driver.find_element_by_xpath("//*[@id='ddate']")
    departure_date.click()

    # weekdays = driver.find_elements_by_xpath("//div[text()='"+ month +"']/parent::div/parent::div/*[@class='weekdays']//li")
    # weekdays = [day.text for day in weekdays]

    dates = driver.find_elements_by_xpath("//div[text()='"+ month +"']/parent::div/parent::div/*[@class='weekdays']/following-sibling::div[@class='days']//li")
    date_list, price_list = cleanse_data([item.text for item in dates])

    date_list_val = process_data(date_list)
    price_list_val = process_data(price_list)

    min_value, index_value = find_min_value_index(price_list_val)

    minumum_fare_date = str(date_list_val[index_value[-1]])
    print("Minimum Flight ticket price is on Date =", minumum_fare_date, "of", month)
    print("Minimum Flight ticket price is = Rs.", str(min_value))

    minimum_fare_date_xpath = "//div[text()='"+ month +"']/parent::div/parent::div/*[@class='days']//li[text()='"+ minumum_fare_date +"']"

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, minimum_fare_date_xpath)))

    assert driver.find_element_by_xpath(minimum_fare_date_xpath).is_displayed()

    driver.find_element_by_xpath(minimum_fare_date_xpath).click()
    print("Departure Date has been selected in the calendar")
