
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.name_to_value_timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.name_to_value_timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        time_val_list = self.name_to_value_timestamps[key]
        l, r = 0, len(time_val_list) - 1
        print(time_val_list)
        print(f'key: {key}, time: {timestamp}')
        best_val = ""

        while l <= r:
           
            mid = l + ((r - l) // 2)
            print(f"len: {len(time_val_list)}, l: {l}, r: {r}, mid: {mid}")
            mid_time, mid_val = time_val_list[mid]

            if mid_time == timestamp:
                return time_val_list[mid][1]
            
            if mid_time > timestamp:
                
                r = mid - 1
            else:
                best_val = mid_val
                l = mid + 1


        return best_val