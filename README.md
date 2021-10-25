**Program Overviews**
- Generate_Game_Info.py
This program scrapes information for the top 200 games on Steam's "All Products Page." In doing so, it collects information such as the title, genres, price, release date, description, trailer link, and steam link for each game. The program then places all of this information in a .csv file called 'games.csv' which will be used by Game_Suggester.py to help the user find a new game to play.

- Game_Suggester.py
This program asks the user for their video game genre preferences, as well as how much they are willing to pay for a new video game. After receiving that information, the program parses through the 'games.csv' file and collects all games that match the user's criteria. The program will then display all relevant information for the highest ranked game that matches all of the user's preferences. This includes information like the game's title, genres, price, release date, description, trailer link, and steam link. The user can then decide whether or not they like the game. If yes, the program will ask if the user wants to find another game with different parameters, or quit the program altogether. If no, the program will display all relevant information for the next-highest ranked game that meets all of the user's criteria. This process will continue until the user finds a game that they like, or there are no more games that meet the user's criteria. At this point the program will ask if the user wants to find another game with different parameters, or quit the program altogether.

**How to Run the Programs**
1.  If you have not done so already, please install Anaconda Python 3.7.
        Link: https://www.anaconda.com/products/individual 
        
        Please select Python 3.7 for your applicable operating system. Selecting Python 2.7 will result in the program failing to run.
  
2.  If you have not done so already, please install Microsoft Visual Studio Code.
        Link: https://code.visualstudio.com/

3.  Open GameSuggester (To Be Shared) in Visual Studio Code
    1. Open Visual Studio Code
    2. Click "Explorer Tab" on top left of application and select "Open Folder".
    3. Select "GameSuggester" folder and click "Open".
    4. If a pop-up appears in the bottom right corner of the application asking for permission to install Python, allow it do do so.

4.  Run the Program.
    1. Ensure that both .py files and games.csv are in the same directory and that the user's python path is directed to that directory as well.
    2. Generate up-to-date games list. (Optional)
        1. Select Generate_Game_Info.py from the GameSuggester (To Be Shared) folder.
        2. Select the green "play button" symbol in the top right corner of the application.
            - Although it will appear as though nothing is happening, simply wait 2-3 minutes for 'games.csv' to be updated with up-to-date game information.

    3. Run the Suggester
        1. Select Game_Suggester.py from the GameSuggester (To Be Shared) folder.
        2. Select the green "play button" symbol in the top right corner of the application.
        3. Use the Program:
            1. When prompted, enter desired genres (one at a time) from the given list, follow each input by pressing the 'Enter' key.
                - When all desired genres have been entered, type 'done' to move on.
            2. When prompted, enter the maximum price ($USD) that you are willing to pay for the game, follow input by pressing the 'Enter' key.
            3. Program will output highest ranked game that meets all of the user's preferences.
                - Program will output title, genres, price, release date, description, trailer link, and steam link for the game.
            4. Program will ask the user if they like the game, enter 'Y' for yes or 'N' for no.
                1. If 'Y' is entered, the program will then ask if the user would like to find another game with new parameters, or quit the program.
                    - If 'Y' is entered, the program will start over by asking for new parameters and will behave in the exact same manner as before.
                    - If 'N' is entered, the program will end.
                2. If 'N' is entered, the program will continously display games the meet the user's preferences (in order of rank) until a game that the user likes is found, or no more games meet the user's preferences.
                    - If 'Y' is entered when the user is asked if they like one of the games, refer to step 4.1
                    - If 'N' is entered until there are no more games that meet the user's preferences, the program will output a message stating that there are no more games that match the user's desired parameters and will ask the user if they'd like to find another game with new parameters, or quit the program.
                        - If 'Y' is entered, the program will start over by asking for parameters and behave in the exact same manner as before.
                        - If 'N' is entered, the program will end.

***Have Fun!***