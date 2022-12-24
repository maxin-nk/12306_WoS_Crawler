## 爬取旧版的页面
# 实现爬取的操作

from splinter import Browser
import time
import math
import numpy as np
import pandas as pd
import random
from citaton import paqu_citation
user_agent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
executable_path = {'executable_path':r'C:\Users\dell\Downloads\Compressed\chromedriver.exe'}
browser = Browser(driver_name='chrome',user_agent=random.choice(user_agent), **executable_path)
js = 'window.scrollTo(0,document.body.clientHeight)'  #scroll
js2 = 'window.scrollTo(0,document.body.scrollHeight)'
js3 = 'window.scrollTo(0,0)'


def download_file(browser, option):
    if option == 0:
        time.sleep(2)
        k = 1
        for ith in range(2):
            try:
                browser.find_by_xpath("//app-records-list[@class='app-records-list']"
                                      "/app-record[1]/div[2]/div[1]/app-summary-title/h3/a").click()
                break
            except:
                if ith != 1:
                    gundong(k,browser)
                    k += 2
                    time.sleep(0.5)
                else:
                    print('未找到第一篇文章')
    else:
        for ii in range(3):
            time.sleep(1)

            for ith in range(2):
                try:
                    browser.find_by_xpath('//*[@id="FullRecSnRecListtop"]/app-export-menu/div/button').click()
                    break
                except:
                    if ith == 0:
                        time.sleep(2)
                    else:
                        browser.back()
                        return False, browser.url

            time.sleep(1)

            for ith in range(3):
                try:
                    browser.find_by_xpath('//*[@id="exportToExcelButton"]').click()
                    break
                except:
                    if ith == 2:
                        browser.back()
                        return False, browser.url
                    else:
                        time.sleep(2)

            time.sleep(2)

            for ith in range(2):
                try:
                    browser.find_by_xpath('// *[@id = "FullRecordExportToEnwOptionContentover"] / button').click()
                    break
                except:
                    if ith == 1:
                        browser.back()
                        return False, browser.url
                    else:
                        time.sleep(2)

            time.sleep(1)
            for ith in range(2):
                try:
                    browser.find_by_xpath('// *[@id = "global-select"] / div / div[2] / div[3]').click()
                    break
                except:
                    if ith == 1:
                        browser.back()
                        return False, browser.url
                    else:
                        time.sleep(2)

            time.sleep(0.5)

            browser.find_by_xpath('// *[@id = "FullRecordExportToEnwBtnover"]').click()
            time.sleep(3)
            try:
                if browser.find_by_xpath('// *[@id = "FullRecordExportToEnwBtnover"]').first.visible and ii != 1:
                    # 表示点那个×
                    browser.find_by_xpath('/html/body/app-wos/div/div/main/app-input-route/'
                                      'app-export-overlay/div/div[3]/div[1]/button').click()
                    browser.reload()
                    time.sleep(2)
                else:
                    if browser.find_by_xpath('// *[@id = "FullRecordExportToEnwBtnover"]').first.visible:
                        if ii == 2:
                            return False, browser.url, browser
                        else:
                            # 表示点那个×
                            browser.find_by_xpath('/html/body/app-wos/div/div/main/app-input-route/'
                                                  'app-export-overlay/div/div[3]/div[1]/button').click()
                            #　这块就把页面关掉，重新进入这个页面
                            url_l = [browser.url].copy()
                            browser.quit()
                            time.sleep(0.5)
                            browser = Browser(driver_name='chrome', user_agent=random.choice(user_agent), **executable_path)
                            browser.visit(url_l[0])
                            wait(browser)
            except:
                break
        print('success')
        return True, browser.url, browser


