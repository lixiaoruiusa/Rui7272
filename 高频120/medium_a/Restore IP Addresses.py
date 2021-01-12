class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    @ DFS 
    """
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res
    
    def dfs(self, s, idx, path, res):
        if idx > 4:
            return 
        if idx == 4 and not s:
            # 正向输出  从开始 ~ 倒数第第1个字符（不含)
            res.append(path[:-1])
            return 
        
        for i in range(1, len(s)+1):
            
            if s[:i] == '0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                
                self.dfs(s[i:], idx+1, path+s[:i]+".", res)