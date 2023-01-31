from typing import List
from typing import Optional

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        l = list(key)
        l2 = []
        for s in l:
            if s !=  " ":
                l2.append(s)
        # 順番を保持して重複を取り除く
        s = list(sorted(set(l2), key=l2.index))
        # ascii->char : chr
        # char -> ascii : ord
        ans = ""
        for m in message:
            if m == " ":
                ans = ans + " "
            else:
                ans = ans + (chr(s.index(m)+97))
        return ans

    # この記述方法は良いと思う
    # def decodeMessage(self, key: str, message: str) -> str:
    #     table = {" " : " "}
    #     alpha = 97
    #     for i in range(len(key)):
    #         if key[i] not in table:
    #             table[key[i]] = chr(alpha)
    #             alpha += 1
    #             if alpha == 123:
    #                 break
    #     ans = "".join([table[c] for c in message])
    #     return(ans)

    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)

def main():
    s = Solution()
    key,message,expected = "the quick brown fox jumps over the lazy dog","vkbs bs t suepuv", "this is a secret"
    s.test(s.decodeMessage(key,message),expected)

if __name__ == "__main__":
    main()

