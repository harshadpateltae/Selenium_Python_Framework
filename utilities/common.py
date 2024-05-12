import os
import platform
import random
import string
import time
from datetime import datetime, timedelta
import pyautogui
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import threading
import logging


class Common:
    """ Wrapper for selenium operations """
    logging.basicConfig(filename='.\\Logs\\automation.log', level=logging.INFO,
                        format='%(asctime)s: %(levelname)s: (message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.steps = threading.local()
        self.first_window = threading.local()
        self.second_window = threading.local()
        self.steps.value = 1

    def print(self, msg_to_print):
        if msg_to_print.startswith("Step"):
            message = msg_to_print.split("::")
            reporter_log = "Step {}: {}".format(self.steps.value, message[1].strip())
            logging.info(reporter_log)
            print(reporter_log)
            self.steps.value += 1  # Increment steps for each step message
        else:
            logging.info(msg_to_print)
            print(msg_to_print)

    def wait_until_element_to_be_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.highlight_from_wait(element)
        return element

    def pause(self):
        time.sleep(3)

    def wait_until_alert_present(self):
        self.wait.until(EC.alert_is_present())

    def wait_until_element_to_be_visible(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.highlight_from_wait(element)
        return element

    def wait_until_frame_to_be_available_and_switch_to_it(self, index):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(index))

    def wait_until_elements_to_be_visible(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def len(self, locator):
        return len(self.wait_until_elements_to_be_visible(locator))

    def is_displayed(self, locator):
        element = self.wait_until_element_to_be_visible(locator)
        return element.is_displayed()

    def is_enabled(self, locator):
        element = self.wait_until_element_to_be_visible(locator)
        return element.is_enabled()

    def is_selected(self, locator):
        element = self.wait_until_element_to_be_visible(locator)
        return element.is_selected()

    def is_exist(self, locator):
        try:
            element = self.driver.find_element(locator)
            self.highlight_from_wait(element)
            return True
        except NoSuchElementException:
            return False

    def click(self, locator, index=None):
        if index is None:
            self.wait_until_element_to_be_clickable(locator).click()
        else:
            new_locator = (locator[0], locator[1] + "[" + str(index) + "]")
            self.wait_until_element_to_be_clickable(new_locator).click()

    def click_javascript(self, locator):
        element = self.wait_until_element_to_be_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def move_to_element(self, locator):
        element = self.wait_until_element_to_be_clickable(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def get_attribute(self, locator, attribute, index=None):
        if index is None:
            return self.wait_until_element_to_be_visible(locator).get_attribute(attribute)
        else:
            new_locator = (locator[0], locator[1] + "[" + str(index) + "]")
            return self.wait_until_element_to_be_visible(new_locator).get_attribute(attribute)

    def send_keys(self, locator, text):
        element = self.wait_until_element_to_be_clickable(locator)
        element.clear()
        element.send_keys(text)

    def clear(self, locator):
        self.wait_until_element_to_be_clickable(locator).clear()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_element(self, locator):
        element = self.wait_until_element_to_be_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_by_pixel(self, x_pixels, y_pixels):
        try:
            self.driver.execute_script("window.scrollBy(" + x_pixels + "," + y_pixels + ")")
        except Exception as e:
            print("An error occurred:", e)

    def random_number_integer(self, start, end):
        return random.randint(start, end)

    def os_name(self):
        return platform.system().lower()

    def switch_to_frame(self, index):
        self.wait_until_frame_to_be_available_and_switch_to_it(index)

    def switch_to_frame(self, locator):
        try:
            element = self.wait_until_element_to_be_visible(locator)
            self.driver.switch_to.frame(element)
        except Exception as e:
            print("An error occurred:", e)

    def switch_to_frame(self):
        self.driver.switch_to.default_content()

    def text(self, locator, index=None):
        if index is None:
            return self.wait_until_element_to_be_visible(locator).text
        else:
            new_locator = (locator[0], locator[1] + "[" + str(index) + "]")
            return self.wait_until_element_to_be_visible(new_locator).text

    def tooltip_text(self, locator, tooltip_locator):
        self.move_to_element(locator)
        tooltip = self.wait_until_element_to_be_visible(tooltip_locator)
        return tooltip.text

    def wait_until_page_loaded(self):
        old_page = self.driver.find_element_by_tag_name('html')
        yield
        self.wait.until(EC.staleness_of(old_page))

    def highlight_from_wait(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                   element, "border: 4px solid red;")

    def highlight_element(self, locator):
        self.wait_until_element_to_be_visible(locator)

    def is_contains_numeral(self, to_be_checked):
        for i in range(10):
            if str(i) in to_be_checked:
                return True
        return False

    def indexed_locator(self, locator, index):
        first = locator[0]
        second = locator[1] + "[" + str(index) + "]"
        return first, second
