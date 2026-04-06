class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        left = 0
        max_count = 0
        best = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            freq[idx] += 1

            max_count = max(max_count, freq[idx])

            while (right - left + 1) - max_count > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best