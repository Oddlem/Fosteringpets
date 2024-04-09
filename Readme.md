Remade this file so that it explains what all the code does



Everything is separated into moduals, though that probably goes without saying. Here's what each modual does:

-main.py contains classes, functions, and some objects that were created.

-assets.py imports raw visual data (because of this, dialogue box doesn't belong in here since it's created via pygame_gui). This includes spritesheets and tilesets.

-config.py contains certain booleans (for example, character_can_move), anything handling dialogue or dialogue boxes, and vital pygame calls (like pygame.init()).

-main_game_loop.py contains the actual game loop, along with some calls that can't be put anywhere else due to circular dependancy problems.
