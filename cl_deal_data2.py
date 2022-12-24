# 实现爬取的操作
from bei import *
import pickle


def xiazai(browser):
    time.sleep(1)
    browser.find_by_xpath('//*[@id="snRecListTop"]/app-export-menu/div/button').click()
    time.sleep(1)
    browser.find_by_xpath('//*[@id="exportToExcelButton"]').click()
    time.sleep(1)
    browser.find_by_xpath('//*[@id="radio3"]/label/span[1]').click()
    time.sleep(1)
    browser.find_by_xpath('/html/body/app-wos/div/div/main/app-input-route/app-export-overlay'
                          '/div/div[3]/div[2]/app-export-out-details/div/div[2]/div/div[1]/wos-select/button').click()
    time.sleep(0.2)
    try:
        browser.find_by_xpath('//*[@id="global-select"]/div/div[2]/div[3]').click() # 点击获取全文
        time.sleep(0.3)
        browser.find_by_xpath('/html/body/app-wos/div/div/main/app-input-route/'
                              'app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/div/div[2]/button[1]').click()
        time.sleep(2)
        return True
    except:
        browser.find_by_xpath('/html/body/app-wos/div/div/main/app-input-route/'
                              'app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/div/div[2]/button[2]').click()
        time.sleep(2)
        return False
if __name__ == '__main__':
    qikans = ['APPLIED CATALYSIS B-ENVIRONMENTAL']    # 'ENERGY & ENVIRONMENTAL SCIENCE','PROGRESS IN ENERGY AND COMBUSTION SCIENCE'
    for qikan in qikans:
        # jicao(browser,qikan)
        browser.visit('https://www.webofscience.com/wos/alldb/summary/4500fc3a-397e-44d0-8f97-94783683ba13-09e29e96/relevance/1')
        browser.driver.maximize_window()
        start = input('准备开始')
        ys = browser.find_by_xpath('/html/body/app-wos/div/div/main/div/app-input-route/app-base-summary-component/'
                                   'app-search-friendly-display/div[1]/app-general-search-friendly-display/h1/span').text
        ys = int(ys.replace(',', ''))
        wait(browser)
        # 先点进去第一篇文献
        # download_file(browser, 0)  # 表示点进去
        loss_data = []
        TITLE = []
        kk = 0.5
        kg = 1
        for each_page in range(2377, ys):  # 269
            shu = each_page % 50 + 1
            # 判断是否翻页
            if kg == 1:
                kg = 0
                for _ in range(each_page//50):
                    # 翻页
                    try:
                        browser.find_by_xpath('/html/body/app-wos/div/div/main/div/app-input-route/app-base-summary-component/'
                                              'div/div[2]/app-page-controls[1]/div/form/div/button[2]').click()
                        time.sleep(0.5)
                    except:
                        wait(browser)
                        browser.find_by_xpath(
                            '/html/body/app-wos/div/div/main/div/app-input-route/app-base-summary-component/'
                            'div/div[2]/app-page-controls[1]/div/form/div/button[2]').click()
            # 爬取文章标题
            while True:
                try:
                    titile = browser.find_by_xpath('/html/body/app-wos/div/div/main/div/app-input-route/app-base-summary-component/'
                                          'div/div[2]/app-records-list/app-record['+str(shu)+']/div[2]/div[1]/app-summary-title/h3/a').text
                    TITLE.append(titile)
                    break
                except:
                    gundong(kk, browser)
                    kk += 0.25
                if kk > 50*0.25+0.5:
                    kk = 0.5
            # 点参考文献
            try:
                browser.find_by_xpath('/html/body/app-wos/div/div/main/div/app-input-route/app-base-summary-component/div/div[2]'
                                      '/app-records-list/app-record['+str(shu)+']/div[3]/div/div[1]/div[2]/a').click()
            except:
                wait(browser)
                try:
                    browser.find_by_xpath(
                        '/html/body/app-wos/div/div/main/div/app-input-route/app-base-summary-component/div/div[2]'
                        '/app-records-list/app-record[' + str(shu) + ']/div[3]/div/div[1]/div/a').click()
                except:
                    print('没有参考文献，直接跳过')
                    continue
            time.sleep(1)
            for ee in range(3):
                try:
                    panduan = xiazai(browser)
                    break
                except:
                    browser.reload()
                    wait(browser)
                    gundong(0.25, browser)
                if ee == 2:
                    panduan = False
            if panduan is False:
                print('没有全文记录')
                loss_data.append(titile)
                TITLE.pop(TITLE.index(titile))
            for each_wait in range(10):
                try:
                    time.sleep(1)
                    browser.find_by_id('mat-input-0').click()
                except:
                    break
                if each_wait == 7:
                    browser.reload()
                    wait(browser)
                    time.sleep(1)
                    browser.find_by_xpath('/html/body/app-wos/div/div/main/app-input-route/'
                                          'app-export-overlay/div/div[3]/div[2]/app-export-out-details/div/div[2]/div/div[2]/button[1]').click()
                    time.sleep(3)
                if each_wait == 9:
                    # 证明下载失败了
                    print('没下载下来')
                    loss_data.append(titile)
                    TITLE.pop(TITLE.index(titile))
                    browser.find_by_xpath(
                        "/html/body/app-wos/div/div/main/app-input-route/app-export-overlay/div/div[3]/div[1]/button").click()
                    time.sleep(1)
            # 退回
            try:
                browser.find_by_xpath('//*[@id="breadcrumb"]/ul/li['+str(each_page//50+1)+']/a').click()
            except:
                browser.back()
            time.sleep(1)
            if shu == 50:  # 表示最后一个爬完了
                # 翻页
                gundong(0.25, browser)
                try:
                    browser.find_by_xpath('/html/body/app-wos/div/div/main/div/app-input-route/app-base-summary-component/'
                                          'div/div[2]/app-page-controls[1]/div/form/div/button[2]').click()
                except:
                    wait(browser)
                    browser.find_by_xpath(
                        '/html/body/app-wos/div/div/main/div/app-input-route/app-base-summary-component/'
                        'div/div[2]/app-page-controls[1]/div/form/div/button[2]').click()
                kk = 0.5
                with open('TITLE' + str(each_page // 50) + '.pkl', 'wb') as f1:
                    pickle.dump(TITLE, f1)
                    TITLE = []
            print('finish', each_page)