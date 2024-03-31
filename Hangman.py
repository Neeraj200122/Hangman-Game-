import random

class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        encrypted_text = ''
        for i in range(self.key):
            for j in range(i, len(plaintext), self.key):
                encrypted_text += plaintext[j]
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = [''] * len(ciphertext)
        idx = 0
        for i in range(self.key):
            for j in range(i, len(ciphertext), self.key):
                decrypted_text[j] = ciphertext[idx]
                idx += 1
        return ''.join(decrypted_text)

class HangmanGame:
    def __init__(self, words, attempts=6):
        self.words = words
        self.attempts = attempts

    def choose_word(self):
        return random.choice(self.words)

    def display_word(self, word, guessed_letters):
        displayed_word = ''
        for letter in word:
            if letter in guessed_letters:
                displayed_word += letter + ' '
            else:
                displayed_word += '_ '
        return displayed_word.strip()

    def play(self):
        print("\nWelcome to Hangman!")
        word = self.choose_word()
        guessed_letters = set()
        while self.attempts > 0:
            print("\nAttempts left:", self.attempts)
            print("Word:", self.display_word(word, guessed_letters))
            guess = input("Guess a letter: ").upper()
            if guess in guessed_letters:
                print("You already guessed that letter.")
            else:
                guessed_letters.add(guess)
                if guess not in word:
                    self.attempts -= 1
                    print("Incorrect guess!")
                else:
                    print("Correct guess!")
                if all(letter in guessed_letters for letter in word):
                    print("Congratulations! You guessed the word:", word)
                    return
        print("Sorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    while True:
        choice = input("\nEnter 'E' for encryption and decryption, 'H' for Hangman game, or 'Q' to quit: ").upper()

        if choice == 'E':
            key = int(input("Enter the cipher key: "))
            message = input("Enter the message to encrypt and decrypt: ")
            cipher = TranspositionCipher(key)
            encrypted_message = cipher.encrypt(message)
            print("\nEncrypted message:", encrypted_message)
            decrypted_message = cipher.decrypt(encrypted_message)
            print("Decrypted message:", decrypted_message)
        elif choice == 'H':
            words = ["PYTHON", "PROGRAMMING", "HANGMAN", "COMPUTER", "SCIENCE"]
            game = HangmanGame(words)
            game.play()
        elif choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'E', 'H', or 'Q'.")
