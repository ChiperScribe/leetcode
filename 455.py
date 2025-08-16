## 1
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g: greed factor, s: cookie size
        g.sort()
        s.sort()

        res = 0
        for cookie in s:
            pos = bisect.bisect_right(g, cookie)
            if pos > res:
                res += 1
        return res

## 2
# two pointer solution
# time complexity: O(NlogN) + O(N) ≈ O(NlogN)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g: greed factor, s: cookie size
        g.sort()
        s.sort()

        child = cookie = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child
