class Solution:
    def isPalindrome(self, x: int) -> bool:
        # initial thoughts, convert x to a string and use l and r pointers to check for palindrome
        # secondary thoughts, use left and right pointers by using modulo to keep track of location

        if x < 0:
            return False
        
        # 3265, n = 4

        my_str = x
        length = 0
        while my_str > 0:
            my_str = my_str // 10
            length += 1
        
        n = length
        i = 10
        l, r = x // (10 ** (n - 1)), x % i
        for _ in range(length // 2):
            if l != r:
                return False
            
            n -= 1
            l = (x // (10 ** (n - 1))) % 10

            i *= 10
            r = (x % i) // (i / 10)
        
        return True
        
        