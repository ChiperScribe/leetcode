## 1
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # x[0]: 키, x[1]: 키 큰 사람의 수
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        res = []
        
        for p in people:
            res.insert(p[1], p)
        return res

## 2
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # x[0]: 키, x[1]: 키 큰 사람의 수
        heap = []
        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))

        res = []
        while heap:
            person = heapq.heappop(heap)
            res.insert(person[1], [-person[0], person[1]])
        return res
