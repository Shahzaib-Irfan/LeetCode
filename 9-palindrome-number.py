class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0: 
            return False

        elements = []
        while x >= 10:
            modulus = x % 10
            divident = x // 10
            elements.append(modulus)
            if divident < 10:
                elements.append(divident)
                break

            x = divident

        return elements == elements[::-1]