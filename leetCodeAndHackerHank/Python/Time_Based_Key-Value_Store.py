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
