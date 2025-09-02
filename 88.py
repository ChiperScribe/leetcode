# 1. 초기 코드
# in-place하게 nums1을 수정해야 하는데, nums1 = res는 nums1의 참조를 바꾸기만 할 뿐 nums1 자체를 수정해주지 않는다.
#   nums1[:m+n] = res와 같이 수정해야 한다. nums1[:] -> nums1의 크기가 바뀔 수도 있다.
#   문제에서는 nums1 배열이 m+n 크기를 유지하길 바라고 있으므로, nums1[:m+n]이 더 안전하다
# 불필요한 if-else문. while문에서 조건 검사를 하므로 if-else는 필요 없다.
# 잘못된 while문. i, j를 증가시키는 연산을 빼먹었다.
# 총체적 난국이다. 한 걸음씩 앞으로 나가자
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = j = 0
        res = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        if i == m:
            while j < n:
                res.append(nums2[j])
        elif j == n:
            while i < m:
                res.append(nums1[i])
              
        nums1 = res

# 2. 오류만 고친 코드
# [슬라이싱]: 참조를 유지한 채, 리스트의 내용 자체를 교체 [할당]: 참조를 교체
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = j = 0
        res = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < m:
            res.append(nums1[i])
            i += 1
        while j < n:
            res.append(nums2[j])
            j += 1

        nums1[:m+n] = res

# 3. 최적화 코드
# 배열의 뒷 요소들이 dummy이므로, dummy를 먼저 올바른 값으로 채워나가면,
# 추가적인 공간 할당 없이 문제를 풀이할 수 있다.
# j < 0에 의해 while문을 탈출한 경우, nums1은 추가적인 작업이 필요하지 않다.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        
        while i >=0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -=1
