# Beats 52.31% of Users

from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        def divide_string(input_string, part_size):
            return [input_string[i:i + part_size] for i in range(0, len(input_string), part_size)]



        if not words:
            return []
        word_count = len(words)
        single_word_length = len(words[0])
        total_length = word_count * single_word_length

        indices = []
        for i in range(0, len(s)):
            if i + total_length <= len(s):
                sub_string = s[i: i + total_length]
                sub_string_list = divide_string(sub_string, single_word_length)
                if Counter(sub_string_list) == Counter(words):
                    indices.append(i)
            else:
                break

        return indices

        