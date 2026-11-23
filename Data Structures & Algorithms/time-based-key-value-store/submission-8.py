class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        search = self.mp[key]
        l, r = 0, len(search) - 1
        while l <= r:
            mid = (l + r) // 2
            if search[mid][1] == timestamp:
                return search[mid][0]
            elif search[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        
        #r ends on equal or less timestamp (or -1 if dne)
        if r < 0:
            return ""
        return search[r][0]

