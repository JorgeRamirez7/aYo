import webbrowser

class SearchDocumentationIntents():
    def search_documentation_intents(self, user_input):
        # P/L name as keyword
        # Automatically searches documentation website for following words
        if user_input.split()[0] == "C++":
            search_for = ' '.join(user_input.split()[1:])
            webbrowser.open('http://www.cplusplus.com/search.do?q={}'.format(search_for))

        elif user_input.split()[0] == "Python":
            search_for = ' '.join(user_input.split()[1:])
            webbrowser.open('https://docs.python.org/3/search.html?q={}'.format(search_for))
