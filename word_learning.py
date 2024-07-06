import random

class WordLearning:
    def __init__(self):
        self.words = {
            'apple': 'a fruit',
            'run': 'to move quickly',
            'happy': 'feeling or showing pleasure'
        }

    def start(self):
        print("\nWord Learning")
        while True:
            print("\n1. Flashcards")
            print("2. Quiz")
            print("3. Back to main menu")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.flashcards()
            elif choice == '2':
                self.quiz()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def flashcards(self):
        words = list(self.words.keys())
        random.shuffle(words)
        
        for word in words:
            print(f"\nWord: {word}")
            input("Press Enter to see the meaning...")
            print(f"Meaning: {self.words[word]}")
    
    def quiz(self):
        words = list(self.words.keys())
        random.shuffle(words)
        correct = 0
        
        for word in words:
            answer = input(f"\nWhat is the meaning of '{word}'? ")
            if answer.lower() == self.words[word].lower():
                print("Correct!")
                correct += 1
            else:
                print(f"Incorrect! The correct meaning is: {self.words[word]}")
        
        print(f"\nQuiz over! You got {correct}/{len(words)} correct.")
