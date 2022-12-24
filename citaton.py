import time


def wait(browser):
    browser.driver.maximize_window()
    for _ in range(2):
        time.sleep(1)
        try:
            browser.find_by_xpath('//*[@id="pendo-button-747973e0"]').click()
            time.sleep(0.1)
            browser.find_by_xpath('// *[@id = "pendo-button-6f487453"]').click()
            time.sleep(0.1)
            browser.find_by_xpath('//*[@id="pendo-button-c8a19033"]').click()
            time.sleep(0.1)
            try:
                browser.find_by_xpath("//*[@id='pendo-button-506b4382']").click()  # //*[@id='pendo-close-guide-dc656865']
            except:
                print('no thanks')
        except:
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
def gundong(c, browser):
    js = 'window.scrollTo(0,' + str(c) + '*document.body.clientHeight)'
    browser.execute_script(js)
    time.sleep(0.1)


def tiqu(text1, browser, address):
    each = 1
    yjfx = []
    while True:
        item_text = browser.find_by_xpath(address+'[' + str(each) + ']').text
        each += 1
        if item_text != '':
            yjfx.append(item_text)
            if text1.find(item_text) + len(item_text) == len(text1):  # 说明找到最后一个了
                break  # 停止
    return yjfx


def paqu_citation(browser):
    data, YJFX, WBOS,TITLE = [],[],[],[]
    try:
        gs = browser.find_by_xpath('//*[@id="FullRRPTa-wos-citation-network-refCountLink"]').text
    except:
        wait(browser)
        print('未找到参考文献数量对于的链接')
        try:
            gs = browser.find_by_xpath('//*[@id="FullRRPTa-wos-citation-network-refCountLink"]').text
        except:
            return [],[],[]
    browser.find_by_xpath('//*[@id="FullRRPTa-wos-citation-network-refCountLink"]').click()
    time.sleep(0.1)
    # 点进去第一个参考文献
    try:
        browser.find_by_xpath(
            '//*[@id="FRMiniCrlTa-snMcrl"]/div/app-records-list/app-record[1]/div[2]/div[1]/app-summary-title/h3/a').click()
    except:
        wait(browser)
        try:
            browser.find_by_xpath(
                '//*[@id="FRMiniCrlTa-snMcrl"]/div/app-records-list/app-record[1]/div[2]/div[1]/app-summary-title/h3/a').click()
        except:  # 说明第一个点不进去，就换一个
            for ith in range(2,10):
                try:
                    browser.find_by_xpath(
                        '//*[@id="FRMiniCrlTa-snMcrl"]/div/app-records-list/app-record['+str(ith)+']/div[2]/div[1]/app-summary-title/h3/a').click()
                    break
                except:
                    print('没有点到参考文献界面')
                if ith == 9:
                    print('没爬到数据')
                    return [],[],[]
    time.sleep(0.1)
    for each_page in range(0, int(gs)):
        #　研究方向提取
        for finder in range(1,10):
            try:  # 如果没有找到的话，那就是没有该信息，就跳过
                if '研究方向' in browser.find_by_xpath('//*[@id="snJournalData"]/div[1]/div['+str(finder)+']').text:
                    biaoji = False
                    break
            except:
                # 翻页
                wait(browser)
                try:
                    browser.find_by_xpath('/html/body/app-wos/div/div/main/div/app-input-route/app-full-record-home/div[1]/'
                                      'app-page-controls/div/form/div/button[2]/span[1]').click()
                    time.sleep(0.5)
                except:
                    return [],[],[]
                biaoji = True
                break
        if biaoji:
            continue
        #　文章标题提取
        time.sleep(0.1)
        title = browser.find_by_xpath('// *[ @ id = "FullRTa-fullRecordtitle-0"]').text
        TITLE.append(title)
        gundong(1, browser)
        while True:
            text1 = browser.find_by_xpath('//*[@id="snJournalData"]/div[1]/div['+str(finder)+']').text
            gundong(1, browser)
            time.sleep(0.1)
            if text1 != '':
                break
            else:
                print('没提出来文本信息')
        address = '//*[@id="snJournalData"]/div[1]/div['+str(finder)+']/span'
        try:
            yjfx = tiqu(text1, browser, address)
        except:
            wait(browser)
            yjfx = tiqu(text1, browser, address)
        YJFX.append(yjfx)
        # web of science 类别提取
        for finder in range(1,10):
            try:  # 如果没有找到的话，那就是没有该信息，就跳过
                if 'Web of Science 类别' in browser.find_by_xpath('//*[@id="snJournalData"]/div[1]/div['+str(finder)+']').text:
                    address2 = '//*[@id="snJournalData"]/div[1]/div[' + str(finder) + ']/span'
                    text2 = browser.find_by_xpath(
                        '// *[ @ id = "snJournalData"] / div[1] / div[' + str(finder) + ']').text
                    wbos = tiqu(text2, browser, address2)
                    WBOS.append(wbos)
                    break
            except:
                WBOS.append([])
                break
        # 翻页
        try:
            browser.find_by_xpath('/html/body/app-wos/div/div/main/div/app-input-route/app-full-record-home/div[1]/'
                              'app-page-controls/div/form/div/button[2]/span[1]').click()
            time.sleep(0.5)
        except Exception:
            wait(browser)
            browser.find_by_xpath('/html/body/app-wos/div/div/main/div/app-input-route/app-full-record-home/div[1]/'
                              'app-page-controls/div/form/div/button[2]/span[1]').click()
            time.sleep(0.5)
    return YJFX, WBOS, TITLE




