from clinphen import main
from typing import List
import json


def get_HPO_list(text:str)->List[str]:
    with open("./temp.txt", 'w', encoding='utf-8') as file:
        file.write(text)
    result=main(inputFile="./temp.txt",
         custom_thesaurus="",
         rare=False)
    result_list=result.split('\n')
    HPO_list=[elem[:10] for elem in result_list[1:]]
    return HPO_list


if __name__=="__main__":
    result_list=[]
    file_path = r"C:\internship\data\test_set\test_data_reduced.json"
    with open(file_path, encoding="utf-8") as f:
        cases = json.load(f)
    i=0
    for text,tag in cases:
        result_list.append([get_HPO_list(text),tag])
        print(i)
        i+=1
    file_path=r"C:\internship\data\test_set\test_data_clinphen.json"
    with open(file_path, 'w',encoding="utf-8") as f:
        json.dump(result_list, f, ensure_ascii=False, indent=4)


