# This solution takes 33ms and beats 88.78% of users

def reverse(x: int) -> int:
        sign = 1
        if x < 0: 
            sign = -1
            x = str(x)[1:]

        x = int(str(x)[::-1])

        return x * sign if x <= (2 ** 31) -1 and x * sign >= -(2 ** 31) else 0