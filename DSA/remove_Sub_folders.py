"""
LeetCode 1233 – Remove Sub-Folders from the Filesystem

📝 Problem:
You are given a list of strings 'folder', where each string represents a valid folder path (e.g. "/a", "/a/b", "/c/d").

📌 Task:
Remove all sub-folders from the list. A sub-folder is any folder that is inside another folder.
For example, "/a/b" is a sub-folder of "/a".

✅ Output:
Return a list of only the top-level folders, i.e., folders that are not inside any other folder.
The order of the output does not matter.
"""

class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        ans = []
        prev = ""
        for f in folder:
            if not (prev and f.startswith(prev) and f[len(prev)] == '/'):
                ans.append(f)
                prev = f
        return ans
