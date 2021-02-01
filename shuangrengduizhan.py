# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import uiautomator2 as u2
import time
import os

from mysqlpy import getAns
from util import GetKeyValue
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

d = u2.connect('192.168.50.218')
print(d.info)
d(text='我的', className='android.widget.TextView').click()
d(text='我要答题', className='android.widget.TextView').click()
d.xpath(
    "//android.view.View[@text='挑战对抗磨练答题技能']/following-sibling::android.view.View/following-sibling::android.view.View/following-sibling::android.view.View").click()
# d.xpath("//android.view.View[@text='随机匹配']/following-sibling::android.view.View").click()
time.sleep(1)
d.click(552 + 465 / 2, 816 + 480 / 2)
i = 0
while i <= 5:
    try:
        info_content = str(d.xpath("//android.widget.ListView/preceding-sibling::android.view.View[1]").get_text())
        option_elements = d.xpath(
            "//android.widget.ListView//android.widget.RadioButton/following-sibling::android.view.View[1]").all()
        options_A = str(d.xpath(
            "//android.widget.ListView//android.widget.RadioButton/following-sibling::android.view.View[1]").get_text())
        res = getAns(info_content, 1, options_A)
        option = res[0]
        choose = str(res[1]).replace("[", "").replace("]", "").replace("\"", "").split(',')
        if option == 'A':
            option_elements[0].click()
        elif option == 'B':
            option_elements[1].click()
        elif option == 'C':
            option_elements[2].click()
        elif option == 'D':
            option_elements[3].click()
        i = i + 1
        time.sleep(3)
    except Exception:
        if len(option_elements) > 0:
            option_elements[0].click()
            i = i + 1
            time.sleep(3)
        continue
print("答题完成,返回一次")
d.xpath("//android.view.View[@text='继续挑战']").click()
time.sleep(1)
d.keyevent("back")
ctx = d.watch_context()
ctx.when("退出").click()
ctx.wait_stable()  # 等待界面不在有弹窗了
ctx.stop()
d.keyevent("back")
d.keyevent("back")
os.system("python zhengshangyou.py")
