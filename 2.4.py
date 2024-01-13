import collections
import re
from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned = List[str]) -> str:

        word_list = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        filtered_words = [word for word in word_list if word not in banned]

        counts = collections.defaultdict(int)
        for word in filtered_words:
            counts[word] += 1

        return max(counts, key=counts.get)
