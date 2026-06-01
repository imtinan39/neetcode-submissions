from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Fixed-size array for 26 lowercase letters — faster than a hash map
        chars_count = [0] * 26
        for c in chars:
            chars_count[ord(c) - 97] += 1  # ord('a') == 97

        ans = 0

        for word in words:
            word_count = [0] * 26
            for c in word:
                word_count[ord(c) - 97] += 1

            # Check all 26 slots — no need for key iteration
            for i in range(26):
                if word_count[i] > chars_count[i]:
                    break
            else:
                # for-else: the else block runs only if the loop did NOT break
                ans += len(word)

        return ans

