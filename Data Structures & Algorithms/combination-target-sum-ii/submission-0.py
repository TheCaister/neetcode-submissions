class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        sorted_cand = sorted(candidates)

        def dfs(index, cur_list, running_total):
            if running_total == target:
                res.append(cur_list.copy())
                return

            if index >= len(sorted_cand) or running_total > target:
                return
            


            cur_list.append(sorted_cand[index])
            dfs(index + 1, cur_list, running_total + sorted_cand[index])

            index += 1
            while index < len(sorted_cand) and sorted_cand[index] == sorted_cand[index - 1]:
                index += 1

            # while index + 1 < len(sorted_cand) and sorted_cand[index] == sorted_cand[index + 1]:
                # index += 1

            cur_list.pop()
            dfs(index, cur_list, running_total)
        

        dfs(0, [], 0)

        return res