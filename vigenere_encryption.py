import string


def generate_vigenere_matrix():
    """
    generating vigenere matrix
    """
    all_letters = string.ascii_lowercase
    # time 2 otherwise we would get out of range
    all_letters = all_letters * 2
    matrix = []

    for i in range(26):
        matrix.append([])
        for j in range(26):
            matrix[i].append(all_letters[j + i])
    return matrix


def word_key(word, key):
    """
    creating key stream - it means we have to repeat the key as many times
    as is the number of characters in our plaintext
    """
    number_of_keys = len(word) // len(key)
    remainder = len(word) - (number_of_keys * len(key))
    return key * number_of_keys + key[:remainder]


def return_letter_index(letter):
    """
    optimal will be just use hashtable
    keys are letters
    values are indexes
    """
    letters = string.ascii_lowercase
    letters_indices = {letters[i]: i for i in range(len(letters))}
    return letters_indices[letter]


def vigenere_encryptor(plaintext, key):
    """
    the main function
    """
    vigenere_matrix = generate_vigenere_matrix()
    keystream = word_key(plaintext, key)
    encoded_text = ''
    for number in range(len(plaintext)):
        row = return_letter_index(plaintext[number])
        col = return_letter_index(keystream[number])
        decode_letter = vigenere_matrix[row][col]
        encoded_text += decode_letter
    return encoded_text


