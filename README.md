 # What is aYo? 

    aYo is an application to improve a programmer's efficiency by providing voice-command quick access to programming language
    documentation and other online web-searching. The purpose is to help quickly answer questions mid development without
    interrupting the flow of thought. Additionally, aYo provides fast and easy access to learning materials and the official
    documentation of various languages in addition to common voice assistant functionality, like playing music. aYo is designed 
    to take advantage of Microsoft's Cognitive Services for seamless implementation. What sets aYo apart from its competition 
    will be its focus on aiding Software Developers; unlike Alexa, Cortana, Google Assistant and Siri which were designed for 
    more general purposes.   

 # Who is aYo designed for?   

    In general, aYo is designed to be a helpful assistant to anyone who downloads it. However, its focus is on software 
    developers and as such many of its unique features are focused on enhancing the software development process. With language 
    documentation, music, program execution, and real time query searching over the internet, aYo is made to be a tool that 
    empowers software developers during the development process allowing them to complete their work in a more efficient manner 
    while still providing the basic tools most voice assistants have.  

 # Compatibility: 

    Windows 
 
 # Installation  

   # Language: Python 

        aYo is designed to run in Python version 3.9.2 

        To download the latest version of Python go to this website: https://www.python.org/downloads/ 

        You can check your current version of python with the:   python3 --version   command in your console/terminal. 

   # Python packages to download and the version aYo uses:  

        Downloading a specific package in python can be done though these simple steps:  

         1) Open a Console/Terminal window and make sure you are currently in the root file directory.  

         2) type pip3 install "insert package name here". An example of the command to install playsound is shown below: 

            pip3 install playsound 

         3) Wait. It usually takes a few seconds to fetch the package and begin installing.  

         4) Once it is done installing, check that it was successful by typing pip3 list into your terminal. 
         After hitting enter, this will show a list of all the python packages you have downloaded and their version number.  

        Here is the list of packages aYo needs to function.  

        Package Name                         Version 
        ----------------------------------   -------       
        azure-cognitiveservices-speech       1.16.0 
        playsound                            1.2.2 
        PyQt5_sip                            12.8.1 
        PyYAML                               5.4.1 
        requests                             2.25.1 
        spotipy                              2.18.0 
        word2number                          1.1 


        If you need to check your packages, the     pip3 list      command will show you 
        the name and version number of all the python packages you have downloaded. 


 # aYo File Hierarchy:  
    aYo 
        azure 
            speech_settings 
                en_US 
                    Guy.xml 
                    Jenny.xml 
                en_US 
                    Dalia.xml 
                    Jorge.xml 
            get_query.py 
            microphone_input.py 
            text_to_speach.py 
        config 
            ayo.ini 
            config.ini 
        data 
            alarm.wav 
            intro.wav
            sources.txt 
            warning_azure_api_missing.mp3
            warning_openweather_api_missing.mp3
        database 
            aYo_database.py 
            aYo_decode.py 
            aYo_encode.py 
            aYo_pw_database.csv 
            aYo_un_database.csv 
        dialouge 
            en_US  
                conversation
                    ayo-functions.yami
                    bye.yami
                    credits.yaml
                    fun-facts.yaml
                    greetings.yaml
                    how-am-i.yaml
                    jokes.yaml
                    thanks.yaml
                    unknown.yaml
                    user-apologies.yaml
                intents
                    alarm-timer.yaml
                    conversation-queries.yaml
                    music.yaml
                    user-queries.yaml
                    verbs.yaml
                    weather.yaml
                skills
                    alarm.yami 
                    introductions.yami
                    stopwatch.yami
                    timer.yami
                    weather.yami
                default-voices.yami 
                time-words.yami 
            en_US 
                default-voices.yami 
                stopwatch.yami 
                time-words.yami 
                user-queries.yami     
        intents 
            alarm_timer_intents.py 
            conversation_intents.py
            intents.py 
            music_intents.py 
            open_documentation_intents.py 
            search_documentation_intents.py 
            stopwatch_intents.py 
            weather_intents.py 
            web_search_intents.py 
        skills 
            alarm_skill.py 
            introduction_skill.py
            music_skills.py 
            random_element_skill.py
            stopwatch_skill.py 
            timer_skill.py 
            weather_skill.py 
        ui 
            ui_classes 
                __init__.py 
                ayo_body.py 
                ayo_login.py 
                languages_window.py 
                new_user_window.py 
                query_worker.py
                recover_password_window.py 
                settings_window.py 
                worker.py
            ui_files 
                aYo_body.ui 
                aYo.ui 
                languages.ui 
                new_user.ui 
                recovery.ui 
                settings.ui 
            aYo_ui_main.py 
        utils 
            find_matching_word.py 
            get_time.py 
            import_dialouge.py 
            readable_time_output.py 
        __main__.py 
        requirements.txt 

 # Running aYo after installation:

    1) Open a command prompt/terminal window. 

    2) Navigate into the aYo folder 

    3) Navigate into the ui folder 

    4) Run the command     python3 -i aYo_ui_main.py 

 # Obtaining API keys

   # Weather API
        1) Make a free account on https://home.openweathermap.org/ 
        2) Make sure you are signed in and go to "My API Keys" which can be found in a tab under your profile name
        3) Type a name into the window next to the button generate key, and press the generate key button. 
        4) Wait for a bit before using the key. It can take up to a few hours for a key to be activated. 

   # Speech to Text API
        1) Make an account on Azure portal at https://portal.azure.com/#home
        2) Create a resource.
        3) Search 'speech'.
        4) In the search results, select 'Speech'.
        5) Fill in the information, then select 'Create'.
        6) On the Azure portal homepage, select the resource you created.
        7) on the left pane, under RESOURCE MANAGEMENT, select 'Keys and Endpoint'.

        8) Or follow this guide: https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/overview#try-the-speech-service-for-free


 # aYo user-interface buttons: 

	With how aYo works using Microsoft azure speech to text Api, there will be a 15 second lockout time 
    on many of aYo’s buttons to prevent crashing issues.  

 # aYo Features and how to use them  

   # Documentation Support:  

        Keyword(s): Programing language you want to search 

        Some basic queries for documentation are:
            _language_ arrays
            _language_ lists


   # Web-Searching:  

        Keyword(s): Search 

        The basic format for web-based query searching is: 
            Search _whatever you are searching for_

   # Spotify: 

        Keyword(s): Play, Shuffle, Resume, Pause, Next, Previous, Skip  

        Some basic queries for music include:  
            Play _band name here_. 
            Skip 
            Next song 
            Pause song. 
            Skip 
            Shuffle	 

   # Alarms/Timers/Stopwatch: 

        Keyword(s): Alarm, Timer, Stopwatch, Start, Stop, Reset, A.M., P.M. 

        Some basic queries for alarms/timers/stopwatch include:  
            Set timer for _time here_ 
            Stop timer 
            Set alarm for _time here_ 
            Stop alarm 
            Start stopwatch.  
            Reset stopwatch 

   # Weather Information:  
        Keyword(s): weather in, weather for 
 	    
        A basic query for weather is: 
            What is the weather in _city name here_	 

 # Known Bugs:
    Recover password button has no functionality

    aYo only works right now in work mode

 

 

 
 
 

 
