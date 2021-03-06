import json
from pprint import pprint
from datetime import datetime
import xml.etree.ElementTree as ET
class json_top():

    def top_words(self,some_list):
        temp_list = []
        temp_dic = {} 
        for item in some_list:
            temp_list = list(filter(lambda x: len(x)>=6, item))
            for word in temp_list:
                word = word.lower()
                if word not in temp_dic:
                    temp_dic[word] = 1
                else :
                    temp_dic[word] += 1  
        return temp_dic              
    def json_read(self):

        temp_list = []
        self.file_dic = json.load(self.file)
        list_items = self.file_dic["rss"]["channel"]["items"]
        for item in list_items:
            temp_list.append(item["description"].split())
        temp_dic = self.top_words(temp_list)    
        return list(sorted(temp_dic.items(),key = lambda item: -item[1]))[:10]
        
    def xml_read(self): 
        temp_list = []
        parser = ET.XMLParser(encoding = "utf-8")
        tree = ET.parse(self.file, parser)    
        root = tree.getroot()
        channel = root.find("channel")
        items = channel.findall("item")
        for item in items:
            description = item.find("description")
            temp_list.append(description.text.split())
        temp_dic = self.top_words(temp_list)

        return list(sorted(temp_dic.items(),key = lambda item: -item[1]))[:10]    


    def error_log(self, exc_type, exc_val, exc_tb):
        with open("./file.txt", 'w', encoding="utf-8") as er:
            er.write(f"При выполнени возникла ошибка {exc_type} \n {exc_val} \n {exc_tb} ")
    def __init__(self,file_path,encod_type="utf-8"):
        self.start_work = datetime.now()
        self.format_name = file_path.split(".")[-1]
        self.file = open(file_path,encoding=encod_type)
        self.top = self.format_type[self.format_name](self)
   
    def __enter__(self):
        return self    
    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_type is not None:
            self.error_log(exc_type,exc_val,exc_tb)
        self.end_work = datetime.now()
        self.file.close()

    format_type = {
        'json' : json_read,
        'xml' : xml_read
    }

with json_top("./newsafr.json") as f:
    pprint(f.top)
print(f"Начало работы {f.start_work}\n Конец Работы {f.end_work}\n В работе{f.end_work - f.start_work}") 
print("="*40)
with json_top("./newsafr.xml") as f:
    pprint(f.top)
print(f"Начало работы {f.start_work}\n Конец Работы {f.end_work}\n В работе{f.end_work - f.start_work}") 