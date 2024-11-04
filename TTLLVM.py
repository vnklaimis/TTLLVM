import viz
import vizact
import vizcam
import random

# Define the boundaries for the player's movement (x, z min/max limits)
BOUNDARY_MIN_X = -10
BOUNDARY_MAX_X = 10
BOUNDARY_MIN_Z = -10
BOUNDARY_MAX_Z = 10

NUM_GNOMES = 5  # Number of gnomes to spawn
collected_gnomes = 0  # Counter for collected gnomes
gnome_objects = []  # List to store gnome objects

def main():
    global counter_text

    # Set the simulation to windowed mode (non-fullscreen)
    viz.go()  # Initialize Vizard
    viz.window.setSize(1920, 1080)

    # Load main objects
    ferma = viz.add("ferma.obj")
    ferma_tex = viz.addTexture("ferma.mtl")
    ferma.apply(ferma_tex)
    ferma.collideMesh()  # Enable collision for ferma object

    wizard = viz.add("wizard.obj")
    wizard_tex = viz.addTexture("wizard.mtl")
    wizard.apply(wizard_tex)
    wizard.collideMesh()  # Enable collision for wizard object

    setup_camera()
    setup_mouse_controls()
    setup_environment()

    # Spawn gnomes at random positions
    spawn_gnomes(NUM_GNOMES)

    # Set up the collection counter text
    counter_text = viz.addText(f"{collected_gnomes}/{NUM_GNOMES} Gnomes Collected", viz.SCREEN)
    counter_text.setPosition(0.05, 0.95)  # Top-left corner of the screen
    counter_text.fontSize(24)

    # Check for gnome collection in real-time
    vizact.ontimer(0, check_for_collection)

def setup_camera():
    # Use the WalkNavigate camera for basic navigation
    tracker = vizcam.addWalkNavigate()
    tracker.setPosition([0, 1.8, 0])  # Set position height to simulate a human perspective (1.8m is typical)
    tracker.collision(viz.ON)  # Enable collision for the camera
    viz.link(tracker, viz.MainView)

    viz.mouse.setVisible(False)

MOUSE_SENSITIVITY = 0.1

def setup_mouse_controls():
    # Mouse look around control
    def onMouseMove(e):
        view_angle = viz.MainView.getEuler()
        view_angle[0] -= e.dx * MOUSE_SENSITIVITY
        view_angle[1] -= e.dy * MOUSE_SENSITIVITY
        viz.MainView.setEuler(view_angle)
    viz.callback(viz.MOUSE_MOVE_EVENT, onMouseMove)

def setup_environment():
    viz.clearcolor(viz.SKYBLUE)  # Set a bright sky color

def spawn_gnomes(num_gnomes):
    global gnome_objects

    for i in range(num_gnomes):
        # Generate random x and z coordinates within the boundaries
        random_x = random.uniform(BOUNDARY_MIN_X, BOUNDARY_MAX_X)
        random_z = random.uniform(BOUNDARY_MIN_Z, BOUNDARY_MAX_Z)

        # Load the gnome model and position it at the random coordinates
        gnome = viz.add("gnome.obj")
        gnome_tex = viz.addTexture("gnome.mtl")
        gnome.apply(gnome_tex)
        gnome.setPosition([random_x, 0, random_z])  # Place on the ground (y=0)
        gnome.collideMesh()  # Enable collision for each gnome

        gnome_objects.append(gnome)  # Add gnome to the list for tracking

def check_for_collection():
    global collected_gnomes, counter_text

    player_position = viz.MainView.getPosition()  # Get the player's position

    for gnome in gnome_objects:
        if gnome.getVisible():  # Only check gnomes that are still visible
            gnome_position = gnome.getPosition()
            distance = vizmat.Distance(player_position, gnome_position)  # Calculate distance to gnome

            if distance < 1.5:  # If close enough to collect
                gnome.visible(False)  # Hide the gnome (simulating collection)
                collected_gnomes += 1  # Increase collected counter
                counter_text.message(f"{collected_gnomes}/{NUM_GNOMES} Gnomes Collected")  # Update the counter text

def load_house_model(model_path):
    try:
        house = viz.add(model_path)
        house.setPosition(0, 0, 0)
        house.collideMesh()  # Enable collision for custom model
    except:
        print(f"Error loading '{model_path}'. Please check the file path or replace with a valid model.")

if __name__ == "__main__":
    main()
