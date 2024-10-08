from collections import deque

class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        def get_next_words(word):
            next_words = []
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + char + word[i+1:]
                    if new_word != word and new_word in wordList:
                        next_words.append(new_word)
            return next_words

        def bfs():
            level_map = {beginWord: [[beginWord]]}
            while level_map:
                new_level_map = {}
                for word in level_map:
                    if word == endWord:
                        return level_map[word]
                    for next_word in get_next_words(word):
                        for path in level_map[word]:
                            new_path = path + [next_word]
                            if next_word not in new_level_map:
                                new_level_map[next_word] = [new_path]
                            else:
                                new_level_map[next_word].append(new_path)
                wordList -= set(new_level_map.keys())
                level_map = new_level_map
            return []

        return bfs()
