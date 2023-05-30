# Pygame Game

This is a simple game built using the Pygame library. The game involves controlling a player character, avoiding enemies, and collecting bonuses to score points. The player can move the character using the arrow keys.

## Getting Started

To run the game, you need to have Pygame installed. If you don't have it, you can install it using the following command:

```
pip install pygame
```

Once you have Pygame installed, you can clone the repository and run the game using the following commands:

```
git clone <repository-url>
cd <repository-directory>
python game.py
```

## Gameplay

- Use the **up** arrow key to move the character upwards.
- Use the **down** arrow key to move the character downwards.
- Use the **left** arrow key to move the character to the left.
- Use the **right** arrow key to move the character to the right.

Your goal is to avoid colliding with the enemies while collecting the bonuses to score points. The game ends if the player collides with an enemy.

## Controls

- Use the **up** arrow key to move the character upwards.
- Use the **down** arrow key to move the character downwards.
- Use the **left** arrow key to move the character to the left.
- Use the **right** arrow key to move the character to the right.
- Press **QUIT** to exit the game.

## Customization

You can customize the game by modifying the following parameters:

- `HEIGHT`: The height of the game window.
- `WIDTH`: The width of the game window.
- `PLAYER_MOVE_SPEED`: The speed at which the player character moves.
- `FONT`: The font used for displaying the score.
- `CREATE_ENEMY`: The frequency (in milliseconds) at which new enemies are created.
- `CREATE_BONUS`: The frequency (in milliseconds) at which new bonuses are created.
- `CHANGE_IMAGE`: The frequency (in milliseconds) at which the player character image changes.

You can also customize the game assets by replacing the following files:

- `background.png`: The background image.
- `player.png`: The player character image.
- `enemy.png`: The enemy image.
- `bonus.png`: The bonus image.
- The images in the `goose` folder, which are used to change the player character image.

Feel free to explore and modify the code to make the game your own!

Enjoy playing the game! If you have any questions or suggestions, please let me know.
