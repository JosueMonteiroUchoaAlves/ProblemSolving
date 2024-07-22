# https://leetcode.com/problems/time-based-key-value-store/
# 981. Time Based Key-Value Store

class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.map.get(key, 0):
            self.map[key] = []
        self.map[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res = ""

        
        values = self.map.get(key, [])
        a, c = 0, len(values)-1
        while a <= c:
            # map[key][actualMiddleItem][hisTimestamp]
            b = (a+c)//2
            if values[b][1] <= timestamp:
                res = values[b][0]
                a = b + 1
            else:
                c = b - 1
        return res

        
    
lista = ["set","set","get","set","get","set","set","get","set","get","set","get","set","get","set","get","get","get","get","get","get","set","set","set","get","get","set","set","get","set"]
lista2 = [["rtzoj","kuexwze",1],["xcywxndnz","herqmazp",2],["xcywxndnz",3],["rtzoj","dgpguflin",4],["xcywxndnz",5],["dgpguflin","lvrexco",6],["xcywxndnz","dgpguflin",7],["xcywxndnz",8],["rtzoj","wxqixmxs",9],["xcywxndnz",10],["kuexwze","lvrexco",11],["dgpguflin",12],["lvrexco","wxqixmxs",13],["xcywxndnz",14],["herqmazp","vjfhio",15],["dgpguflin",16],["herqmazp",17],["herqmazp",18],["rtzoj",19],["herqmazp",20],["herqmazp",21],["kuexwze","vjfhio",22],["dgpguflin","qrkihrb",23],["kuexwze","dgpguflin",24],["rtzoj",25],["dgpguflin",26],["herqmazp","rtzoj",27],["lvrexco","iztpo",28],["lvrexco",29],["kuexwze","lvrexco",30]]
timeMap = TimeMap();

for index, item in enumerate(lista):
    if item == "set":
        print(timeMap.set(lista2[index][0],lista2[index][1],lista2[index][2]))
    if item == "get":
        print(timeMap.get(lista2[index][0],lista2[index][1]))


