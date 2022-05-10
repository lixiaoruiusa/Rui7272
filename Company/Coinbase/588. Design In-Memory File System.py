"""
ls 的时间复杂度是 O(m+n+klog(k))。这里 m 是输入字符串的长度，我们需要扫描输入字符串一次并获得每一层的文件名。
n 是最后一层文件夹的深度，我们需要进入 n 层的文件树以到达最后一层文件所在路径。k是最后一层的文件和文件夹总数目。我们需要将它们排序，所以需要 klog(k) 的时间。

mkdir 时间复杂度是 O(m+n)，这里 m 是输入字符串的长度，n是最后一层文件夹的深度。

addContentToFile 和 readContentFromFile 操作的时间复杂度都是 O(m+n)。m 是输入字符串的长度，n 是最后一层文件夹在文件树中的深度。

Pro：
使用这种维护文件结构的优势是很容易添加更多指令。比方说，rmdir 删除一个文件夹的指令只需要从列表中删除相应的条目。

重命名文件或者文件夹非常容易，因为我们只需要以新名字创建一个新的文件夹结构或者文件并删除原本的条目即可。

从一个路径移动子文件夹到另一个路径也很容易，因为我们需要做的只是获得相应子文件夹类的地址，然后在新文件路径下赋新的值。

如果文件夹数目非常大，我们会因为 isfile 和 content浪费多余的空间，这部分空间在方法 1 中不会存在。

这个方法的一个问题是如果我们只想要给定路径中文件夹的列表，而不是文件的列表，访问将会变得低效。我们需要遍历当前文件夹所有内容一遍并检查是否是文件夹，才能得到我们想要的数据。

https://leetcode.cn/problems/design-in-memory-file-system/solution/she-ji-nei-cun-wen-jian-xi-tong-by-leetcode/
"""


class Trie:

    def __init__(self):
        self.child = {}
        self.is_file = False
        self.name = ""
        self.content = ""


class FileSystem:

    def __init__(self):
        self.root = Trie()

    def ls(self, path: str) -> List[str]:
        cur = self.root
        res = []
        # 如果path为ls根目录下内容
        if path == '/':
            for key in cur.child.keys():
                res.append(key)
            return sorted(res)

        # 如果path为ls某个具体目录下内容（['a', 'b', 'c', 'd']或者invalid['a', 'b', 'c', '']）
        path_list = path[1:].split('/')
        for ch in path_list:
            if ch not in cur.child.keys():
                return []
            # 如果在就继续往下找
            cur = cur.child[ch]

        for key in cur.child.keys():
            res.append(key)
        if cur.is_file:
            res.append(cur.name)
        return sorted(res)

    def mkdir(self, path: str) -> None:
        cur = self.root
        path_list = path[1:].split('/')
        for ch in path_list:
            if ch not in cur.child.keys():
                cur.child[ch] = Trie()
            cur = cur.child[ch]
            cur.name = ch

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        path_list = filePath[1:].split('/')
        for i, ch in enumerate(path_list):
            if ch not in cur.child.keys():
                cur.child[ch] = Trie()
            cur = cur.child[ch]
            cur.name = ch

        cur.is_file = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        path_list = filePath[1:].split('/')
        for ch in path_list:
            cur = cur.child[ch]
        return cur.content

"""

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

"""

file_sys = FileSystem() 
path_listed = file_sys.ls(path)
file_sys.mkdir(path)
file_sys.addContentToFile(filePath,content)
content_filePath = file_sys.readContentFromFile(filePath)
"""

"""
    try:
        cur.execute(
            query,
            (row['agent_id'], row['agent_pid'], row['agent_json'],row['agent_json'])
        )
        conn.commit()
        return True, "Records created successfully with agent_id of " + row['agent_id']

    except Exception as e:
        cur.execute("ROLLBACK")
        conn.commit()
        print(e)
        return False, e


# 题目是实现一个in-memory file system, support
# createFolder(path:string)
# deleteFolder(path:string)
# traverseRoot() lists all folders and subfolders from root folder.
# create和delete需要验证路径是否有效，所有操作都是文件夹，没有文件。
# follow up 1： traverse‍‍‌‍‌‌‍‍‌‍‌‍‌‌‍‍‍‌‌‍ 输出的结果要按照字典序
# follow up 2： 现实中实现这个类似的file system，需要考虑那些scalability和reliability的问题


# class Trie:
#
#     def __init__(self):
#         self.child = {}
#         self.name = ""
#
# class FileSystem:
#
#     def __init__(self):
#         self.root = Trie()
#
#     def is_valid(self, path):
#         if not path:
#             return False
#         if path[0] != "/":
#             return False
#         path_list = path[1:].split('/')
#         for ch in path_list:
#             if not ch.isalpha():  # isalnum()
#                 return False
#         return True
#
#     def createFolder(self, path):
#         if not self.is_valid(path):
#             return "not valid path"
#
#         cur = self.root
#         path_list = path[1:].split('/')
#         for ch in path_list:
#             if ch not in cur.child.keys():
#                 cur.child[ch] = Trie()
#             cur = cur.child[ch]
#             cur.name = ch
#
#     def deleteFolder(self, path):
#         if not self.is_valid(path):
#             return "not valid path"
#         cur = self.root
#         path_list = path[1:].split('/')
#         for ch in path_list:
#             if ch not in cur.child.keys():
#                 cur.child[ch] = Trie()
#             cur = cur.child[ch]
#             cur.name = ch
#
#     def traverseRoot(self):
#         cur = self.root
#         res = []
#         # 如果path为ls根目录下内容
#         if path == '/':
#             for key in cur.child.keys():
#                 res.append(key)
#             return sorted(res)
