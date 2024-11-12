Here's a README file for your gnome collection game:

---

# Gnome Collection Game

This is a 3D game developed in Vizard where players control a wizard character to explore a virtual world, collect hidden gnomes, and complete the quest as fast as possible. The game is implemented with camera control, boundary limitations, collision detection, and a real-time counter of collected gnomes.

## Features

- **3D Wizard Player**: The player controls a wizard character, using WASD keys for movement.
- **Mouse-Controlled Camera**: Rotate the camera with mouse movement for a dynamic view of the environment.
- **Boundary Limits**: The player can only move within specified x and z boundaries.
- **Gnome Collection**: A set number of gnomes are randomly spawned in the environment for the player to find and collect.
- **Collision Detection**: Prevents the player from moving outside the boundary.
- **Real-Time Collection Counter**: Displays the current count of collected gnomes.
- **Completion Timer**: Records the time taken to collect all gnomes and displays it upon completion.

## Gameplay Instructions

1. **Movement**: Use `W`, `A`, `S`, and `D` keys to move the wizard forward, left, backward, and right, respectively.
2. **Camera Control**: Move the mouse to rotate the camera view around the wizard.
3. **Objective**: Collect all the gnomes as quickly as possible.
4. **Gnome Collection**: Approach a gnome to collect it. The collection counter updates in real time.
5. **Completion**: After collecting all gnomes, your completion time will display on the screen.

## Controls

- `W`: Move forward
- `A`: Move left
- `S`: Move backward
- `D`: Move right
- `C`: Display current player coordinates
- Mouse: Rotate camera around the wizard

## Game Mechanics

- **Boundary Limits**: The wizard is restricted within a defined x and z range (from -10 to 10 on both axes).
- **Collision Detection**: The game prevents the player from moving out of bounds.
- **Gnome Detection Radius**: Gnomes within a 1-unit radius of the player are automatically collected.
- **Completion Tracking**: Once all gnomes are collected, the time taken will display on the screen.

## Setup and Installation

1. Install Vizard (a virtual reality software development platform).
2. Download or clone the game files into a local directory.
3. Open the main script in Vizard and run the game.

## Code Structure

- `main()`: Initializes the game and sets up objects, UI elements, and event handlers.
- `setup_environment()`: Configures the game environment with settings like sky color.
- `setup_mouse_controls()`: Defines mouse controls for rotating the camera.
- `setup_keyboard_controls()`: Handles keyboard input for player movement.
- `update_movement()`: Updates player movement based on keys pressed.
- `spawn_gnomes(num_gnomes)`: Spawns a specified number of gnomes in random positions.
- `check_for_collection()`: Checks if the player is within range to collect a gnome.

## Requirements

- **Vizard**: A Vizard environment with the necessary 3D assets (`wizard.obj`, `ferma.obj`, `gnome.obj`) and textures (`wizard.mtl`, `ferma.mtl`, `gnome.mtl`).
- **Python**: A basic understanding of Python for customization, if desired.

## Future Enhancements

- Additional levels with more complex gnome placements.
- Power-ups or time bonuses for completing tasks faster.
- Enhanced graphics, sound effects, and animations.

---

This README provides the essential details to help users understand, set up, and play the game, along with possible future enhancements for added functionality.