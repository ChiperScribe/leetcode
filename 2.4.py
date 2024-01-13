import collections
import re
from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned = List[str]) -> str:
        word_list = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        filtered_words = [word for word in word_list if word not in banned]

        counts = collections.Counter(filtered_words)
        return counts.most_common(1)[0][0]
