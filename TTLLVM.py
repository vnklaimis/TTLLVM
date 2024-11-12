import viz
import vizact
import vizcam
import random
import math

# Define the boundaries for the player's movement (x, z min/max limits)
BOUNDARY_MIN_X = -10
BOUNDARY_MAX_X = 10
BOUNDARY_MIN_Z = -10
BOUNDARY_MAX_Z = 10

NUM_GNOMES = 5  # Number of gnomes to spawn
collected_gnomes = 0  # Counter for collected gnomes
gnome_objects = []  # List to store gnome objects
start_time = None  # Variable to store the start time
keys_pressed = {'w': False, 'a': False, 's': False, 'd': False}  # Keys for movement
ir_kustiba = False  # Movement flag

# Load the player object
player = viz.add('wizard.obj')
player_texture = viz.addTexture('wizard.mtl')
player.apply(player_texture)
player.collideMesh()
player.setPosition([0, 0, 0])  # Adjusted initial position
player.setScale([1, 1, 1])

# Camera parameters
camera_distance = 5
camera_elevation = 1.5
camera_angle = 0
MOUSE_SENSITIVITY = 0.1

def main():
    global counter_text, start_time
    viz.go(viz.FULLSCREEN)  # Initialize Vizard

    # Load main objects
    ferma = viz.add("ferma.obj")
    ferma_tex = viz.addTexture("ferma.mtl")
    ferma.apply(ferma_tex)
    ferma.collideMesh()

    setup_environment()
    setup_mouse_controls()
    setup_keyboard_controls()
    
    start_time = viz.tick()  # Record the start time
    
    viz.mouse.setVisible(False)

    spawn_gnomes(NUM_GNOMES)

    # Set up the collection counter text
    counter_text = viz.addText(f"{collected_gnomes}/{NUM_GNOMES} Gnomes Collected", viz.SCREEN)
    counter_text.setPosition(0.05, 0.95)
    counter_text.fontSize(24)

    vizact.ontimer(0, check_for_collection)
    vizact.ontimer(0.02, update_movement)

def setup_environment():
    viz.clearcolor(viz.SKYBLUE)  # Set a bright sky color

def setup_mouse_controls():
    def onMouseMove(e):
        global camera_angle
        camera_angle += e.dx * MOUSE_SENSITIVITY
        camera_angle %= 360
        update_camera_position()
        
        # Rotate the player to face the camera's forward direction
        player.setEuler([camera_angle, 0, 0])

    viz.callback(viz.MOUSE_MOVE_EVENT, onMouseMove)

def update_camera_position():
    model_position = player.getPosition()
    x = model_position[0] + camera_distance * math.sin(math.radians(camera_angle))
    z = model_position[2] + camera_distance * math.cos(math.radians(camera_angle))
    viz.MainView.setPosition([x, camera_elevation, z])
    viz.MainView.lookAt(player.getPosition())

def setup_keyboard_controls():
    viz.callback(viz.KEYDOWN_EVENT, onKeyDown)
    viz.callback(viz.KEYUP_EVENT, onKeyUp)

def check_collision(new_position):
    x, y, z = new_position
    wall_thickness = 0.2  # Define wall thickness for boundary collision
    if x < BOUNDARY_MIN_X + wall_thickness or x > BOUNDARY_MAX_X - wall_thickness or z < BOUNDARY_MIN_Z + wall_thickness or z > BOUNDARY_MAX_Z - wall_thickness:
        print(f"Collision detected at position: {new_position}")
        return True
    return False

def update_movement():
    if ir_kustiba:
        current_position = player.getPosition()
        move_x, move_z = 0, 0
        o = 0.1

        if keys_pressed['w']:
            move_z -= o
        if keys_pressed['s']:
            move_z += o
        if keys_pressed['a']:
            move_x += o
        if keys_pressed['d']:
            move_x -= o

        euler = player.getEuler()
        angle = math.radians(euler[0])
        forward_x = move_z * math.sin(angle)
        forward_z = move_z * math.cos(angle)
        strafe_x = move_x * math.cos(angle)
        strafe_z = -move_x * math.sin(angle)
        
        new_position = [
            current_position[0] + forward_x + strafe_x,
            current_position[1],
            current_position[2] + forward_z + strafe_z
        ]
        
        if not check_collision(new_position):
            player.setPosition(new_position)
            update_camera_position()

def onKeyDown(key):
    global ir_kustiba
    if key in keys_pressed:
        keys_pressed[key] = True
    if key == 'c':
        print("Player coordinates:", player.getPosition())
    ir_kustiba = True  # Start movement

def onKeyUp(key):
    global ir_kustiba
    if key in keys_pressed:
        keys_pressed[key] = False
    ir_kustiba = any(keys_pressed.values())  # Stop if no movement keys are pressed

def spawn_gnomes(num_gnomes):
    global gnome_objects
    for _ in range(num_gnomes):
        random_x = random.uniform(BOUNDARY_MIN_X, BOUNDARY_MAX_X)
        random_z = random.uniform(BOUNDARY_MIN_Z, BOUNDARY_MAX_Z)
        gnome = viz.add("gnome.obj")
        gnome_tex = viz.addTexture("gnome.mtl")
        gnome.apply(gnome_tex)
        gnome.setPosition([random_x, 0, random_z])
        gnome.collideMesh()
        gnome_objects.append(gnome)

def check_for_collection():
    global collected_gnomes, counter_text, start_time
    player_position = player.getPosition()

    for gnome in gnome_objects:
        if gnome.getVisible():
            gnome_position = gnome.getPosition()
            distance = vizmat.Distance(player_position, gnome_position)

            if distance < 1:
                gnome.visible(False)
                collected_gnomes += 1
                counter_text.message(f"{collected_gnomes}/{NUM_GNOMES} Gnomes Collected")

                if collected_gnomes == NUM_GNOMES:
                    end_time = viz.tick()
                    duration = end_time - start_time
                    print(f"All gnomes collected! Time taken: {duration:.2f} seconds")
                    completion_text = viz.addText(f"Completed in {duration:.2f} seconds!", viz.SCREEN)
                    completion_text.setPosition(0.5, 0.5)
                    completion_text.fontSize(32)

if __name__ == "__main__":
    main()
