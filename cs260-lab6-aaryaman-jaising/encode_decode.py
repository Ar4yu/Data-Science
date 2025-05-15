"""
Testing the shannon class and performing encoding and decoding
Author: Aaryaman Jaising
Date: Tuesday, March 18th, 2025
"""

import Shannon

################################################################################
# MAIN
################################################################################

def main():
    # Read in twitter train and train shannon encoder
    train_str = read_file("data/vaccine_tweets_codes_source.csv",encode="ISO-8859-1")
    char_prob = create_char_prob(train_str)
    shannon = Shannon.Shannon(char_prob)
    first_two = dict(list(shannon.encoder.items())[:2])
    print(f"Encoder: {first_two}")
    
    test_str = read_file("data/vaccine_tweets_to_encode.csv",encode="ISO-8859-1")
    encoded_str = shannon.encode(test_str)
    write_file("output/vaccine_tweets_encoded.txt",encoded_str)
    #reveal secret
    secret = read_file("data/secrete_message_to_decode.txt")
    secret_revealed = shannon.decode(secret)
    write_file("output/secret_message_decoded.txt",secret_revealed)

    """
    fact
    the australian giant cuttlefish is the world's largest species of cuttlefish.
    """

    #code for average number of bits per character using weighted average
    print(f"Number of Unique Characters in Twitter Dataset: {len(shannon.encoder)}")
    print(f"Average Number of bits per character: {sum(val*len(shannon.encoder[key]) for key, val in shannon.char_probs.items())}")

################################################################################
# HELPER FUNCTIONS
################################################################################

def create_char_prob(str):
    """
    This function takes in the string and returns the character probability dictionary
    """
    char_prob = {}
    total = len(str)
    for ch in str:
        if ch in char_prob:
            char_prob[ch] +=1
        else:
            char_prob[ch] = 1
    for key in char_prob:
        char_prob[key] = char_prob[key]/total

    return char_prob



def read_file(filename, encode="utf-8"):
    """
    This function reads in the contents of the file at the filename (string).
    The contents are returned as a string.
    """
    to_ret = ""
    file = open(filename, 'r', encoding=encode, newline="")
    for line in file:
        to_ret = to_ret + line
    file.close()
    return to_ret

def write_file(filename, output, encode="utf-8"):
    """
    This function writes output (string) to the file at the filename (string).
    """
    file = open(filename, 'w', newline="", encoding=encode)
    file.write(output)
    file.close()

if __name__ == "__main__":
    main()
