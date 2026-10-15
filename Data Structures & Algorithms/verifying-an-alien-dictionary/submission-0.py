class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d ={}
        i = 0; j = 0
        for i in range(len(order)):
            d[order[i]] = i

        for j in range(len(words) - 1):

            w1 = words[j]
            w2 = words[j+1]


            for k in range(min(len(w1),len(w2))):

                if w1[k] != w2[k]:
                    if d[w1[k]] > d[w2[k]]:
                        return False
                    break
                
            else:
                if len(w1) > len(w2):
                    return False 

        return True 