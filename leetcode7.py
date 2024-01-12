def reverse( x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x = x // 10
        reversed_x *= sign
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        else:
            return reversed_x

print(reverse(int(input())))
