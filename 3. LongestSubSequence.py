# This solution takes 38ms and it beats 99.74& of users

def lengthOfLongestSubstring(s: str) -> int:

        longest = []
        current_s = ''
        for i in s:
            if i not in current_s:
                current_s += i
                longest.append(current_s)
            else:
                j = current_s.index(i)
                longest.append(current_s)
                current_s = current_s[j + 1:] + i
                
            print(longest)
        return max([len(str(i)) for i in longest]) if longest else 0
