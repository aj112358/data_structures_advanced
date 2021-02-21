"""A module that implements a Caesar cipher, but allows you to define shifts other than three (taken from book).

Created By: AJ Singh
Date: Feb 21, 2021
"""


class CaesarCipher:
    """Class for doing encryption and decryption using a simple substitution cipher."""
    
    def __init__(self, shift):
        """Construct the encoder and decoder strings for the given shift."""

        # Initializing temporary arrays for encryption and decryption, respectively.
        encoder = [None] * 26
        decoder = [None] * 26

        # Constructing the arrays.
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord("A"))
            decoder[k] = chr((k - shift) % 26 + ord("A"))

        # Converting to string (to make immutable).
        self._forward = "".join(encoder)
        self._backward = "".join(decoder)
        
    def encrypt(self, plaintext):
        """Return string representation of ciphertext."""
        return self._transform(plaintext, self._forward)
    
    def decrypt(self, ciphertext):
        """Return string representation of plaintext."""
        return self._transform(ciphertext, self._backward)

    def _transform(self, original, code):
        """Utility to perform a transformation, based on a given code alphabet.

        @param original: String to convert (can be either plaintext or ciphertext).
        @param code:     Alphabet we use for conversion (either encoder or decoder)
        """

        msg = list(original)
        for k in range(len(msg)):

            if msg[k].isupper():
                j = ord(msg[k]) - ord("A")  # Determining correct index for new character.
                msg[k] = code[j]

        return "".join(msg)


if __name__ == "__main__":

    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE S."
    coded = cipher.encrypt(message)
    print('Secret:', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)
