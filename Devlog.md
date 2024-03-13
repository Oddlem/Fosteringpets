3/9/2024
Implemented sprites and player movement, though the system was primitive and could only allow the player to move when the arrow keys are tapped, not pressed.


3/11/2024
Fixed the movement issue by using booleans to determine whether a key is pressed or not, and move indefinitely until the key is no longer pressed. This may cause issues in the future,
though I can't predict what the specifics would be. I'll have to fix them once they arise.


3/12/2024
Created multiple creature objects, implemented a dictionary containing their name and the corresponding main sprite. This is preparation for drawing multiple creatures on the screen
at the same time, though I'm running into issues implementing this. It seems to have something to do with rects, so it might not be difficult to fix.


3/13/2024
Cleaned the main file, organized the folders. Put gif_test.gif and harold.png in "images", from "placeholder_images". I attempted to modualize, however I continued running into the 
problem of circular dependancy. I decided it would be beneficial to study this more and come back at a later time so that I can focus more on fixing other problems. Added a readme
and this devlog.