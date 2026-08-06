# so brutally forced way to check if it's even somehwat possibl is to do a column check across all triples
# however, the main challenge here is figuring out if you can actually use the triplet, or it would be brutally overridden by other triples
# brute force, try all possible combos, factorial time

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        marked_indices = set()

        for triplet in triplets:
            if (
                triplet[0] > target[0] or
                triplet[1] > target[1] or
                triplet[2] > target[2]
            ):
                continue
            
            for i, v in enumerate(triplet):
                if v == target[i]:
                    marked_indices.add(i)

        return len(marked_indices) == len(target)