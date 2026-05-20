class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # position to write the next compressed character
        read = 0   # position to read from

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count consecutive occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # Write the count (only if > 1), digit by digit
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        print(chars)
        return write

            

        