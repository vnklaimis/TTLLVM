import viz
import vizact
import vizcam

# Define the boundaries for the player's movement (x, z min/max limits)
BOUNDARY_MIN_X = -10
BOUNDARY_MAX_X = 10
BOUNDARY_MIN_Z = -10
BOUNDARY_MAX_Z = 10

def main():
    viz.go(viz.FULLSCREEN)
    setup_camera()
    setup_mouse_controls()
    setup_environment()
    load_house_model('TTLLVM.obj')
    
    # Add an update function to keep the player within boundaries
    vizact.ontimer(0, enforce_boundaries)

def setup_camera():
    tracker = vizcam.addWalkNavigate()
    tracker.setPosition([0, 1.5, 0])
    viz.link(tracker, viz.MainView)
    viz.mouse.setVisible(False)

MOUSE_SENSITIVITY = 0.1

def setup_mouse_controls():
    def onMouseMove(e):
        view_angle = viz.MainView.getEuler()
        view_angle[0] -= e.dx * MOUSE_SENSITIVITY
        view_angle[1] -= e.dy * MOUSE_SENSITIVITY
        viz.MainView.setEuler(view_angle)
    viz.callback(viz.MOUSE_MOVE_EVENT, onMouseMove)

def setup_environment():
    viz.clearcolor(viz.SKYBLUE)

def load_house_model(model_path):
    try:
        house = viz.add(model_path)
        house.setPosition(0, 0, 0)
    except:
        print(f"Error loading '{model_path}'. Please check the file path or replace with a valid model.")

def enforce_boundaries():
    # Get the current position of the player
    position = viz.MainView.getPosition()

    # Apply boundaries to the x and z coordinates
    x = position[0]
    z = position[2]

    # Clamp the x position between the defined boundaries
    if x < BOUNDARY_MIN_X:
        x = BOUNDARY_MIN_X
    elif x > BOUNDARY_MAX_X:
        x = BOUNDARY_MAX_X

    # Clamp the z position between the defined boundaries
    if z < BOUNDARY_MIN_Z:
        z = BOUNDARY_MIN_Z
    elif z > BOUNDARY_MAX_Z:
        z = BOUNDARY_MAX_Z

    # Update the player's position if it exceeds the boundary limits
    viz.MainView.setPosition([x, position[1], z])

if __name__ == "__main__":
    main()
