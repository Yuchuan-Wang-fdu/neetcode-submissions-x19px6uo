class TimeMap:

    def __init__(self):
        self.keySet = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keySet:
            self.keySet[key] = {}
        if timestamp not in self.keySet[key]:
            self.keySet[key][timestamp] = []
        self.keySet[key][timestamp].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keySet:
            return ""
        seen = 0
        for time in self.keySet[key]:
            if time<= timestamp:
                seen = max(seen, time)
        return "" if seen == 0 else self.keySet[key][seen][-1]
        
