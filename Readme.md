I've always wanted to create a game, and tell a story. That's most artists' dream, right?

-----------------------------------------------------------------

Since I've been learning python, naturally, I gravitated towards game development and how I could make my own game. I understood that python is by no means the best way to do this, but I thought I'd learn a lot about programming itself as well as optimization. After all, good optimization would be crucial since pygame runs pretty slow. I saw this as a challenge, as a way to create a prototype for a much larger project. 

You're seeing this prototype, which I will continue to update until I determine it's no longer viable to keep using pygame. It's still very much in it's baby stage, though it took a lot of learning and practice to get it to this point in the first place. 

So far, within the course of 3 days, I've implemented: Player movement, collision, and creature classes/objects.

-----------------------------------------------------------------

The purpose of this game is to be a goblin, and take care of the wounded creatures you encounter. Then, once they're healthy, you set them free. Each creature has it's own quirks and needs, making it so that the player has to figure out what special care they need to become healthy again.

-----------------------------------------------------------------

To tell the truth, it has absolutely been challenging solely using pygame, but so far that hasn't stopped me and I've overcome almost all obstacles I've encountered so far. Everything I've implemented was a challenge and required me grasping a deeper understanding of the libray I've been using, as well as some general concepts such as OOP and optimization. I will start keeping a devlog of any problems I encounter in the future, and what I did to overcome them.

As an example of an obstance, I wanted to have each creature have it's own special image. I COULD simply just create objects using an image and it's path, but it looked really bad and wasn't very readable. Instead, I opted to use a dictionary, use the creature's name as the key and the image as the value, and retrieve it using the creature_retriever function. This function was just a simple for loop that would automatically find the image using the key I inserted into the "image" field. By doing things this way, it looks much more clean than if I were to lazily insert the image path in that field instead.

-----------------------------------------------------------------

What I did:
1. Appearances of multiple creatures on the screen at once (using objects and not drawing instances of classes on the screen). 
2. Finding a way to put the if statements regarding player movement into a function. 

What I will do in the next repository:
1. A system for generating tiles, and adding ground collision. This proved to be much more complex than I originally thought and so I'd need to take more time to learn how to implement this.
2. The ability to interact with creatures by pressing the "e" button.