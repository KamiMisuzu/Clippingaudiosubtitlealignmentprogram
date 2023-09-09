import json
import copy
def start(path):
    try:
        Tracktimerecording = 0  # 记录校正长度
        Tracktimecorrection = 0  # 记录校正开始
        Trackdatatimes = []
        Subtitletrack = []
        with open(path, "r", encoding='utf-8') as f:
            # 读取 JSON 数据
            data = json.load(f)
            copydata=copy.deepcopy(data)
            f.close()
        number=0
        guidao=len(data["tracks"])
        # with open("D:\\JianyingPro Drafts\\9月6日 (4)\\draft_content.json", "w+", encoding='utf-8') as f:
        for j in range(0,guidao):
            if data["tracks"][j]["type"] == "audio": #获取类型 判断音频轨道类型
                dataSummary=data["tracks"][j]["segments"] # 得到所有的轨道数据
                timelens = len(dataSummary)
                for i in range(0,timelens):
                    Trackdatatimes.append(data["tracks"][j]["segments"][i]["target_timerange"]|{"number":j}|{"numlist":i}) #遍历轨道中所有数据的trget_timerange类型
        for j in range(0,guidao):
            if data["tracks"][j]["type"] == "text": #获取类型 判断字幕轨道类型
                dataSummary=data["tracks"][j]["segments"] # 得到所有的轨道数据
                timelens = len(dataSummary)
                for i in range(0,timelens):
                    Subtitletrack.append(data["tracks"][j]["segments"][i]["target_timerange"]|{"number":j}|{"numlist":i}) #遍历轨道中所有数据的trget_timerange类型
        skipped = False # 创建一个布尔变量，用于标记是否已经跳过第一个"audio"节点
        numat = [i for i, item in enumerate(copydata["tracks"]) if item["type"] == "audio"] # 使用列表推导式生成需要删除的节点的索引列表
        if len(numat) == 0:
            return  False
        first_audio = numat[0] # 创建一个变量来存储第一个"audio"节点的索引


        for i in reversed(numat): # 使用reversed()函数反向遍历索引列表
            if len(numat)==1:
                copydata["tracks"][first_audio]["segments"]=[]
                break
            if not skipped: # 如果还没有跳过第一个"audio"节点
                skipped = True # 将布尔变量设为True
                del copydata["tracks"][i]["segments"]
                copydata["tracks"][i]["segments"]=[]
                continue # 跳过当前循环
            del copydata["tracks"][i] # 删除当前节点
        numat = [i for i, item in enumerate(copydata["tracks"]) if item["type"] == "text"] # 使用列表推导式生成需要删除的节点的索引列表
        if len(numat) == 0:
            return False
        first_text = numat[0] # 创建一个变量来存储第一个"audio"节点的索引

        for i in reversed(numat): # 使用reversed()函数反向遍历索引列表
            if len(numat)==1:
                copydata["tracks"][first_text]["segments"]=[]
                break
            if not skipped: # 如果还没有跳过第一个"audio"节点
                skipped = True # 将布尔变量设为True
                del copydata["tracks"][i]["segments"]
                copydata["tracks"][i]["segments"]=[]
                continue # 跳过当前循环
            del copydata["tracks"][i] # 删除当前节点
        Trackdatatimes.sort(key=lambda x :  x["start"])
        Subtitletrack.sort(key=lambda x :  x["start"])
        Ifst=False
        for i in Trackdatatimes:
            if not Ifst:
                Ifst=True
                Tracktimerecording= i["duration"]
                Tracktimecorrection=i["start"]
                continue
            i["start"]=Tracktimerecording+Tracktimecorrection
            Tracktimerecording=i["duration"]
            Tracktimecorrection=i["start"]
            data["tracks"][i["number"]]["segments"][i["numlist"]]["target_timerange"]["duration"]=i["duration"]
            data["tracks"][i["number"]]["segments"][i["numlist"]]["target_timerange"]["start"]=i["start"]
        for i in range(len(Trackdatatimes)):
            data["tracks"][Subtitletrack[i]["number"]]["segments"][Subtitletrack[i]["numlist"]]["target_timerange"]["duration"]=Trackdatatimes[i]["duration"]
            data["tracks"][Subtitletrack[i]["number"]]["segments"][Subtitletrack[i]["numlist"]]["target_timerange"]["start"]=Trackdatatimes[i]["start"]

        for i in Trackdatatimes:
            copydata["tracks"][first_audio]["segments"].append(data["tracks"][i["number"]]["segments"][i["numlist"]])
        for i in Subtitletrack:
            copydata["tracks"][first_text]["segments"].append(data["tracks"][i["number"]]["segments"][i["numlist"]])
        with open(path, "w", encoding='utf-8') as f:
            json.dump(copydata,f)
            f.close()
        return True
    except:
        return False
