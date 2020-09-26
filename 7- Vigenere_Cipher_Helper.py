class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key, self.alphabet = key, alphabet
        while len(self.key) < len(alphabet): self.key = 2*self.key
    def encode(self, text):
        res = ""
        for i,char in enumerate(text):
            ind = self.alphabet.find(char)
            res = res + char if ind == -1 else res + self.alphabet[(self.alphabet.find(self.key[i]) + ind) % len(self.alphabet)]
        return res
    def decode(self, text):
        res = ""
        for i,char in enumerate(text):
            ind = self.alphabet.find(char)
            res = res + char if ind == -1 else res + self.alphabet[self.alphabet.find(char) - self.alphabet.find(self.key[i])]
        return res