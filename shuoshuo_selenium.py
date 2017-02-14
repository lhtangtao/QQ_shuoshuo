#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name   = shuoshuo_selenium
#author = tangtao
#time   = 2017/2/14 15:39
#Description=添加描述信息
#eMail   =tangtao@lhtangtao.com
#git     =lhtangtao
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓      ┏┓
┏┛┻━━━┛┻┓
┃      ☃      ┃
┃  ┳┛  ┗┳  ┃
┃      ┻      ┃
┗━┓      ┏━┛
┃      ┗━━━┓
┃  神兽保佑    ┣┓
┃　永无BUG！   ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫  ┃┫┫
┗┻┛  ┗┻┛
"""

import json
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
from selenium import webdriver
import time

# 使用selenium
driver = webdriver.Chrome()
driver.maximize_window()


# 登录QQ空间
def get_shuoshuo(src_qq, dest_qq):
    """
    获取src_qq的所有说说并且保存到haha.json上。请确保登录了dest_qq
    :param src_qq:
    :param dest_qq:
    :return:
    """
    driver.get('http://user.qzone.qq.com/{}/311'.format(src_qq))
    time.sleep(2)
    driver.find_element_by_id('login_div')
    driver.switch_to.frame('login_frame')
    driver.find_element_by_id("img_out_" + str(dest_qq)).click()
    time.sleep(5)
    driver.switch_to.frame('app_canvas_frame')
    last_page = int(driver.find_element_by_xpath(".//*[@id='pager_last_0']/span").text)
    i = 0
    while i < last_page:
        # 以下指的是说说里的数据
        content = driver.find_elements_by_css_selector('.content')
        stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
        likes = driver.find_elements_by_css_selector(".c_tx.comment_btn")
        for con, sti, like in zip(content, stime, likes):
            data = {
                u'内容': con.text,
                u"评论数": like.text,
                u'时间': sti.text
            }
            with open('haha.json', "a+") as f:
                f.write('\n')
                json.dump([data], f, ensure_ascii=False)
        time.sleep(2)
        if int(i) + 1 != last_page:
            xpath = ".//*[@id='pager_next_" + str(i) + "']/span"
            driver.find_element_by_xpath(xpath).click()
        i += 1
        time.sleep(3)
    print("==========完成================")
    driver.quit()


if __name__ == '__main__':
    get_shuoshuo('670076298', "670076298")
