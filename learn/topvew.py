import collections
def topview(root):
    if root is None:
        return []
    index_val = collections.defaultdict(list)
    result = []

    def dfs(node, height, level):
        if node is None:
            return
        if level not in index_val:
            index_val[level] = [node.data, height]
        elif index_val[level][1] > height:
            index_val[level] = [node.data, height]
        dfs(node.left, height + 1, level - 1)
        dfs(node.right, height + 1, level + 1)
        return

    dfs(root, 0, 0)
    sorted_dict = sorted(index_val.items(), key=lambda x: x[0])
    for pair in sorted_dict:
        result.append(pair[1])
    return result
    