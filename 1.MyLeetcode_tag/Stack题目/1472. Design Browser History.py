# 题意：Design Browser History
# 思路：用两个stack： browser和stack
# visit时，browser入栈，stack清零
# back时，while step和browser>1时，主栈pop的元素放到副栈去，返回主栈顶
# forward时，while step和stack时， 副栈pop的元素放到主栈去，返回主栈顶
# All Time：O(n)

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.browser = [homepage]
        self.stack = []

    def visit(self, url: str) -> None:
        self.browser.append(url)
        self.stack.clear()

    def back(self, steps: int) -> str:
        while steps and len(self.browser) > 1:
            self.stack.append(self.browser.pop())
            steps -= 1
        cur = self.browser[-1]
        return cur

    def forward(self, steps: int) -> str:
        while steps and self.stack:
            self.browser.append(self.stack.pop())
            steps -= 1
        cur = self.browser[-1]
        return cur

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)