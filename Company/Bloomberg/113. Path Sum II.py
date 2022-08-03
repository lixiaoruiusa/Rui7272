class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        if not root:
            return []

        paths = []

        self.dfs(root, targetSum, [root.val], paths)

        return paths

    def dfs(self, root, targetSum, path, paths):

        if not root:
            return

        # 在最底层的时候
        if not root.left and not root.right:
            if sum(path) == targetSum:
                paths.append(list(path))

        if root.left:
            path.append(root.left.val)
            self.dfs(root.left, targetSum, path, paths)
            path.pop()

        if root.right:
            path.append(root.right.val)
            self.dfs(root.right, targetSum, path, paths)
            path.pop()

"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None: 
            return []
        result = [root.val]
        results = []
        self.dfs(root, targetSum, 0, result, results)
        return results

    def dfs(self, root, targetSum, cur_sum, cur_result, results):

        if root is None:
            return

        cur_sum += root.val

        if root.left is None and root.right is None and cur_sum == targetSum:
            results.append(list(cur_result))
            return

        if root.left:
            cur_result.append(root.left.val)
            self.dfs(root.left, targetSum, cur_sum, cur_result, results)
            cur_result.pop()

        if root.right:
            cur_result.append(root.right.val)
            self.dfs(root.right, targetSum, cur_sum, cur_result, results)
            cur_result.pop()
"""