"""
Implementation of Shnanon Encoding
Author: Aaryaman Jaising
Date: Tuesday March 18, 2025
"""
import math
################################################################################
# CLASSES
################################################################################

class Shannon:


    def __init__(self, char_probs):
        """
        Constructor that takes in character probabilities and creates shannon encoding in the shannon.encoder 
        decoder in shannon.decoder
        sorted char_probs in shannon.char_probs
        """
        self.char_probs = dict(sorted(char_probs.items(),key = lambda x:x[1],reverse=True))
        self.cum_probs = []
        self.number_digits = []
        tmp = 0
        self.encoder = {}
        self.decoder = {}

        for key, value in self.char_probs.items():
            self.cum_probs.append(tmp)
            tmp+=value
            self.number_digits.append(math.ceil(-math.log2(value)))
            digits = self.helper_binary(self.cum_probs[-1],self.number_digits[-1])
            self.encoder[key] = digits
            self.decoder[digits] = key
        

        # TODO
        pass
    
    def helper_binary(self,cum_prob,num_digits):
        """
        Converts cumulative probability into binary string up to limit length of number of digits
        """
        ans = ""
        for i in range(num_digits):
            cur = 0.5**(i+1)
            if cum_prob >= cur:
                ans+="1"
                cum_prob -= cur
            else:
                ans+='0'
        return ans


    def encode(self, encode_str):
        """
        Trivial encoding per character using encoder dictioary
        """
        ans = ""
        for char in encode_str:
            ans = ans+ self.encoder[char]
        return ans
        


    def decode(self,decode_str):
        """
        decodes string using two pointer approach for decoder method
        """
        ans = ""
        l = 0
        r=1
        while l < len(decode_str):
            if decode_str[l:r] in self.decoder:
                ans = ans+ self.decoder[decode_str[l:r]]
                l = r
                r = r+1
            else:
                r+=1
        return ans


################################################################################
# MAIN
################################################################################

def main():
    """
    testing the shannon object
    """
    char_probs = {"A": 0.25, "B": 0.125, "C": 0.5, "D": 0.125}
    shannon = Shannon(char_probs)
    print(f"Shannon Encoder: {shannon.encoder}")
    orig = "ABAACDDBACCDAAABDBBABCDDCBA"
    encoded = shannon.encode(orig)
    print(f"Encoded String {encoded}")
    decoded = shannon.decode(encoded)
    print(f"Decoded String: {decoded}")
    assert decoded == orig
    print("Assertion Succesful")
    pass

if __name__ == "__main__":
    main()
