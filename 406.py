class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # x[0]: 키, x[1]: 키 큰 사람의 수
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        res = []
        
        for p in people:
            res.insert(p[1], p)
        return res
