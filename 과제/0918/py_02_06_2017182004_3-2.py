from pico2d import *
from helper import *

RESOURCE_DIRECTORY = '../res'
HEIGHT = 600

class Character:
    def __init__(self):
        self.pos = 20, 85
        self.speed = 5
        self.delta = 0, 0
        self.target = 0, 0
        self.frame = 0
        self.running = False
        self.image = load_image(RESOURCE_DIRECTORY + '/run_animation.png')
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.pos[0], self.pos[1])
    def update(self):
        self.frame = (self.frame + 1) % 8

def handle_events():
    global running
    global destination
    global number
    
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_q:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            target = event.x, HEIGHT - event.y - 1

            if character.running == False:
                character.target = target
                character.running = True
                character.speed = 1
            else:
                character.speed += 1

            destination.append(target)

#--------------------------------------------------------------------------------------

open_canvas()

grass = load_image(RESOURCE_DIRECTORY + '/grass.png')
running = True
x, y = 0, 0
done = False
click = 0
number = 0
destination = []

character = Character()

while running:
    clear_canvas()

    grass.draw(400, 30)
    character.draw()

    if character.running:
        character.delta = delta(character.pos, character.target, character.speed)
        character.pos, done = move_toward(character.pos, character.delta, character.target)
    
    if character.pos == character.target:
        character.delta = 0, 0
        
        if number + 1 == len(destination):
            character.running = False
            character.speed = 0
        else:
            number += 1    
            character.target = destination[number]

    character.update()
    update_canvas()
    handle_events()
    delay(0.03)

close_canvas()