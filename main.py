from word_learning import WordLearning
from sentence_practice import SentencePractice
from grammar_learning import GrammarLearning

def main():
    print("Welcome to TeachEnglish!")
    while True:
        print("\nChoose an option:")
        print("1. Word Learning")
        print("2. Sentence Practice")
        print("3. Grammar Learning")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            WordLearning().start()
        elif choice == '2':
            SentencePractice().start()
        elif choice == '3':
            GrammarLearning().start()
        elif choice == '4':
            print("Thank you for using TeachEnglish!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
