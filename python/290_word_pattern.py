class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}

        for i, ch in enumerate(pattern):
            if ch in char_to_word and char_to_word[ch] != words[i]:
                return False

            if words[i] in word_to_char and word_to_char[words[i]] != ch:
                return False

            char_to_word[ch] = words[i]
            word_to_char[words[i]] = ch

        return True
