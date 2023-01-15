from typing import List
from typing import Optional

#31ms /73.78%
class MyQueue:
    def __init__(self):
        self.res = []

    def push(self, x: int) -> None:
        self.res.append(x)

    def pop(self) -> int:
        return self.res.pop(0)

    def peek(self) -> int:
        return self.res[0]

    def empty(self) -> bool:
        if self.res:
            return False
        else:
            return True

def main():
    res = []
    q = MyQueue()
    q.push(1)
    print (q.res)
    q.push(2)
    print (q.res)
    print(q.peek())
    print (q.res)
    q.pop()
    print(q.res)
    q.empty()



if __name__ == "__main__":
    main()

