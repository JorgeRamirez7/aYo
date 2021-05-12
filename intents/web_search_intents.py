import webbrowser

class WebSearchIntents():
    def web_search_intents(self, user_input):
        # Send result.text through google search in last char is a '?'
        if user_input[-1] == '?':
            webbrowser.open('https://www.google.com/search?q={}'.format(result.text))
            return False

        # Search keyword function
        # Search google ignoring first word
        elif user_input.split()[0] == "Search":
            searchFor = ' '.join(user_input.split()[1:])
            webbrowser.open('https://www.google.com/search?q={}'.format(searchFor))
            return False
