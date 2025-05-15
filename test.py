import json



file_path=r"C:\internship\data\dataset\train1_data.json"

with open(file_path,encoding="utf-8") as f:
    cases=json.load(f)

result_list=[]
for case in cases:
    text=case["case_report"]+'\n'+case["test_results"]
    tag=["ORPHA:"+case["Orpha_id"]]
    result_list.append([text,tag])

file_path=r"C:\internship\data\dataset\train1_data_reduced.json"
with open(file_path,"w",encoding="utf-8") as f:
    json.dump(result_list, f, ensure_ascii=False, indent=4)
