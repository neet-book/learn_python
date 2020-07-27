import re
s_ks = [{'skill_name': '罪惡牢籠', 'skill_type': '必殺技', 'description': '必殺技\n罪惡牢籠\n以前方第３名敵人為中心，展開使範圍內的敵人大幅度降低魔法防禦力，並小幅度降低ＴＰ上升的領域，且小幅度降低行動速度。'}, {'skill_name': '束縛之徑', 'skill_type': '技能1', 'description': '技能1\n束縛之徑\n對前方範圍內的全體敵人造成小幅度的魔法傷害，並且施加束縛。'}, {'skill_name': '束縛之徑+', 'skill_type': '專武強化技能1', 'description': '專武強化技能1\n束縛之徑+\n對前方範圍內的全體敵人造成小幅度的魔法傷害，並且施加束縛。依照範圍內敵人的數量，提升束縛的時間。'}, {'skill_name': '誤導之彈', 'skill_type': '技能2', 'description': '技能2\n誤導之彈\n對面前的１名敵人造成小幅度的魔法傷害，並且使其混亂。'}, {'skill_name': '偵探智慧', 'skill_type': 'EX技能', 'description': 'EX技能\n偵探智慧\n戰鬥開始時，中幅度提升自己的魔法防禦力。'}, {'skill_name': '偵探智慧+', 'skill_type': 'EX技能+', 'description': 'EX技能+\n偵探智慧+\n戰鬥開始時，大幅度提升自己的魔法防禦力。'}]

for s_k in s_ks:
    str = re.sub(r'(EX)?技能[1-3]?\+?|必殺技|\n','', s_k['description'])
    str.replace(s_k['skill_name'], '')
