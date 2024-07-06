class SentencePractice:
    def __init__(self):
        self.sentences = [
            {'sentence': 'I ___ to the store.', 'answer': 'went'},
            {'sentence': 'She is very ___.', 'answer': 'happy'}
        ]

    def start(self):
        print("\nSentence Practice")
        while True:
            print("\n1. Fill in the blanks")
            print("2. Back to main menu")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.fill_in_the_blanks()
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please try again.")

    def fill_in_the_blanks(self):
        correct = 0
        for item in self.sentences:
            answer = input(f"\n{item['sentence']} ")
            if answer.lower() == item['answer']:
                print("Correct!")
                correct += 1
            else:
                print(f"Incorrect! The correct answer is: {item['answer']}")
        
        print(f"\nPractice over! You got {correct}/{len(self.sentences)} correct.")
