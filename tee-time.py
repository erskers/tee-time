import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class TeeTime:
    def __init__(self, golf_id, password, golf_buddies, courses, time):
        self.golf_buddies = golf_buddies
        self.password = password
        self.golf_id = golf_id
        self.time = time
        self.courses = courses
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.implicitly_wait(30)

    def teardown_method(self):
        self.driver.quit()

    def _login(self):
        # Login step
        self.driver.get("https://mingolf.golf.se/Login?ReturnUrl=%2F")
        self.driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll').click()
        self.driver.find_element(By.ID, 'txtGolfID').send_keys(self.golf_id)
        self.driver.find_element(By.ID, 'txtPassword').send_keys(self.password)
        self.driver.find_element(By.ID, 'btnLogin').click()

    def _pick_golf_buddies(self):
        self.driver.find_element(By.CLASS_NAME, 'home-action').click()
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Välj golfvän')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Visa fler (6)')]").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".btn-show-more:nth-child(17) > .show-more-text").click()
        print("HERE")
        for buddie in self.golf_buddies:
            self.driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(buddie)).click()
        self.driver.find_element(By.ID, "btnBookingContinue").click()

    def _pick_courses(self):
        self.driver.find_element(By.LINK_TEXT, "Ingen bana är vald").click()
        for course in self.courses:
            self.driver.find_element(By.XPATH, "//*[contains(text(), 'GolfStar - {}')]".format(course)).click()

        self.driver.find_element(By.ID, "btnBookingContinue").click()

    def _time_and_date_picker(self):
        self.driver.find_element(By.XPATH, "//*[@data-date='20220417']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-prev").click()
        self.driver.find_element(By.CSS_SELECTOR, ".search-view-when-times-body").click()
        self.driver.find_element(By.CSS_SELECTOR, ".search-view-when-times-body").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-next > .icon").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-next > .icon").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-next > .icon").click()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-next > .icon").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-next > .icon")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".swiper-button-next > .icon").click()
        self.driver.find_element(By.LINK_TEXT, self.time).click()
        self.driver.find_element(By.ID, "btnBookingContinue").click()

    def find_available_teetimes(self) -> str:
        self._login()
        self._pick_golf_buddies()
        self._pick_courses()
        self._time_and_date_picker()

        self.driver.find_element(By.LINK_TEXT, "Visa lediga tider").click()
        available_tee_times = self.driver.find_element(By.XPATH, "//div[@class='teetimes-child available-times']").text
        return available_tee_times

class ArgParser:
     def __init__(self, argv):
         self.golf_buddies = argv[3:]
         self.password = argv[2]
         self.golf_id = argv[1]


if __name__ == "__main__":
    '''
    Expecting input arguments:
    1. golf_id (format yymmdd-xxx)
    2. password
    3. golf_buddies (format buddie_1 buddie_2 ...)
     
    '''
    tee_time_conf = ArgParser(sys.argv)

    lets_go = TeeTime(tee_time_conf.golf_id, tee_time_conf.password, tee_time_conf.golf_buddies,
                      ["Kungsängen Kings", "Kungsängen Queens", "Brollsta", "Kyssinge", "Lindö Dal", "Waxholm"],
                      "11.00")

    available_tee_times = lets_go.find_available_teetimes()
    print(available_tee_times)
