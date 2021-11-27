class RecentCounter:

    def __init__(self):
        self.counter : List[int] = []
        self.time_window = 3000

    def ping(self, t: int) -> int:
        self.counter.insert(0, t)
        num_pings_in_time_window = 0
        for ping_time in self.counter:
            if (t - self.time_window) <= ping_time:
                num_pings_in_time_window += 1
            else:
                break
        return num_pings_in_time_window
