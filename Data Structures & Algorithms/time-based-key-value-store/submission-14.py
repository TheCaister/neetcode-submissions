# timestamps are strictly increasing, there's a sorted order to it
# so this seems like nested map. name -> (list of (timestamps, value) tuples)
# set should be pretty simple and constant time, just quickly find the name, and append the value to the end.
# it will be sorted because we're told it's sorted
# get is where things become interesting. it's basically a binary search. if we find exact match, nice. if we don't, let's pretend that
# we're about to insert it at an appropriate position. we just set the value of the previous item in the list
# if there is no previous, return ""

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.name_to_value_timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.name_to_value_timestamps[key].append((timestamp, value))
        

# 2, 4
# we should be able to get mid in most cases
# what about target = 5? we'll have to make sure l crosses mid?

    def get(self, key: str, timestamp: int) -> str:
        value_list = self.name_to_value_timestamps[key]
        
        l, r = 0, len(value_list) - 1
        res = ""

        while l <= r:
            mid = l + ((r - l) // 2)
            # print(value_list)
            # print(f'l: {l}, r: {r}, mid: {mid}')
            mid_time = value_list[mid][0]

            if mid_time < timestamp:
                res = value_list[mid][1]
                l = mid + 1
            elif mid_time > timestamp:
                r = mid - 1
            else:
                res = value_list[mid][1]
                # print('breaking.....')
                break

        return res