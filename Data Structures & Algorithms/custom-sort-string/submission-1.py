class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        ans = []

        for ch in order:
            if ch in count:
                ans.append(ch * count[ch])
                del count[ch]

        for ch, freq in count.items():
            ans.append(ch * freq)

        return "".join(ans)