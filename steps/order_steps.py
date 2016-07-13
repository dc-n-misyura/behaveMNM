

@step('I navigate to the DC Home page')
def open_home_page(self):
    # open home page
    wd = self.driver
    wd.get("http://www.delivery-club.ru/")

@step('I login')
def login(self, Login):
    wd = self.app.driver
    wd.find_element_by_link_text("Вход / Регистрация").click()
    wd.find_element_by_name("c_l").click()
    wd.find_element_by_name("c_l").clear()
    wd.find_element_by_name("c_l").send_keys(Login.login)
    wd.find_element_by_name("c_p").click()
    wd.find_element_by_name("c_p").clear()
    wd.find_element_by_name("c_p").send_keys(Login.password)
    wd.find_element_by_link_text("ВОЙТИ").click()
    time.sleep(2)
    self.app.open_profile_page()
    time.sleep(2)

@step('I see profile screen')
def assert_balls(self):
    wd = self.driver
    wd.find_elements_by_id("user-points")

@step('I adding new address')
def add_new_address(self, new_address):
    wd = self.driver
    wd.find_element_by_id("user-addr__input").click()
    wd.find_element_by_id("user-addr__input").clear()
    wd.find_element_by_id("user-addr__input").send_keys(new_address)
    wd.find_element_by_link_text(new_address).click()
    wd.find_element_by_css_selector("a.user-addr__submit.sbm-btn").click()
    time.sleep(2)
    wd.find_element_by_css_selector("span.user-profile__span").click()
    time.sleep(2)

@step('Delete this address')
def delete_first_address(self):
    wd = self.driver
    wd.find_element_by_css_selector("a.delete_uaddress").click()
    time.sleep(2)
    alert = wd.switch_to_alert()
    time.sleep(2)
    alert.accept()
    time.sleep(5)

@step('I see old address list')
def assert_title_profile(self):
    wd = self.driver
    wd.find_element_by_xpath("//div[@class='card_address']//h1[.='Мои адреса']")
    wd.find_element_by_css_selector("h1")

@step('I comeback to the DC Home Page')
def open_home_page(self):
    # open home page
    wd = self.driver
    wd.get("http://www.delivery-club.ru/")

@step('I input in search new address')
def find_by_address_from_home_page(self, new_address):
    wd = self.driver
    wd.find_element_by_id("user-addr__input").click()
    wd.find_element_by_id("user-addr__input").clear()
    wd.find_element_by_id("user-addr__input").send_keys(new_address)
    wd.find_element_by_css_selector("a.user-addr__submit.sbm-btn").click()
    time.sleep(5)


@step('Click by result vendors')
def open_vendor_from_search(self, title):
    wd = self.driver
    wd.find_element_by_id("fast_search_rest_input").click()
    wd.find_element_by_id("fast_search_rest_input").send_keys(title)
    time.sleep(1)
    wd.get("http://www.delivery-club.ru/srv/Tanuki/#Volgogradskij_prospjekt/Sushhjevskij_Val")
    time.sleep(2)

@step('I see vendor-page')
def assert_vendor_page(self):
    wd = self.driver
    wd.find_element_by_xpath("//h2[@id='anchor_test']//b[.='Популярное']")
    wd.find_element_by_link_text("Инфо").click()
    wd.find_element_by_css_selector("h1")
    wd.find_element_by_link_text("Отзывы 4929").click()
    wd.find_element_by_link_text("Меню").click()

@step('I order product')
def ordering_products(self):
    wd = self.driver
    wd.find_element_by_css_selector("i.quantity").click()
    wd.find_element_by_css_selector("a.inc").click()
    wd.find_element_by_css_selector("a.inc").click()
    wd.find_element_by_css_selector("a.inc").click()
    wd.find_element_by_css_selector("a.inc").click()
    wd.find_element_by_css_selector("a.done").click()
    time.sleep(3)

@step('Open Basket')
def open_cart(self):
    wd = self.driver
    wd.find_element_by_xpath("//div[@id='middle']/div[3]/a[2]").click()

@step('Open Checkout-Screen')
def open_checkout(self):
    wd = self.driver
    wd.find_element_by_link_text("ОФОРМИТЬ ЗАКАЗ").click()
    time.sleep(3)

@step('I see checkout')
def assert_checkout(self):
    wd = self.driver
    wd.find_element_by_name("tel_number_change")

