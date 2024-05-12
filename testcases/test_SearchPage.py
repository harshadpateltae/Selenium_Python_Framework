import time
import pytest
from pageObjects.all_Locators import Locators
from utilities.common import Common
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup", "log_on_failure")
class TestSearchPage:
    url = ReadConfig.getCommonInfo("baseURL")
    logger = LogGen.loggen()

    def test_verify_shop_by_brand_in_camera_section(self):
        common = Common(self.driver)
        common.print("Step :: Open URL : " + self.url)
        self.driver.get(self.url)
        common.print("Step :: Click on electronics menu.")
        common.click(Locators.ELECTRONICS_TOP_MENU)
        common.print("Step :: Mouse hover to audio sub menu.")
        common.move_to_element(Locators.AUDIO_SUB_MENU)
        common.print("Step :: Click on any brand from speaker brand column.")
        total_brands = common.len(Locators.ALL_SHOP_BY_BRAND)
        index = common.random_number_integer(1, total_brands)
        selected_brand = common.text(Locators.ALL_SHOP_BY_BRAND, index).lower()
        common.click(Locators.ALL_SHOP_BY_BRAND, index)
        common.print("Step :: Verify all products displays for selected brand.")
        common.pause()
        total_products = common.len(Locators.TEXT_SEARCH_PAGE_PRO)
        for i in range(1, total_products):
            assert selected_brand in common.text(Locators.TEXT_SEARCH_PAGE_PRO, i).lower()

    def test_verify_customer_review_filter(self):
        common = Common(self.driver)
        common.print("Step :: Open URL : " + self.url)
        self.driver.get(self.url)
        common.print("Step :: Click on mobiles sub menu.")
        common.click(Locators.MOBILES_TOP_MENU)
        common.print("Step :: CLick on any review option to filter.")
        count = common.len(Locators.ALL_STAR_REVIEW)
        index = common.random_number_integer(1, count)
        review_filter = common.get_attribute(Locators.ALL_STAR_REVIEW, "aria-label", index)
        selected = review_filter.split(" ")
        common.print("Star rating selected for filter : " + selected[0])
        selected_star = float(selected[0])
        common.click(Locators.ALL_STAR_REVIEW, index)
        common.print("Step :: Verify all products displays after filter having 4 star & above star ratings.")
        count = common.len(Locators.ALL_PRODUCT_STARS)
        for i in range(1, count):
            review_text = common.get_attribute(Locators.ALL_PRODUCT_STARS, "aria-label", i)
            reviews = review_text.split("out")
            common.print("Star rating of product " + str(i) + " is : " + reviews[0])
            stars = float(reviews[0])
            assert stars >= selected_star, "Reviews filter not working properly."

    def test_find_samsung_brand_mobile_phone_via_drawer_menu(self):
        common = Common(self.driver)
        common.print("Step :: Open URL : " + self.url)
        self.driver.get(self.url)
        common.print("Step :: Click on all button from top left corner of page.")
        common.click(Locators.BTN_ALL_MENU)
        common.print("Step :: Click on mobile computers menu.")
        common.click(Locators.LINK_MOBILE_COMPUTERS)
        common.print("Step :: Click on all mobiles phones menu.")
        common.pause()
        common.click_javascript(Locators.LINK_ALL_MOBILE_PHONES)
        common.print("Step :: Check samsung brand check box.")
        common.pause()
        common.click_javascript(Locators.CHKBOX_SAMSUNG)
        common.print("Step :: Verify all product displays after search are fsrom samsung brand.")
        common.pause()
        product_count = common.len(Locators.TEXT_SEARCH_PAGE_PRODUCT)
        for i in range(1, product_count):
            product_name_search_page = common.text(Locators.TEXT_SEARCH_PAGE_PRODUCT, i).lower()
            assert "samsung" in product_name_search_page

    def test_search_product_and_add_to_cart(self):
        global product_name
        common = Common(self.driver)
        common.print("Step :: Open URL : " + self.url)
        self.driver.get(self.url)
        product_to_search = "Apple iPhone 15"
        common.print("Step :: Enter " + product_to_search + " in search textbox.")
        common.send_keys(Locators.TXB_SEARCH_BOX, product_to_search)
        common.print("Step :: Click on submit button.")
        common.click(Locators.BTN_SUBMIT)
        common.print(
            "Step :: Verify searched product displayed on list page and if displayed click on add to cart button.")
        total_searched = common.len(Locators.TEXT_LISTPAGE_PRODUCT)

        is_product_added = False
        for i in range(1, total_searched):
            product_name = common.text(Locators.TEXT_LISTPAGE_PRODUCT, i)
            if product_to_search.lower() in product_name.lower():
                count_atc = common.text(Locators.TEXT_CART_COUNT)
                common.print("Step :: Click on add to cart button.")
                common.click(Locators.BTN_LISTPAGE_ATC, i)
                time.sleep(2)
                common.print("Step :: Verify product count increased by 1 in cart.")
                count_atc_after = common.text(Locators.TEXT_CART_COUNT)
                assert int(count_atc) + 1 == int(count_atc_after), "Product not added in cart, Please check the issue."
                is_product_added = True
                break

        if is_product_added:
            common.print("Step :: Click on cart logo on top right corner of page.")
            common.click(Locators.BTN_CART_ICON)
            common.print("Step :: Verify selected product present in cart.")
            product_in_cart = len(common.wait_until_elements_to_be_visible(Locators.TEXT_PRODUCT_NAME_CART))
            is_product_in_cart = False
            for j in range(1, product_in_cart):
                product_name_in_cart = common.text(Locators.TEXT_PRODUCT_NAME_CART, j)
                if product_name.lower() in product_name_in_cart.lower():
                    is_product_in_cart = True
                    break

            if not is_product_in_cart:
                common.print("Selected product not added in cart, please check the issue.")
            else:
                common.print("Selected product added in cart successfully.")
