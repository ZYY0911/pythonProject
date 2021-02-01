import uiautomator2 as u2
import time
import os
from uiautomator2 import Direction


d = u2.connect('192.168.50.218')
print("开始阅读文章")
# d.click(980,2080)
# time.sleep(2)
# d.xpath("//*[@resource-id='cn.xuexi.android:id/general_card_title_id']").click()
# d.xpath("//*[@resource-id='cn.xuexi.android:id/view_pager']/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.TextView")
# for el in d.xpath('//*[contains(name(), "ImageView")]').all():
#         print("rect:", el.rect) # output tuple: (left_x, top_y, width, height)
#         print("bounds:", el.bounds) # output tuple: （left, top, right, bottom)
#         print("center:", el.center())
#         print(el.attrib) # 输出lxml解析出来的Node
# d.xpath("//*[@resource-id='cn.xuexi.android:id/home_bottom_tab_icon_large']").click()//学习
# d.xpath("//*[@resource-id='cn.xuexi.android:id/img_search_left']").click()#搜索
# d.set_fastinput_ime(True) # 切换成FastInputIME输入法
# d.send_keys("唐诗三百首") # adb广播输入
# d.set_fastinput_ime(False) # 切换成正常的输入法
# d.send_action("search") # 模拟输入法的搜索

# d(text='我的', className='android.widget.TextView').click()


d.xpath("电台").click()
d.xpath("听广播").click()
d.xpath("中国之声").click()
d.xpath("//*[@resource-id='cn.xuexi.android:id/home_bottom_tab_icon_large']").click()  # 学习
d.xpath("北京").click()
time.sleep(2)
d.xpath("北京学习平台").click()
print("本地学习平台停留15秒")
time.sleep(15)
d.keyevent("back")
d.xpath("要闻").click()
time.sleep(3)
for j in range(2):
    el = d.xpath('//*[@resource-id="cn.xuexi.android:id/general_card_title_id"]').all()
    msgTitle = el[j].info.get("text")
    d.xpath(msgTitle).click()
    time.sleep(2)
    d.swipe_ext(Direction.FORWARD)
    d.xpath("//android.widget.TextView[@text='欢迎发表你的观点']").click()
    d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
    d.send_keys("习近平同玻利维亚总统阿尔塞通电话,习近平听取贺一诚述职报告")  # adb广播输入
    d.set_fastinput_ime(False)  # 切换成正常的输入法
    d.send_action("search")  # 模拟输入法的搜索
    time.sleep(2)
    d.xpath("//android.widget.TextView[@text='发布']").click()
    time.sleep(1)
    d.xpath("//android.widget.TextView[@text='删除']").click()
    time.sleep(3)
    d.xpath("//android.widget.Button[@text='确认']").click()
    d.xpath("//android.widget.TextView[@text='欢迎发表你的观点']/following-sibling::android.widget.ImageView[1]").click()
    d.xpath("//android.widget.TextView[@text='欢迎发表你的观点']/following-sibling::android.widget.ImageView[2]").click()
    time.sleep(1)
    d.xpath("//android.widget.TextView[@text='分享到学习强国']").click()
    d.keyevent("back")
    d.keyevent("back")
print("完成点赞，分享，评论")
d.xpath("北京").click()
time.sleep(5)
befortitle = ""
i = 0
while i <= 6:
    try:
        d.swipe_ext("up", scale=0.3)
        time.sleep(1)
        el = d.xpath('//*[@resource-id="cn.xuexi.android:id/general_card_title_id"]').all()
        msgTitle = el[1].info.get("text")
        if befortitle == msgTitle:
            el[2].info.get("text")
        else:
            d.xpath(msgTitle).click()
            time.sleep(20)
            print("20秒")
            d.swipe_ext(Direction.FORWARD)
            time.sleep(20)
            print("40秒")
            d.swipe_ext(Direction.FORWARD)
            time.sleep(25)
            print("65秒")
            print("学习完" + msgTitle)
        befortitle = msgTitle
        i = i + 1
        d.keyevent("back")
    except Exception:
        print("阅读失败")
        continue
print("学习完六篇文章")
d.xpath("电视台").click()
d.xpath("联播频道").click()
time.sleep(5)
d.swipe_ext("up", scale=0.4)
befortitle = ""
i = 0
while i <= 6:
    try:
        d.swipe_ext("up", scale=0.3)
        time.sleep(1)
        el = d.xpath('//*[@resource-id="cn.xuexi.android:id/general_card_title_id"]').all()
        msgTitle = el[1].info.get("text")
        if befortitle == msgTitle:
            el[2].info.get("text")
        else:
            d.xpath(msgTitle).click()
            time.sleep(10)
            print("10秒")
            d.swipe_ext(Direction.FORWARD)
            time.sleep(10)
            print("20秒")
            d.swipe_ext(Direction.FORWARD)
            time.sleep(15)
            print("35秒")
            print("学习完" + msgTitle)
        befortitle = msgTitle
        i = i + 1
        d.keyevent("back")
    except Exception:
        print("阅读失败")
        continue
print("学习完六个视频")
d.app_stop('cn.xuexi.android')
