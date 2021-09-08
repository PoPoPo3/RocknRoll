# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(
            executable_path='./chromedriver.exe'
        )
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_cash_order_k_r_d(self):
        driver = self.driver
        # max window size
        driver.maximize_window()
        # open site
        driver.get("https://rocknrolls23.ru/")
        # start shoping
        driver.find_element_by_link_text(u"Меню").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='c'])[10]/following::span[2]").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'https://cdn9.arora.pro/d/upload/scale/94/0/2/b67d32aa-d14f-4f3c-8160-9dadfd9511e7/group//4d2389b7-b769-4ad0-bcdb-a8b90070c197.png')]").click()
        driver.find_element_by_xpath("//div[3]/div/div[3]/div[6]/a/i").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/header/div[3]/div[2]/div[2]/div[2]/p[1]/a").click()
        driver.find_element_by_xpath("/html/body/div[2]/header/div[3]/div[2]/div[2]/div[2]/div[1]/div/a[2]").click()
        driver.find_element_by_id("orderDeny").click()
        # start order
        driver.find_element_by_xpath("//form[@id='base_info']/div[2]").click()
        driver.find_element_by_id("order_phone").clear()
        driver.find_element_by_id("order_phone").send_keys("+79999999999")
        driver.find_element_by_xpath("//div[@id='courier-delivery-form']/div/h3").click()
        driver.find_element_by_id("order_comment").click()
        driver.find_element_by_id("order_comment").clear()
        driver.find_element_by_id("order_comment").send_keys(u"ТЕСТ НЕ ГОТОВИТЬ")


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except 55 as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):

        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
