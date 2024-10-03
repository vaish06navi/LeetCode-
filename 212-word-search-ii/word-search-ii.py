class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the Trie
        root = TrieNode()
        for w in words:
            root.addWord(w)

        rows = len(board)
        cols = len(board[0])

        res = set()  # To store unique words
        visited = set()  # To track visited positions

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r == rows or c == cols or
                    (r, c) in visited or board[r][c] not in node.children):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.add(word)

            # Explore all four directions
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            # Backtrack
            visited.remove((r, c))

        # Start DFS from each cell in the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, '')

        return list(res)


