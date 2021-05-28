"""Search for a user query through existing programming language documentation available online"""
import webbrowser


class SearchDocumentationIntents():
    # P/L name as keyword
    # Automatically searches documentation website for following words
    def search_documentation_intents(self, user_input):
        language = user_input.split()[0]
        language = language.lower()

        search_for = '+'.join(user_input.split()[1:])
        
        if language == "c++":
            webbrowser.open('http://www.cplusplus.com/search.do?q={}'.format(search_for))

        elif language == "python":
            webbrowser.open('https://docs.python.org/3/search.html?q={}'.format(search_for))
        
        elif language == "javascript" or language == "html" or language == "css":
            webbrowser.open('https://developer.mozilla.org/en-US/search?q={}'.format(search_for))
        
        else:
            print("Language not currently supported")