def Sousuo(qikan, browser):
    # 搜索指定期刊
    button1 = browser.find_by_xpath('//*[@id="searchrow1"]/td[2]/span/span[1]/span/span[2]/b')
    button1.click()
    # 点击出版物名称
    browser.find_by_xpath('//*[@id="searchrow1"]/td[2]/span/span[1]/span/span[2]/b').click()
    time.sleep(0.1)
    browser.find_by_xpath('//*[@id="select2-select1-result-46xo-SO"]').click()
    time.sleep(0.5)
    browser.find_by_xpath('//*[@id="value(input1)"]').fill(qikan)
    browser.find_by_xpath('//*[@id="timespan"]/div[2]/div/span/span[1]/span/span[2]/b').click()
    browser.find_by_xpath('//*[@id="timespan"]/div[2]/div/select/option[2]').click()
    time.sleep(0.1)
    browser.find_by_xpath('//*[@id="searchCell1"]/span[1]/button').click()
    time.sleep(2)
    browser.find_by_xpath('//*[@id="global-select"]/div/div[2]/div[5]').click()
    browser.find_by_xpath('//*[@id="snSearchType"]/div[2]/app-search-row/div[1]/div[2]/input').fill('2016-2020')
    time.sleep(2)
    browser.find_by_xpath('//*[@id="snSearchType"]/div[4]/button[2]').click()


def wait(browser):
    for _ in range(1):
        try:
            time.sleep(2)
            browser.find_by_xpath('//*[@id="pendo-button-747973e0"]').click()
            time.sleep(2)
            browser.find_by_xpath('// *[@id = "pendo-button-6f487453"]').click()
            time.sleep(2)
            browser.find_by_xpath('//*[@id="pendo-button-c8a19033"]').click()
            time.sleep(2)
            try:
                browser.find_by_xpath("//*[@id='pendo-button-506b4382']").click()  # //*[@id='pendo-close-guide-dc656865']
            except:
                print('no thanks')
        except:
            time.sleep(2)
        time.sleep(1)
        try:
            browser.find_by_xpath("//*[@id='pendo-button-506b4382']").click()  # //*[@id='pendo-close-guide-dc656865']
        except:
            break
        try:
            browser.find_by_xpath('// *[ @ id = "pendo-button-4b0c6f06"]').click()
        except:
            break
        try:
            browser.find_by_xpath('//*[@id="pendo-close-guide-3ba5cee4"]').click()
        except:
            break

def gundong(c,browser):
    js = 'window.scrollTo(0,' + str(c) + '*document.body.clientHeight)'
    browser.execute_script(js)
    time.sleep(0.8)


def paqu(browser):
    for ith in range(2):
        try:
            panduan, url_l, browser = download_file(browser, 1)
            break
        except:
            if ith == 0:
                gundong(1, browser)
    if not panduan:
        URL_L.append(url_l)  # 没有查到的
        print(url_l)
    # 跳到下一个界面
    for _ in range(2):
        try:
            browser.find_by_xpath('/html/body/app-wos/div/div/main/div/app-input-route/'
                              'app-full-record-home/div[1]/app-page-controls/div/form/div/button[2]').click()
            break
        except:
            browser.reload()
    time.sleep(0.5)
    print('第%d页面' % (each_page + 1))
    return browser


