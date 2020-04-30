#!usr/bin/env python3
#-*- coding:utf-8 -*-

#THIS FILE IS ONLY USED FOR STUDY SHARING
#clear_cart.py - MAIN PART OF THE PROJECT
#
#THE PROJECT IS A FREE SOFTWARE
#PLEASE GIVE Copyright IF USING
#
#Copyright © 2020 By arcovegle. All rights reserved.

'''
@time:2020-04-29
@author:arcovegle(aRc0v3gle)
'''

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import datetime

desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "eager"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://cart.taobao.com/")
driver.implicitly_wait(5)

def checktime(time):
    while True:
        if datetime.datetime.now().__ge__(datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')):
            break

def buy_all():
    while True:
        try:
            actions = ActionChains(driver)
            actions.click(driver.find_element_by_css_selector(btn_select))
            actions.move_to_element(driver.find_element_by_css_selector(btn_pay))
            actions.click(driver.find_element_by_css_selector(btn_pay))
            actions.perform()
            break
        except:
            continue

def order():
     while True:
        try:
            if driver.find_element_by_css_selector(btn_order):
                driver.find_element_by_css_selector(btn_order).click()
                break
        except:
            continue

def pay_by_pwd(pwd):
    while True:
        try:
            if driver.find_element_by_css_selector(input_pwd):
                driver.find_element_by_css_selector(input_pwd).send_keys(pwd)
                break
        except:
            continue
    while True:
        try:
            if driver.find_element_by_css_selector(btn_submit):
                driver.find_element_by_css_selector(btn_submit).click()
                break
        except:
            continue

if __name__ == "__main__":
    sale_time = input("Input the sale time(YY-mm-dd HH:MM:SS):")
    pay_pwd = input("Input your pay password:")
    btn_select='#J_SelectAll1 > div.cart-checkbox > label'
    btn_pay='#J_FloatBar > div.float-bar-wrapper > div.float-bar-right > div.btn-area > a.submit-btn'
    btn_order='#submitOrderPC_1 > div.wrapper > a.go-btn'
    input_pwd='#payPassword_container > input'
    btn_submit='#J-rcSubmit > div > input'
    checktime(sale_time)
    buy_all()
    order()
    pay_by_pwd(pay_pwd)
    print("Purchase done.")
