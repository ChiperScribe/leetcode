# 헬퍼 함수 사용
# 문자열 슬라이싱을 과하게 사용하지 않고, 인덱스 기반으로 문자열 내의 문자를 처리
# if-else 구문을 사용하지 않았다.
#   파이썬에서는 Early return을 선호한다. 코드를 살펴보면, if문에 들어갔을 때 return이 되는 것을 확인할 수 있다.
#   1. 불필요한 경우를 먼저 처리하고 2. 정상 흐름은 else문 없이 작성하는 연습을 하자.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
        return True
