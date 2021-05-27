class BrowserHistory:

    def __init__(self, homepage: str):
        self.his = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        while self.his and len(self.his) - 1 > self.cur:
            self.his.pop()

        self.his.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        self.cur -= min(self.cur, steps)
        return self.his[self.cur]

    def forward(self, steps: int) -> str:
        self.cur += steps
        self.cur = min(self.cur, len(self.his) - 1)
        return self.his[self.cur]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


# 使用一个数组his保存所有的访问记录，使用cur保存当前处于数组中的哪个位置。
# 1 __init__(str)函数：初始化时把homepage放入数组中。
# 2 forward(steps)函数：会让cur前进steps步，但是注意不能超出数组的右边界。
# 3 back(steps)函数：会让cur后退steps步，但是注意不能少于数组的左边界。
# 4 visit(url)函数：会先把cur位置以后的所有历史记录清空，然后把url放到his数组的后面。

obj = BrowserHistory("leetcode.com")
obj.visit("1.com")
obj.visit("2.com")
obj.visit("3.com")
param_2 = obj.back(1)
param_3 = obj.forward(2)
print(param_2)
print(param_3)


# browserHistory = BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       #// You are in "leetcode.com". Visit "google.com"
# browserHistory.visit("facebook.com");     #// You are in "google.com". Visit "facebook.com"
# browserHistory.visit("youtube.com");      #// You are in "facebook.com". Visit "youtube.com"
# browserHistory.back(1);                   #// You are in "youtube.com", move back to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   #// You are in "facebook.com", move back to "google.com" return "google.com"
# browserHistory.forward(1);                #// You are in "google.com", move forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     #// You are in "facebook.com". Visit "linkedin.com"
# browserHistory.forward(2);                #// You are in "linkedin.com", you cannot move forward any steps.
# browserHistory.back(2);                   #// You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);








