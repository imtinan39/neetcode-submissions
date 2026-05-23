class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        ans = float("inf")
        count = 0  # number of white blocks in the current window

        for r in range(len(blocks)):
            # Expand window: count white blocks
            if blocks[r] != "B":
                count += 1

            # When window reaches size k
            if r - l + 1 == k:
                ans = min(ans, count)
                # Shrink window: remove the contribution of blocks[l]
                if blocks[l] != "B":
                    count -= 1
                l += 1

        return ans

        