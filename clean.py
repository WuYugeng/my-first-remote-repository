#清洗数据
import json

file_name=r"temp.txt"
with open(file_name, 'r', encoding='utf-8') as f:
    cases = json.load(f)

result_list = []
for case in cases:
    raw_result=case[0]
    tag=case[1]
    lines=raw_result.split("\n")
    HPO_list=[line[:10] for line in lines[1:]]
    result_list.append([HPO_list,tag])

file_name=r"C:\internship\codes\timgroup_disease_diagnosis-main\codes\core\data\preprocess\patient\CCRD_OMIM_ORPHA\custom\clinphen_test_set.json"
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(result_list, f, ensure_ascii=False, indent=4)