3/9/2024
Implemented sprites and player movement, though the system was primitive and could only allow the player to move when the arrow keys are tapped, not pressed.


3/11/2024
Fixed the movement issue by using booleans to determine whether a key is pressed or not, and move indefinitely until the key is no longer pressed. This may cause issues in the future, though I can't predict what the specifics would be. I'll have to fix them once they arise.


3/12/2024
Created multiple creature objects, implemented a dictionary containing their name and the corresponding main sprite. This is preparation for drawing multiple creatures on the screen at the same time, though I'm running into issues implementing this. It seems to have something to do with rects, so it might not be difficult to fix.


3/13/2024
Cleaned the main file, organized the folders. Put gif_test.gif and harold.png in "images", from "placeholder_images". I attempted to modualize, however I continued running into the  problem of circular dependancy. I decided it would be beneficial to study this more and come back at a later time so that I can focus more on fixing other problems. I ran into issues adding multiple creatures on screen, though the problem was simply that I wasn't adding them correctly to the sprite group and it ended up working.

Summary:
-Added a readme and this devlog. 
-Added the ability to draw multiple objects (creatures) on the screen, with working collision. 
-Simplified player movement into functions.
-Organized the main file.

3/14/2024
Created tile images and attempted to create a system to blit them across the screen. Originally tried using sprites, but switched to simply blitting them due to better performance. An algorithm to do this was successfully made using two stacking for loops, however, creating blocks with collision may still present as a problem. These may have to be sprites.

3/15/2024
Began working on creating specific tiles with collision, started using a similar loop that was used to make a box of wall tiles, but it wouldn't give any room for customization. Also, the biggest problem is that the player will move from room to room using doors, which wouldn't work with the system I wanted to use. I'd have to use only ONE kind of block and I wouldn't be able to choose where they go. What if I don't want the room to be a square and I wanted it to be a circle? How will they leave if there's no way to create an "exit"?

I'm now planning on implementing a system that allows me to create and store tiles in a list. 

3/26/2024
Decided to not go forward with creating a collision system for maps, since it's more of a priority to have a working prototype ready. Instead, I will disallow the player to move off-screen as a temporary fix. For today, I'm simply going to implement the ability for the player to interact with sprites using "e".

3/28/2024
Successfully added the ability to use "e" to prompt a dialogue box to appear. However, it it ONLY triggered by the player pressing said button, not by it's intended purpose of talking to the creatures. In other words, simply pressing this button will show someone "talking." The next priority is to implement a system where if the player is within a specific range of a creature, THEN pressing "e" reveals a dialogue window.

Summary for this repository:
-Created a function that automatically renders tiles across the entire screen
-Cleaned up and organized some code in the main file, removed some unnecessary lines.
-The appearance of a dialogue box once the player pressed "e".

3/29/2024
Added some functions that basically only allowed a dialogue box to appear when the player is within a certain range of a creature. However, it only seems to be working with a single creature-- there's a bug somewhere that I need to find. I also separated the game loop from the main file to make it more clean.

Another bug appeared, now the player can move when the dialogue box appears which... shouldn't happen.

3/30/2024
As it turned out, the second bug was caused from the implementation of global variables. These were taken out and instead added into a config file; now instead of globals, the variable is imported from this file.

The first bug was due to problems with another I had created called find_distance(). As it turns out, the way if and else statements were used caused the loop to break after only detecting the first creature. 

Other than fixing these bugs, I cleaned up the files (and have plans for how I want to better organize them in the future, I might work on this soon), and made it so that distance_check checks for a CREATURE and not the difference between them. I tried making a very rough dialogue tree but... it's way more complex than I thought and it kept throwing errors, so I reverted it back to what it was before. It now works again, and I need to step back and figure out a strategy as to why my mini-dialogue tree didn't work. The error message was extremely complex but supposedly it traced back to dialogue_box.rebuild() in main. The syntax in the JSON file is correct, which is another reason why I suspect something in dialogue_box_trigger causing it. I think I need to redo the way the boxes are rendered, but I need to think of a clear plan first and foremost.

Next time, I will instead focus on not letting the player move off screen. For the long term, though, I think I should rework some things to include game states since after researching, they seem to be extremely important and it'll only get harder to implement the more things I add.

4/8/2024
After sleeping and waking up with a clear head this morning, I think I know how to tackle the game state problem. I think I do need to make each screen a different class but... oh no, this will be a huge pain and I'll have to rewrite a lot of core parts of the game. But I think this might be the best way to handle it. I also just rememebered that wall tiles technically WORK, I just don't have a way to map them out, so that's another thing I could research how to do.

Summary for this repository:
-Fixed bugs, removed usage of global variables in some functions. Optimized some functions.
-Implemented a working dialogue box, displaying text that is unique to each character.