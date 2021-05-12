import webbrowser

class OpenDocumentationIntents(object):
    def open_documentation_intents(self, user_input):
        # Open popular p/l documentation websites
        # Implement website search in future
        if user_input.split()[1] == "C++":
            webbrowser.open('http://www.cplusplus.com/')
            return False
        elif user_input.split()[1] == "Python":
            webbrowser.open('https://docs.python.org/3/')
            return False
        elif user_input.split()[1] == "Java":
            webbrowser.open('https://docs.oracle.com/en/java/')
            return False
        elif user_input.split()[1] == "terminal":
            subprocess.run(["C:\\Program Files\\Git\\git-bash.exe"])
            return False