if __name__ == '__main__':
    URL_L = []
    data = None
    qikans = ['APPLIED CATALYSIS B-ENVIRONMENTAL']    # 'ENERGY & ENVIRONMENTAL SCIENCE','PROGRESS IN ENERGY AND COMBUSTION SCIENCE'
    for qikan in qikans:
        url = 'http://apps.webofknowledge.com/UA_GeneralSearch_input.do;jsessionid=061436460110923349C91D2893466382?' \
              'product=UA&search_mode=GeneralSearch&SID=8FLo8MVWhysPeWVIqfM&preferencesSaved='
        browser.visit(url)   # 访问首页
        browser.driver.maximize_window()
        for ith in range(4):
            try:
                #　搜素指定期刊
                Sousuo(qikan, browser)
                break
            except:
                if ith != 2:
                    wait(browser)
                    browser.driver.maximize_window()
        # TEST
        # hrl_b = 'https://www.webofscience.com/wos/alldb/summary/1dbb60b9-da2d-4cb9-99f4-b1fbcbec4fad-01b6a65b/relevance/1'
        # browser.visit(hrl_b)
        # 获取页数
        time.sleep(1)

        ys = browser.find_by_xpath('/html/body/app-wos/div/div/main/div/app-input-route/app-base-summary-component/'
                                   'app-search-friendly-display/div[1]/app-general-search-friendly-display/h1/span').text
        ys = int(ys.replace(',', ''))
        wait(browser)
        if qikan == 'APPLIED CATALYSIS B-ENVIRONMENTAL':  #　Effects of the promotion with bismuth and lead on direct synthesis of light olefins from syngas over carbon nanotube supported iron catalysts
            jiezhi = 11
        else:
            jiezhi = 0
        # 先点进去第一篇文献
        url1 = browser.url
        download_file(browser, 0)  # 表示点进去
        for each_page in range(jiezhi, ys):
            # 爬取文章标题
            try:
                title = browser.find_by_xpath('//*[@id="FullRTa-fullRecordtitle-0"]').text
            except:
                time.sleep(0.2)
                print('未爬到标题信息')
                title = browser.find_by_xpath('//*[@id="FullRTa-fullRecordtitle-0"]').text
            # 爬取每一篇的citation
            try:
                YJFX, WBOS, TITLE = paqu_citation(browser)
            except:
                time.sleep(0.5)
                print('再爬取一次')
                browser.driver.close()
                browser = Browser(driver_name='chrome', user_agent=random.choice(user_agent), **executable_path)
                browser.visit(url1)
                browser.driver.maximize_window()
                download_file(browser, 0)  # 表示点进去
                # 翻页
                try:
                    browser.find_by_id("snNextPageTop").fill(str(each_page + 1))
                except:
                    wait(browser)
                    browser.driver.maximize_window()
                    print('输入页码失败，再输入一次')
                    try:
                        browser.find_by_id("snNextPageTop").fill(str(each_page + 1))
                    except:
                        # 一个个点
                        wait(browser)
                        browser.driver.maximize_window()
                        for _ in range(each_page):
                            browser.find_by_xpath('/html/body/app-wos/div/div/main/div/app-input-route/app-full-record-home/div[1]/'
                                                  'app-page-controls/div/form/div/button[2]').click()
                            time.sleep(0.1)

                time.sleep(0.1)
                e2 = browser.find_by_id('FullRTa-fullRecordtitle-0')
                try:
                    e2.click()
                except Exception:
                    e2 = browser.find_by_id('FullRTa-fullRecordtitle-0')
                    time.sleep(0.2)
                    e2.click()
                time.sleep(0.5)
                YJFX, WBOS, TITLE = paqu_citation(browser)
            title11 = pd.DataFrame([title]*len(TITLE),columns=['title'])
            TITLE11 = pd.DataFrame(TITLE,columns=['cited_title'])
            YJFX1 = pd.DataFrame(YJFX)
            YJFX11=pd.concat([YJFX1,pd.DataFrame(np.zeros([YJFX1.shape[0],10-YJFX1.shape[1]]))],axis=1)
            WBOS1 = pd.DataFrame(WBOS)
            WBOS11=pd.concat([WBOS1,pd.DataFrame(np.zeros([WBOS1.shape[0],10-WBOS1.shape[1]]))],axis=1)
            if data is None:
                data = pd.concat([title11, TITLE11, YJFX11, WBOS11],axis=1)
                data.columns = ['title','cited_title']+list(range(20))
            else:
                new_data = pd.concat([title11, TITLE11, YJFX11, WBOS11],axis=1)
                new_data.columns = ['title','cited_title']+list(range(20))
                data = pd.concat([data,new_data],axis=0)
            # 爬完之后回到第一个文献的位置
            try:
                browser.find_by_xpath('// *[ @ id = "breadcrumb"] / ul / li[3] / a / span').click()  # 点到第一个文献的位置
            except:
                browser.reload()
                browser.find_by_xpath('// *[ @ id = "breadcrumb"] / ul / li[3] / a / span').click()  # 点到第一个文献的位置
                print('重新点击第一个文献的位子')
            # browser.visit(url1)
            # download_file(browser, 0)
            time.sleep(0.5)
            if each_page % 10 == 0 and each_page != 0:
                data.to_excel('citation' + str(each_page // 100) + '.xls')
                data = None
                print('success,%d' % each_page)
            browser.find_by_id("snNextPageTop").fill(str(each_page+2))
            # 翻页
            time.sleep(0.5)
            e2 = browser.find_by_id('FullRTa-fullRecordtitle-0')
            try:
                e2.click()
            except Exception:
                e2 = browser.find_by_id('FullRTa-fullRecordtitle-0')
                e2.click()
            time.sleep(0.5)


# 保存数据
data.to_excel('citation_end.xls')

# import pickle
# with open('citation.pkl', 'wb') as f1:
#     pickle.dump(data, f1)
