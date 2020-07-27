import re

def get_chara_skill(driver):
    skill_boxs = driver.find_elements_by_class_name('skill-box')
    chara_skells = []
    for s_b in skill_boxs:
        skill = {}

        skill['skill_name'] = s_b.find_element_by_class_name('skill-name').text
        skill['skill_type'] = s_b.find_element_by_class_name('skill-type').text

        skill['description'] = s_b.find_element_by_class_name('skill-description').text
        skill['description'] = re.sub(r'(EX)?技能[1-3]?\+?|必殺技|\n','', skill['description'])
        skill['description'] = skill['description'].replace(skill['skill_name'], '')

        skill['skill_effect'] = []
        skill_effects = s_b.find_elements_by_css_selector('.skill-effect > .mb-2')
        for s_e in skill_effects:
            s_e_divs = s_e.find_elements_by_tag_name('div')
            e_txt = ''
            for div in s_e_divs:
                if div.text == '' or div.text == ' ':
                    e_txt += div.text
            
            skill['skill_effect'].append(e_txt)

        chara_skells.append(skill)
    return chara_skells

def get_chara_info(driver):
   table =  driver.find_element_by_class_name('chara-table')
   tr_list = driver.find_elements_by_tag_name('tr')
   info = {}
   for tr in tr_list:
