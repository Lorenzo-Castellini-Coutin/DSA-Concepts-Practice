#LeetCode Problem 9 (Palindrome Number)

def isPalindrome(x):
        x = str(x)
        new_num=x[::-1]
        if x == new_num:
                return True
        else:
                return False


