from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

HOST = input("请输入被测服务器ip：")

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.server_url = 'http://' + HOST
        # print(cls.server_url)

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == HOST:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
