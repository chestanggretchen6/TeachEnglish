class GrammarLearning:
    def __init__(self):
        self.rules = {
            'Present Simple': 'Used for regular actions or facts.',
            'Past Simple': 'Used for actions that happened at a specific time in the past.'
        }

    def start(self):
        print("\nGrammar Learning")
        while True:
            print("\n1. View Rules")
            print("2. Back to main menu")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.view_rules()
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please try again.")

    def view_rules(self):
        for rule, description in self.rules.items():
            print(f"\n{rule}: {description}")
