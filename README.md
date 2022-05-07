Welcome to my Whatsapp web AI application;

<<< WAVEIGL BOT APPLICATION >> 

Please follow the instructions above before executing the main.py file;

PLEASE NOTE THAT THIS PROJECT WAS MADE ONLY FOR EDUCATIONAL PURPOSES;

[0] Pre-Instalations*
    1. Before executing the main.py file, you should have Python 3 installed on your computer, otherwise the modules won't load and it will return an error.
    2. If you don't have Python 3 installed on your machine by default (Like Windows), you should visit the Microsoft Store or Python's official website and install python3 on your machine.
    3. You will also need an IDE for manipulating this code, but this is totally optional and not needed.
        #. Recommended IDE: Visual Studio Code (Stable Version), Visual Studio or Notepad++.

[1] Configurating your browser and your browser Driver*
    Line 17: >>> ndriver = webdriver.Chrome('C:/Users/ucdhs/Downloads/chromedriver_win32/chromedriver.exe')
    0. You should replace 'webdriver.Chrome() [module, function]' to your respectively browser, and the driver.
        #. If you are using chrome, you just need to replace 'ucdhs' to your Computer's username.
        #. Please note that this repository comes with a folder called 'chromedriver_win32', please replace that to your Downloads section.
            This folder contains the Chrome Browser Driver for version 101.
        #. If you are using any other Chrome version rather than 101, you should visit https://chromedriver.chromium.org/downloads and select your Chrome version.
    1. If you aren't using chrome as your main browser, you should! install it's respectively driver, otherwise it will return an error at your console]
        #. Opera: https://github.com/operasoftware/operachromiumdriver/releases
        #. Firefox: https://github.com/mozilla/geckodriver/releases 

[2] Configurating your keywords
    After line 62 you can see a few tuples with words in it, and that is the words that the Artificial Intelligence is going to recognize, as you can see below at the for statements, iterabling every word in the tuple followed by an if statement, whose checks if the word in the tuple is a part of the Last message sent by the contact.
    You can configurate it freely, along with the .reply() functions inside of the if statements with random messages with it.
    So it basically works like this:
        1. It checks the message that your Whatsapp Contact just sent
        2. It checks the words inside of the message
        3. If the word inside of the message was found, then reply it with another message.
    You can add time.sleep() wherever you want to give it a more realistic detail to the AI (so it gives an impression that the bot is typing something instead of just sending the message anyways.). 

[3] Setting up the bot
    At line 24, there is a time.sleep delay for you to login with your Whatsapp Account, you can manipulate this time.sleep command whenever you want to give it more time to login if you are slow.
    At line 26 you will be seeing a config input, you should provide a number between 1-5 so the AI can read that messages before sending it, please provide it  an Int value (Number value).

[4] Stop the bot
    You can stop the AI from working, doing a Ctrl+C (^C) combo in the cmd (Keyboard Interrupt Method) or just closing it.

[#]Future updates
    In future updates i may add some new features to the bot, such as:
        1. Banned contacts, tou can ban contacts like your mom, so it doesn't check and auto-answears it with something that you won't like
        2. Inside cmd configurations for your bot, like a setup.py file, that automatically returns the values to main.py, so you don't need to edit it inside of an IDE;