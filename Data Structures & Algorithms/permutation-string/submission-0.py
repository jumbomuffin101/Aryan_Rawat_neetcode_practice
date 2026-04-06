class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = [0] * 26
        freq = [0] * 26
        left = 0

        for c in s1:
            target[ord(c) - ord('a')] += 1

        for right in range(len(s2)):
            freq[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > len(s1):
                freq[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            if right - left + 1 == len(s1):
                if target == freq:
                    return True
        return False