A game that currently serves as a sandbox; you interact with creatures and have to nurse them back to health. The project was created entirely in Pygame (a gamedev library for python), every system being implemented manually.

![oddlem-uPJ2_J_9O5FAhnJS7UFcx-python_BDKzn37Ych](https://github.com/user-attachments/assets/7d96d6f1-9cfb-4554-b9ea-2110883f87cd)


Module Directory:

-main.py contains classes, functions, and some objects that were created.

-assets.py imports raw visual data (because of this, dialogue box doesn't belong in here since it's created via pygame_gui). This includes spritesheets and tilesets.

-config.py contains certain booleans (for example, character_can_move), anything handling dialogue or dialogue boxes, and vital pygame calls (like pygame.init()).

-main_game_loop.py contains the actual game loop, along with some calls that can't be put anywhere else due to circular dependancy problems.
