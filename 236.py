# Pre-check + Post-combine DFS
# 1. if root is None or root == p or root == q를 먼저 검사
#    -> preorder 스타일의 검사(early-exit)
# 2. left, right 탐색
# 3. 자식으로부터 결과를 합성해서 반환 -> postorder 스타일의 결과 처리(aggregation)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        return left if left else right

# 1. p가 q의 서브트리에 있을 때, p가 바로 LCA이다.
# 2. p가 q의 서브트리에 없을 때, p에서 올라간 경로와 q에서 올라간 경로가 만나는 첫 노드를 반환
