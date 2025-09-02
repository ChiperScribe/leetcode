# 1. 정렬
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

# 2. 힙
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)  # descending order, max-heap

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)
----------------------------------------------------------------
# 2-2. 힙 개선된 구조
# 큰 것들만 k개 모아둔 것에서 가장 작은 값: 리스트에서 k번째로 큰 값
# 힙 크기를 k로 유지한다는 건, k개보다 작은 애들은 전부 버린다는 뜻
# Top k 묶음: [1st, 2nd, ..., kth], 그 중 가장 작은 값이 k번째로 큰 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      heap = []
      for num in nums:
        heapq.heappush(heap, num)  # min-heap
        if len(heap) > k:  # 지금까지 본 원소들 중 큰 원소들만 k개 모아두자
          heapq.heappop()

      return heap[0]

# 3. Quick Select
# k번째로 큰 값 혹은 k번째로 작은 값을 찾을 때 유용하게 쓰이는 알고리즘

# 절차
# 1. 배열에서 랜덤하게 pivot 선택
# 2. pivot보다 큰 값들은 왼쪽, 작은 값들은 오른쪽으로 분할(partition)
# 3. 이제 pivot의 위치(index)가 정해짐
# 4. 만약 pivot이 k-1번째 위치라면 -> pivot이 정답
#        pivot이 너무 왼쪽이면 -> 오른쪽에서 계속 탐색.
#        pivot이 너무 오른쪽이면 -> 왼쪽에서 계속 탐색.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left

            for i in range(left, right):
                if nums[i] > pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def select(left, right, k_smallest):
            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)

        return select(0, len(nums) - 1, k - 1)
