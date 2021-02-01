import uiautomator2 as u2
import time
import os
from mysqlpy import getAns
def model():
    j = 0
    while j <= 5:
        time.sleep(1)
        type_question = str(d.xpath("//*[@text='填空题' or @text='单选题'or @text='多选题']").get_text())
        print(type_question)
        if type_question == "填空题":
            d.xpath("//android.view.View[@text='查看提示']").click()
            time.sleep(0.5)
            tips = d.xpath(
                "//android.view.View[@text='提示']/../following-sibling::android.view.View[1]/android.view.View").get_text()
            print(tips)
            d.xpath("//android.view.View[@text='提示']/following-sibling::android.view.View[1]").click()
            content = d.xpath("//android.widget.EditText/../../android.view.View").get_text()
            print(content)
            d.xpath("//android.widget.EditText/../android.view.View").click()
            d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
            time.sleep(2)
            aun = str(tips).split(content)
            try:
                d.send_keys(aun[1])  # adb广播输入
            except Exception:
                d.send_keys("a")
            finally:
                d.set_fastinput_ime(False)  # 切换成正常的输入法
                d.send_action("next")  # 模拟输入法的搜索
                d.xpath('//*[@text="确定" or @text="下一题" or @text="完成"]').click()
        elif type_question == "单选题":
            info_content = str(d.xpath("//android.widget.ListView/preceding-sibling::android.view.View[1]").get_text())
            option_elements = d.xpath(
                "//android.widget.ListView//android.widget.RadioButton/following-sibling::android.view.View[1]").all()
            options_A = str(d.xpath(
                "//android.widget.ListView//android.widget.RadioButton/following-sibling::android.view.View[1]").get_text())
            res = getAns(info_content, 10, options_A)
            option = res[0]
            if option == 'A':
                option_elements[0].click()
            elif option == 'B':
                option_elements[1].click()
            elif option == 'C':
                option_elements[2].click()
            elif option == 'D':
                option_elements[3].click()
            d.xpath('//*[@text="确定" or @text="下一题" or @text="完成"]').click()
        else:
            info_content = str(d.xpath("//android.widget.ListView/preceding-sibling::android.view.View[1]").get_text())
            print(info_content)
            option_elements = d.xpath(
                "//android.widget.ListView/android.view.View/android.view.View/android.view.View[2]").all()
            opt_num = len(option_elements)
            k = 0
            for opt in option_elements:
                option_elements[k].click()
                k = k + 1
            d.xpath('//*[@text="确定" or @text="下一题" or @text="完成"]').click()
            # else:
            #     d.xpath("//android.view.View[@text='查看提示']").click()
            #     time.sleep(0.5)
            #     tips = d.xpath(
            #     "//android.view.View[@text='提示']/../following-sibling::android.view.View[1]/android.view.View").get_text()
            #     print(tips)
        time.sleep(1)
        j = j + 1
        if d.xpath("//android.view.View[@text='答案解析']").exists:
            print("111111111")
            d.xpath('//*[@text="确定" or @text="下一题" or @text="完成"]').click()

d = u2.connect('192.168.50.218')
print(d.info)
d(text='我的', className='android.widget.TextView').click()
d(text='我要答题', className='android.widget.TextView').click()
d.xpath("每日答题").click()
model()
sorce = d.xpath("//android.view.View[starts-with(@text, '+')]").get_text()
if  sorce!="5":
    model()
else:
    os.system("python readermodel.py")

