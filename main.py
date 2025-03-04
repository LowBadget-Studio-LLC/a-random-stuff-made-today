import ppb
from ppb import  keycodes
from ppb.events import KeyPressed,KeyReleased



class Player(ppb.Sprite):
    position = ppb.Vector(0,0)
    direction = ppb.Vector(1,1)
    speed = 4

    def on_update(self,update_event,signal):
        self.position += self.direction * self.speed * update_event.time_delta

def setup(scene):
    scene.add(Player())

ppb.run(setup=setup)