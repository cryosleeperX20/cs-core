
    def isValid(self, word: str) -> bool:
        VOWELS = set("aeiouAEIOU")
        
        if len(word) < 3:
            return False
        
        has_vowel = False
        has_consonant = False
        
        for c in word:
            if not c.isalnum():
                return False
            if c.isalpha():
                if c in VOWELS:
                    has_vowel = True
                else:
                    has_consonant = True
        
        return has_vowel and has_consonant
