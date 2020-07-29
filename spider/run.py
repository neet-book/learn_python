import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from Fetch import get_chara_skill, get_chara_info, get_act_pattern


pro_path = os.path.abspath('./')
path = os.path.join(pro_path, 'chromedriver')
cache_dir = os.path.join(pro_path, 'cache')

opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-plugin')
opt.add_argument('--disable-images')
opt.add_argument(f'--disk-cache-dir={cache_dir}')

try:
    start = datetime.now()
    driver = webdriver.Chrome(executable_path=path, chrome_options=opt)
    driver.get('https://pcredivewiki.tw/Character/Detail/%E9%9C%9E')
    print(driver.title)
    
    #  爬取技能数据
    # skill_info = get_chara_skill(driver)
    # print(skill_info)

    # 爬取角色信息
    # chara_info = get_chara_info(driver)
    # print(chara_info)

    act_pattern = get_act_pattern(driver)
    print(act_pattern)

    end = datetime.now()
    print(end - start)

finally:
    driver.quit()
