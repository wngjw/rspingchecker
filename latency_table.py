class LatencyTable:
    
    def __init__(self, worlds: dict = {}):
        self.worlds = worlds
    
    def sort_lowest(self):
        return sorted(self.worlds.items(), key = lambda kv:(kv[1], kv[0]))