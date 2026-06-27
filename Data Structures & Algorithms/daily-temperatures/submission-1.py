
# number of days after that particular day, before warmer temperature appears
# later in the array, will be 1
# last element is guaranteed to be 0
# highest element is guaranteed to be 0, no other possible days higher
# o n^2 solution where you potentially check the entire list for each element
# decreasing/equal arrays, gonna be all zeros
# strictly increasing arrays, all gonna be 1 until the last element
# would it make sense to start from the start or the end? possible to break this down? Don't think so
# for each individual element by itself, how can we calculate? what references can we use?
# for each individual, we're only concerned about values on the right
# it would be great if we know exactly the next highest number, as well as its index
# i could do a super complicatd solution with sorting etc etc
# 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                else:
                    j += res[j]

            if j < n:
                res[i] = j - i
        return res