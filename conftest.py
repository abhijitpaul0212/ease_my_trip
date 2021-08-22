import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    """
    This fixture uses yield() method approach for teardown
    :return:
    """
    print('*****SETUP*****')
    browser = webdriver.Firefox(executable_path="F:\\Studies\\Python\\LearnGitHub\\ease_my_trip\\resources\\geckodriver64bit.exe")
    print("Browser is launched")
    yield browser
    print("Reached Teardown, so will be closing the browser")
    browser.close()
    browser.quit()


# @pytest.mark.skip()
# @pytest.fixture(scope='function')
# def driver(request):
#     """
#     This fixture uses addfinalizer() method approach for teardown
#     :return:
#     """
#     print('*****SETUP*****')
#     browser = webdriver.Firefox(executable_path=r"F:\Studies\Python\SeleniumFramework\Executables\geckodriver64bit.exe")
#     print("Browser is launched")
#     print("Reached Teardown, so will be closing the browser")
#     request.addfinalizer(browser.close())
#     return browser
