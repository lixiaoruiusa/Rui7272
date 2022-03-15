class Solution:
    """
    @param path: the original path
    @return: the simplified path
    @ 用 stack
    ['', 'a', '.', '..', '..', 'c', '']
    """
    def simplifyPath(self, path):
        # write your code here
        path = path.split('/')
        stack = []
        for i in path:
            if i == '..':
                if stack:
                    stack.pop()
            elif i != '.' and i != '':
                stack.append(i)
                
        return '/' + '/'.join(stack)

 