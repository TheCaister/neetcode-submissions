# i think first of all, would be nice to make adj list for future calculations
# it seems we ALWAYS depart from JFK, so that's always the starting node
# we can always assume there is a valid path, well of course. even if there's a flight that didn't connect, it should be fine
# first instincts -> starting from JFK, dfs all the branches, starting with lex smallest. we stop until we can't go anymore, or we go back to jfk and go to
# the next leg. if from jfk there's only 1 leg, we do jfk + leg. otherwise jfk join all legs
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(deque)
        for src, dst in sorted(tickets):
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].popleft()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]