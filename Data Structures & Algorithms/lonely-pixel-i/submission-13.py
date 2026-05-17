class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        hash_col={}
        hash_rows={}
        count=0

        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if picture[i][j]=="B":
                    hash_col[j]=hash_col.get(j,0)+1
                    hash_rows[i]=hash_rows.get(i,0)+1

        for i in range(len(picture)):
            if hash_rows.get(i, 0) != 1:
                continue
            for j in range(len(picture[i])):
                if picture[i][j]=="B" and hash_col[j]==1:
                    count+=1
        return count

        