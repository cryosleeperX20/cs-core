# LeetCode Problem 1948: Delete Duplicate Folders in a System
# Aim: Given a list of folder paths, remove all duplicate folders (subtrees with identical structure and names).
# Output the list of remaining folder paths in any order.

from collections import defaultdict

class TreeNode:
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = TreeNode()

        # Step 1: Build the tree from paths
        for path in paths:
            curr = root
            for folder in path:
                curr = curr.children[folder]

        # Step 2: Serialize subtrees to detect duplicates
        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            serials = []
            for name in sorted(node.children):
                child_serial = serialize(node.children[name])
                serials.append(f"{name}({child_serial})")
            serial = "".join(serials)
            serial_map[serial].append(node)
            return serial

        serialize(root)

        # Step 3: Mark duplicate folders as deleted
        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        # Step 4: Collect valid paths via DFS
        res = []

        def collectPaths(node, path):
            for name, child in node.children.items():
                if not child.deleted:
                    new_path = path + [name]
                    res.append(new_path)
                    collectPaths(child, new_path)

        collectPaths(root, [])
        return res
