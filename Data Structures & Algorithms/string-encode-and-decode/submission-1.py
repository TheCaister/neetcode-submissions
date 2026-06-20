# the power of next x to scan, and a delimiter to tell you
# when to actually scan
# encode
# 1. add num + delim + str repeatedly

# decode
# we always expect the pattern num + delim + str
# 1. parse num by keep going until we hit non-num
# 2. skip 1, and grab the next num of chars, and add to list
# 3. return list

class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for string in strs:
            length = len(string)
            output += str(length) + '#' + string

        return output

    def decode(self, s: str) -> List[str]:
        output = []
        scan_idx = 0
        look_ahead = 0

        # quickly scan through and build up number
        # in the event where we hit delim, slice and reset
        while scan_idx < len(s):
            cur_char = s[scan_idx]
            # num parsing step
            if '0' <= cur_char <= '9':
                look_ahead = (look_ahead * 10) + int(s[scan_idx])
                scan_idx += 1
            else:
                # slicing step
                output.append(s[scan_idx + 1: scan_idx + 1 + look_ahead])

                # reset step?
                scan_idx = scan_idx + look_ahead + 1
                look_ahead = 0

        return output

