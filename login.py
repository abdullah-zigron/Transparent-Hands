import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://th.zigron.com/")
        # self.assertIn("Python", driver.title)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[@id='header-top-second']/div[2]/a").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[@id='user_login']").send_keys("hafiz.abdullah@zigron.com")
        self.driver.find_element_by_xpath("//*[@id='user_pass']").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='login_btn']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_link_text('LOGOUT').click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
