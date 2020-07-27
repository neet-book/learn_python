from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from Fetch import get_chara_skill


start = datetime.now()
path = '/Users/erika/File/python/crawler/chromedriver'
opt = Options()
opt.add_argument('--headless')
driver = webdriver.Chrome(executable_path=path, chrome_options=opt)

driver.get('https://pcredivewiki.tw/Character/Detail/%E9%9C%9E')

print(driver.title)

#  爬取技能数据
# skill_info = get_chara_skill(driver)
# print(skill_info)

driver.close()

end = datetime.now()
print(end - start)



