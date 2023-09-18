import json
import copy
import uuid
import random
def load_json_data(path): #读取json数据
    with open(path, "r", encoding='utf-8') as f:
        # 读取 JSON 数据
        data = json.load(f)
        copydata=copy.deepcopy(data)
        f.close()
    return data,copydata

def write_json_data(copydata,path): #写入json数据
    with open(path, "w", encoding='utf-8') as f:
        json.dump(copydata,f)
        f.close()


def Obtain_all_orbital_data_material_id(data,tabulation:list,types,dicks:dict): #获取types所指定的类型频道数据
    for j in data["tracks"]:
        if j["type"] == types:
            for i in j["segments"]:
                if i["material_id"] in dicks.keys() or  i["material_id"] in dicks.values(): #判断音频地址是否有对应的字幕地址
                    tabulation.append(i)

def Channerl_sort(tabulation:list,types1,types2=None): #根据types的数据排序列表
    if types2 !=None:
        tabulation.sort(key=lambda x :  x[f"{types1}"][f"{types2}"])
    else:
        tabulation.sort(key=lambda x :  x[f"{types1}"])

def construction_addition(copydata:list,tabulation,types):
    
    copyaddtion={
            "attribute": 0,
            "flag": 0,
            "id": str(uuid.uuid4()),
            "is_default_name": "true",
            "name": "",
            "segments": tabulation,
            "type": f"{types}"
        }
    copydata["tracks"].append(copyaddtion)
    


def Add_to_start(path1,path2): 
    temp=load_json_data(path=path1)
    audio_setof=[]
    text_setof=[]
    data=temp[0]
    Subtitletoaudio={} # 音频地址:字幕地址
    copydata=temp[1]
    delTrackproject=[]
    materid_setof=[j["material_id"] for i in data["tracks"] if i["type"] == 'audio' for j in i["segments"]]
    for i in data["materials"]["audios"]:
        for j in materid_setof:
            if i["id"]==j and i["type"]=="text_to_audio":
                Subtitletoaudio.update({i["text_id"]:j})
                delTrackproject.append(i["text_id"])
                delTrackproject.append(j)
    
    Obtain_all_orbital_data_material_id(data,tabulation=audio_setof,types="audio",dicks=Subtitletoaudio)
    Obtain_all_orbital_data_material_id(data,tabulation=text_setof,types="text",dicks=Subtitletoaudio)
    Channerl_sort(audio_setof,"target_timerange","start")
    is_first_iteration = True
    for i in audio_setof: 
        if is_first_iteration:
            tempstart = i["target_timerange"]['start']
            tempduration=i["target_timerange"]['duration']
            is_first_iteration = False
            continue
        i["target_timerange"]['start']=tempduration+tempstart
        tempstart = i["target_timerange"]['start']
        tempduration=i["target_timerange"]['duration']
    
    for i in text_setof:
        for j in audio_setof:
            if j["material_id"] == Subtitletoaudio[i["material_id"]]:
                i["target_timerange"]['start']=j["target_timerange"]['start']
                i["target_timerange"]['duration']=j["target_timerange"]['duration']
                break
    for i in delTrackproject:
        for j in copydata["tracks"]:
            j["segments"] = [z for z in j["segments"] if z["material_id"] != i]

    
    construction_addition(copydata=copydata,tabulation=audio_setof,types="audio")
    construction_addition(copydata=copydata,tabulation=text_setof,types="text")
    copydata["tracks"] = [track for track in copydata["tracks"] if track["segments"]]
    write_json_data(path=path2,copydata=copydata)


    
Add_to_start(path1="D:\\JianyingPro Drafts\\9月16日\\draft_content.json",path2="D:\\JianyingPro Drafts\\9月16日\\draft_content.json")