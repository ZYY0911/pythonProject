# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import uiautomator2 as u2
import time

from mysqlpy import getAns

ziparr = ["A", "B", "C", "D"]

d = u2.connect('192.168.50.218')
print(d.device_info)
d.app_start('cn.xuexi.android')
d(text='我的', className='android.widget.TextView').click()
# d(text='学习积分', className='android.widget.TextView').click()
d(text='我要答题', className='android.widget.TextView').click()
d.xpath("//android.view.View[@text='挑战对抗磨练答题技能']/following-sibling::android.view.View/following-sibling::android.view.View//following-sibling::android.view.View//following-sibling::android.view.View").click()
j = 0
while j <= 6:
    try:
        info_content = str(d.xpath("//android.widget.ListView/preceding-sibling::android.view.View[1]").get_text())
        print(info_content)
        options = []
        option_elements = d.xpath("//android.widget.ListView//android.widget.RadioButton/following-sibling::android.view.View[1]").all()
        res = getAns(info_content, 0,"")
        option = res[0]
        if j == 6:
            index = ziparr.index(option)
            index = index + 1
            index = index + 1 if index == len(ziparr) else index
            print("答题完成，设置偏移量")
            option = ziparr[index]
        if option == 'A':
            option_elements[0].click()
        elif option == 'B':
            option_elements[1].click()
        elif option == 'C':
            option_elements[2].click()
        elif option == 'D':
            option_elements[3].click()
        if d.xpath("//*[@text='分享就能复活']").exists and j != 6:
            d.xpath("//android.view.View[@text='分享就能复活']").click()
            d.keyevent("back")
            print("回答错误")
            time.sleep(2)
        else:
            print("回答正确")
            j = j + 1
            time.sleep(1)
    except Exception:
        time.sleep(2)
        continue
    finally:
        print(j)
time.sleep(2)
if d.xpath("//android.view.View[@text='结束本局']").exists:
    d.xpath("//android.view.View[@text='结束本局']").click()
    time.sleep(1)
d.keyevent("back")
time.sleep(1)
d.keyevent("back")
time.sleep(1)
d.keyevent("back")
time.sleep(1)
import os
os.system("python shuangrengduizhan.py")
