import webbrowser

class WebSearchIntents():
    def web_search_intents(self, user_input):
        # Send result.text through google search in last char is a '?'
        if user_input[-1] == '?':
            webbrowser.open('https://www.google.com/search?q={}'.format(user_input))

        # Search keyword function
        # Search google ignoring first word
        else:
            search_for = ' '.join(user_input.split()[1:])
            webbrowser.open('https://www.google.com/search?q={}'.format(search_for))
