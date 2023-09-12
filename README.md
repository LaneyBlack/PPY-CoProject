# PPY-CoProject
Cat Farm Game (RPG) - Semester Project on Python (PJATK)

**This project was made by Palina Brahina (polya) and Anton Reut (Laney_Black)**

The game was written in pygame.

The project has /plan.txt file where you can see our resposibilities and what we did:
   ![image](https://github.com/LaneyBlack/PPY-CoProject/assets/44290162/35f1c722-fe6b-49c3-9552-e1f394764189)


**The project features:**
1) Entry window:
   
   ![image](https://github.com/LaneyBlack/PPY-CoProject/assets/44290162/aed1e411-5f40-466b-a08c-f5bc262bae01)
   
2) Login or Registration window (all passwords are incrypted), those windows are showing exception messages for the user:

   ![image](https://github.com/LaneyBlack/PPY-CoProject/assets/44290162/84835e29-9199-4457-bea8-78e41cb8d302)
   
3) The Game Window:
   
   ![image](https://github.com/LaneyBlack/PPY-CoProject/assets/44290162/7fab948f-ec17-4b08-bfaf-a8423fd455b5)
   
4) Character has a standing animation which is directed into last moved side of the screen:
   
  ![image](https://github.com/LaneyBlack/PPY-CoProject/assets/44290162/cf493d0e-3e4f-4794-94c4-10fdc94eabe3)
  ![image](https://github.com/LaneyBlack/PPY-CoProject/assets/44290162/b3f50644-3728-4cd1-85fd-3cb54f3e588c)

5) Character has movement animation:

  ![image](https://github.com/LaneyBlack/PPY-CoProject/assets/44290162/bdae09ac-8454-4aba-a694-7507d0d7e806)
  ![image](https://github.com/LaneyBlack/PPY-CoProject/assets/44290162/90a2792b-d33a-47ec-994d-7ddfc8692d1e)

6) Character collides with edges of the map, trees and bushes and has no collision with flowers and random stuff on the floor.

   ![image](https://github.com/LaneyBlack/PPY-CoProject/assets/44290162/40086acf-eeac-43b6-9528-eead9a042229)
   ![image](https://github.com/LaneyBlack/PPY-CoProject/assets/44290162/7bffb2eb-2979-4de9-a92c-7b00a71d8581)

7) Character has a pouring water animation, cause we planned to add a plant mechanics later
   
  ![image](https://github.com/LaneyBlack/PPY-CoProject/assets/44290162/8af6f573-ccc9-4a5a-ad84-621472ff5214)

**The project is divided into folders by the project structure.**
1) /assets - all images of the GUI: player animations (/animations), buttons(/buttons), base font, textures, map guidelines and other.
2) /doc - the full documentaion generated using Sphinx and Rinoh
3) /src - the code folder
   It is divide into folders and files
   1) /db - database with all the players info, to later store their progress and build a leader scoreboard
   2) /entity - connection between all the textures, their collisions and animations.
   3) /pages - where every page is described so the pygame could have built it
   4) debug.py - using this file you can turn on developer mode to see what is going on in the programm
   5) main.py - that's where the build of the project is happening
   6) settings.py - file with all the project settings (variables) like folder paths to textures, window colors, size and title, texture sizes and other.
   7) support.py - here are functions, that import folders and the game layout


