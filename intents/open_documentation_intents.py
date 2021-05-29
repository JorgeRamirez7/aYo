import webbrowser

class OpenDocumentationIntents():
    """Open documentation website for a specific programming language"""

    def open_documentation_intents(self, user_input):
        language = ' '.join(user_input.split()[1:])
        language = language.lower()

        # Open popular p/l documentation websites
        # Implement website search in future
        if language == "c++":
            webbrowser.open('http://www.cplusplus.com/')

        elif language == "python":
            webbrowser.open('https://docs.python.org/3/')

        elif language == "java":
            webbrowser.open('https://docs.oracle.com/en/java/')

        elif language == "javascript":
            webbrowser.open('https://developer.mozilla.org/en-US/docs/Web/JavaScript')

        elif language == "html":
            webbrowser.open('https://developer.mozilla.org/en-US/docs/Web/HTML')

        elif language == "css":
            webbrowser.open('https://developer.mozilla.org/en-US/docs/Web/CSS')

        elif language == "go":
            webbrowser.open('https://golang.org/ref/spec')

        elif language == "c#" or language == "c sharp":
            webbrowser.open('https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/')

        elif language == "c":
            webbrowser.open('https://docs.microsoft.com/en-us/cpp/c-language/c-language-reference?view=msvc-160')

        elif language == "ruby":
            webbrowser.open('https://docs.ruby-lang.org/en/master/')

        elif language == "swift":
            webbrowser.open('https://swift.org/documentation/')
            
        else:
            print("Language not currently supported")
        
