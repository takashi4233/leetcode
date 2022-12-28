from typing import List
class Solution:
    # 面白くはない（Pythonの機能を使ってるだけ）だけど、簡単にできる
    # 最後の0bを消す処理はreplaceじゃなくて[2:]でスライスしてもいいかも
    def addBinary(self, a: str, b: str) -> str:
        #print (f"a={a},b={b}")
        #print (f"a={int(a,2)},b={int(b,2)}")
        #print (f"a+b = {int(a,2) + int(b,2)}")
        #print (f"a+b = {bin(int(a,2) + int(b,2))}")
        #print (f"a+b = {str.replace(bin(int(a,2) + int(b,2)),'0b','')}")
        return str.replace(bin(int(a,2) + int(b,2)),'0b','')
    
    def test(self,input,answer):
        assert input == answer, '期待する値[{1}], 入力値[{0}]'.format(input, answer)
        
def main():
    s = Solution()
    a = "11"
    b = "1"
    output = "100"
    s.test(s.addBinary(a,b),output) 
    
    a = "1010"
    b = "1011"
    output = "10101"
    s.test(s.addBinary(a,b),output) 
if __name__ == "__main__":
    main()

    
