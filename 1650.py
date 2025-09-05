# Lowest Common Ancestor(LCA) III

# 1.
# Node는 parent의 정보를 담고 있다. root부터 시작하여 하향식으로 푸는 것이 아니라
# p, q부터 시작하여 상향식으로 추적이 가능하다.
# parent라는 추가적인 메모리를 가지는 것만으로도 알고리즘 수행 속도를 획기적으로 단축할 수 있다.
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ancestors = set()
        while p:
            ancestors.add(p)
            p = p.parent

        while q:
            if q in ancestors:
                return q
            q = q.parent

# 2.
# p, q로부터 parent를 따라가는 일련의 과정은 Linked List의 한 형태로도 생각할 수 있다.
# 두 Linked List가 처음으로 만나는 교차점을 구하면, 해당 값이 LCA가 된다.
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q
        
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
            
        return a

# Review
# 내가 실수한 코드
# 3.
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_head, q_head = p, q
      
        while p != q:
            p = p.parent if p else q_head
            ...
# 처음에 코드를 위와 같이 짰다. 이렇게 짜게 되면 p, q의 값이 직접적으로 수정된다는 단점이 있다.
# 당장 해당 메소드에서는 문제가 발생하지 않지만, 해당 메소드에서 변형시킨 p, q가 다른 코드와 어우러지면 문제가 발생할 수도 있다.
# 프로그램의 안정성을 낮추는 문제가 발생할 수도 있는 것이다.
# Linked List에서 노드 탐색을 할 때에는 '탐색용 임시 포인터'를 하나 만들어 그 포인터로 탐색을 진행하는 방향이 옳은 것 같다.

# Key Word: "탐색용 임시 포인터"
