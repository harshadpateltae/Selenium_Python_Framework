import pytest

from pageObjects.all_Locators import Locators
from utilities.common import Common
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup", "log_on_failure")
class TestCart():
    url = ReadConfig.getCommonInfo("baseURL")
    logger = LogGen.loggen()

    def test_verify_empty_cart(self):
        common = Common(self.driver)
        common.print("Step :: Open URL : " + self.url)
        self.driver.get(self.url)
        common.print("Step :: Check count in cart and if 0 cart should be empty.")
        cart_count = common.text(Locators.TEXT_CART_COUNT)
        common.print("cart count : " + cart_count)

        if cart_count == "0":
            common.print("Step :: Click on cart icon from top right corner of page.")
            common.click(Locators.BTN_CART_ICON)
            common.pause()
            common.print("Step :: Verify cart should be empty.")
            empty_message = common.text(Locators.TEXT_EMPTY_MESSAGE)
            common.pause()
            assert "empty" in empty_message
