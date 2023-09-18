import json
import copy
import uuid


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
def Obtain_all_orbital_data_material_id(data,tabulation:list,types,dicks:dict): #获取types所指定的类型频道数据
    for j in data["tracks"]:
        if j["type"] == types:
            for i in j["segments"]:
                if i["material_id"] in dicks.keys() or  i["material_id"] in dicks.values(): #判断音频地址是否有对应的字幕地址
                    tabulation.append(i)

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

def Obtain_all_orbital_data(data,tabulation:list,types): #获取types所指定的类型频道数据
    for j in range(0,len(data["tracks"])):
        if data["tracks"][j]["type"] == types: #获取类型 判断音频轨道类型
            dataSummary=data["tracks"][j]["segments"] # 得到所有的轨道数据
            timelens = len(dataSummary)
            for i in range(0,timelens):
                tabulation.append(data["tracks"][j]["segments"][i]["target_timerange"]|{"number":j}|{"numlist":i}) #遍历轨道中所有数据的trget_timerange类型


def remove_Channel(copydata,types): #删除types指定的节点保留一个
    numat = [i for i, track in enumerate(copydata["tracks"]) if track["type"] == types]

    if len(numat) > 1:
            del_indices = numat[1:]
            del_indices.reverse()  # 倒序遍历删除索引，避免索引改变导致删除错误的元素
            for i in del_indices:
                del copydata["tracks"][i]
    if len(numat) > 0:
        copydata["tracks"][numat[0]]["segments"] = []  # 对第一个元素进行操作

def Find_the_first_index(copydata,types):
    
    numat = [i for i in range(len(copydata["tracks"])) if copydata["tracks"][i]["type"] == types]
    return numat[0]

def Channerl_sort(tabulation:list,types1=None,types2=None): #根据types的数据排序列表
    if types2 !=None:
        tabulation.sort(key=lambda x :  x[f"{types1}"][f"{types2}"])
    else:
        tabulation.sort(key=lambda x :  x[f"{types1}"])



def Add_after_modification(data,tabulation:list,tabulation2:list,funstype=None): #根据音频和字幕的轨道对齐字幕
    is_first_iteration=False
    tempstart = 0 
    tempduration = 0 
    if funstype==None:
        for i in tabulation:
            if is_first_iteration:
                tempstart= i["duration"]
                tempduration=i["start"]
                is_first_iteration = False
                continue
            i["start"]=tempstart+tempduration
            tempstart=i["duration"]
            tempduration=i["start"]
            data["tracks"][i["number"]]["segments"][i["numlist"]]["target_timerange"]["duration"]=i["duration"]
            data["tracks"][i["number"]]["segments"][i["numlist"]]["target_timerange"]["start"]=i["start"]
        try:
            for i in range(len(tabulation)):
                data["tracks"][tabulation2[i]["number"]]["segments"][tabulation2[i]["numlist"]]["target_timerange"]["duration"]=tabulation[i]["duration"]
                data["tracks"][tabulation2[i]["number"]]["segments"][tabulation2[i]["numlist"]]["target_timerange"]["start"]=tabulation[i]["start"]
        except:
            pass
    elif funstype== 'Aitexttospeech':
        for i in tabulation: 
            if is_first_iteration:
                tempstart = i["target_timerange"]['start']
                tempduration=i["target_timerange"]['duration']
                is_first_iteration = False
                continue
            i["target_timerange"]['start']=tempduration+tempstart
            tempstart = i["target_timerange"]['start']
            tempduration=i["target_timerange"]['duration']

def update_data_material_id(text_setof, audio_setof, Subtitletoaudio, delTrackproject, copydata):
    for i in text_setof:
        for j in audio_setof:
            if j["material_id"] == Subtitletoaudio[i["material_id"]]:
                i["target_timerange"]["start"] = j["target_timerange"]["start"]
                i["target_timerange"]["duration"] = j["target_timerange"]["duration"]
                break
    for i in delTrackproject:
        for j in copydata["tracks"]:
            j["segments"] = [z for z in j["segments"] if z["material_id"] != i]
         
def Add_to_final_data(copydata,data,tabulation:list,first_data): #将修改好后的data添加到copydata
    for i in tabulation:
        copydata["tracks"][first_data]["segments"].append(data["tracks"][i["number"]]["segments"][i["numlist"]])

def process_data(data,Subtitletoaudio,delTrackproject):
    materid_setof = [j["material_id"] for i in data["tracks"] if i["type"] == "audio" for j in i["segments"]]
    for i in data["materials"]["audios"]:
        for j in materid_setof:
            if i["id"] == j and i["type"] == "text_to_audio":
                Subtitletoaudio.update({i["text_id"]: j})
                delTrackproject.append(i["text_id"])
                delTrackproject.append(j)



def Add_to_start(path):
    Trackdatatimes= []
    Subtitletrack=[]
    
    temp=load_json_data(path=path)
    
    data=temp[0]
    
    copydata=temp[1]

    Obtain_all_orbital_data(data,Trackdatatimes,"audio")
    
    Obtain_all_orbital_data(data,Subtitletrack,"text")
    remove_Channel(copydata=copydata,types='audio')
    remove_Channel(copydata=copydata,types='text')
    try:
        first_audio = Find_the_first_index(copydata,'audio')
        first_text = Find_the_first_index(copydata,'text')
    except:
        return ["FALSE_audio","抱歉你的轨道中没有音频\n或者缺少至少一个的字幕"]
    Channerl_sort(Trackdatatimes,types1="start")
    
    Channerl_sort(Subtitletrack,types1="start")
    
    Add_after_modification(data,Trackdatatimes,Subtitletrack)
    
    Add_to_final_data(copydata,data,Trackdatatimes,first_audio)
    
    Add_to_final_data(copydata,data,Subtitletrack,first_text)
    
    write_json_data(path=path,copydata=copydata)
    return ["TURE"]

def Align_only_Ai_voice_and_text(path):
    
    temp=load_json_data(path=path)

    audio_setof=[]

    text_setof=[]

    data=temp[0]

    Subtitletoaudio={} # 音频地址:字幕地址

    copydata=temp[1]

    delTrackproject=[]

    process_data(data,Subtitletoaudio,delTrackproject)

    Obtain_all_orbital_data_material_id(data,tabulation=audio_setof,types="audio",dicks=Subtitletoaudio)

    Obtain_all_orbital_data_material_id(data,tabulation=text_setof,types="text",dicks=Subtitletoaudio)

    Channerl_sort(audio_setof,"target_timerange","start")

    Add_after_modification(data=data,tabulation=audio_setof,tabulation2=text_setof,funstype="Aitexttospeech")

    update_data_material_id(text_setof=text_setof,audio_setof=audio_setof,Subtitletoaudio=Subtitletoaudio,delTrackproject=delTrackproject,copydata=copydata)

    construction_addition(copydata=copydata,tabulation=audio_setof,types="audio")

    construction_addition(copydata=copydata,tabulation=text_setof,types="text")

    copydata["tracks"] = [track for track in copydata["tracks"] if track["segments"]]

    write_json_data(path=path,copydata=copydata)
    return ["TURE"]