from selenium.webdriver.common.by import By


class Locators:
    TXB_SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    BTN_SUBMIT = (By.XPATH, "//span[@id='nav-search-submit-text']//input")
    TEXT_CART_COUNT = (By.ID, "nav-cart-count")
    BTN_CART_ICON = (By.ID, "nav-cart")
    BTN_LISTPAGE_ATC = (By.XPATH, "(//button[text()='Add to cart'])")
    TEXT_LISTPAGE_PRODUCT = (By.XPATH, "(//span[@class='a-size-medium a-color-base a-text-normal'])")
    TEXT_SEARCH_PAGE_PRODUCT = (By.XPATH, "(//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4'])")
    TEXT_PRODUCT_NAME_CART = (By.XPATH, "(//span[@class='a-truncate-cut'])")
    TEXT_SEARCH_PAGE_PRO = (By.XPATH, "(//span[@class='a-size-base-plus a-color-base a-text-normal'])")
    BTN_ALL_MENU = (By.ID, "nav-hamburger-menu")
    LINK_MOBILE_COMPUTERS = (By.XPATH, "//a//div[text()='Mobiles, Computers']")
    CHKBOX_SAMSUNG = (By.XPATH, "//input[@aria-labelledby='Samsung']")
    LINK_ALL_MOBILE_PHONES = (By.XPATH, "//a[text()='All Mobile Phones']")
    TEXT_EMPTY_MESSAGE = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']//h2")
    MOBILES_TOP_MENU = (By.XPATH, "//div[@id='nav-xshop']//a[text()='Mobiles']")
    ELECTRONICS_TOP_MENU = (By.XPATH, "//div[@id='nav-xshop']//a[text()=' Electronics ']")
    AUDIO_SUB_MENU = (By.XPATH, "//span[@class='nav-a-content'][contains(text(),'Audio')]")
    ALL_STAR_REVIEW = (By.XPATH, "(//a//div[contains(@aria-label,' & Up')])")
    ALL_SHOP_BY_BRAND = (By.XPATH, "(//div[contains(@style,'display: block;')]//div[@class='mm-column']//h3[text()='Speaker brands']/following-sibling::ul//a)")
    ALL_PRODUCT_STARS = (By.XPATH, "(//div[@class='a-section a-spacing-none a-spacing-top-micro']//span[contains(@aria-label,'stars')])")
