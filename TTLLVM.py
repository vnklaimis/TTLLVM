import viz 
import vizact
viz.go() 
# Importējiet un novietojiet pašu veidotu objektu 
customObject = viz.add('path/to/your/object.osgb') 
customObject.setPosition([0, 0, 5]) 

customObject.setPosition([0, 0, 5]) 
anotherObject.setPosition([2, 0, 5]) 

def onPick(e): 
    if e.object.valid(): 
        e.object.color(viz.RED) 
        move = vizact.moveTo([0, 2, 0], time=1) 
        e.object.addAction(move) 
        viz.callback(viz.PICK_EVENT, onPick) 
        viz.mouse(viz.OFF) 
vizact.onkeydown('p', viz.mouse.pick) 

def updateCamera(): 
    viz.MainView.move([0, 0, 0.1]) 
vizact.ontimer(0, updateCamera)