# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from editing import Editing

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_edit_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False}, firefox_binary="C:/Program Files/Mozilla Firefox 52.9.0/firefox.exe")
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username="admin", password="secret"):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def edit_contact(self, wd, editing):
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[8]/td[8]/a/img").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(editing.company)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(editing.mobile)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(editing.address2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(editing.notes)
        # submit contact deletion
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def test_edit_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.edit_contact(wd, Editing(company="asdfg", mobile="89257788625", address2="erty", notes="5"))
        self.return_to_home_page(wd)
        self.logout(wd)


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
