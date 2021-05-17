"""Open documentation website for a specific programming language"""
import webbrowser

class OpenDocumentationIntents():
    def open_documentation_intents(self, user_input):
        # Open popular p/l documentation websites
        # Implement website search in future
        if user_input.split()[1] == "C++":
            webbrowser.open('http://www.cplusplus.com/')
        elif user_input.split()[1] == "Python":
            webbrowser.open('https://docs.python.org/3/')
        elif user_input.split()[1] == "Java":
            webbrowser.open('https://docs.oracle.com/en/java/')
