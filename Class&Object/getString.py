class StringManipulator:    
    def get_string(self):
        self.text = input("Enter a string: ")
    def print_string(self):
            print(self.text.upper())
    def reverse_words(self):
            words = self.text.split()
            reversed_words = ' '.join(words[::-1])
            print(reversed_words.lower())

ob = StringManipulator()
ob.get_string()
ob.print_string()
ob.reverse_words()
