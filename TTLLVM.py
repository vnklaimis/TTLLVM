import viz
import vizact
import vizcam

# Define the boundaries for the player's movement (x, z min/max limits)
BOUNDARY_MIN_X = -10
BOUNDARY_MAX_X = 10
BOUNDARY_MIN_Z = -10
BOUNDARY_MAX_Z = 10

def main():
    ferma = viz.add("ferma.obj")
    ferma_tex = viz.addTexture("ferma.mtl")
    ferma.apply(ferma_tex)
    gnome = viz.add("gnome.obj")
    gnome_tex = viz.addTexture("gnome.mtl")
    gnome.apply(gnome_tex)
    wizard = viz.add("wizard.obj")
    wizard_tex = viz.addTexture("wizard.mtl")
    wizard.apply(wizard_tex)
    viz.go(viz.FULLSCREEN)
    viz.MainView.collision( viz.ON )
    setup_camera()
    setup_mouse_controls()
    setup_environment()
    

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

if __name__ == "__main__":
    main()
