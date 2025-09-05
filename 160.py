# Intersection of Two Linked List

# 틀린 풀이
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        
        while a != b:
            a = a.next if a.next else headB
            b = b.next if b.next else headA
        return a
# 틀린 이유
# 두 Linked List가 교차하지 않는 경우를 체킹하지 못한다.
# 교차점이 없는 경우, a != b가 항상 참이 되어 무한 루프를 돌게 된다.
# Point: 리트코드에서 Time Limit Exceeded 에러가 발생했다. 위 코드에서 병목이 일어날만한 부분은 while문 밖에 없다.
#        에러 핸들링을 할 때, while에서 무한 루프가 발생했음을 어느 정도 인지를 하고 있었어야 했다.


# 올바른 풀이
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

# 두 Linked List의 교차점이 없는 경우, a와 b가 동시에 null이 될 때, while 루프가 종료된다.
  
