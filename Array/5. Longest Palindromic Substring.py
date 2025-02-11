def longestPalindrome_optimal(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    start, end = 0, 0
    for i in range(len(s)):
        # Odd-length palindrome (single character center)
        l1, r1 = expand_around_center(i, i)
        # Even-length palindrome (two characters as center)
        l2, r2 = expand_around_center(i, i + 1)

        # Update the longest palindrome
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]

print(longestPalindrome_optimal("babad")) # "bab" or "aba"