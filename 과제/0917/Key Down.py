from pico2d import *

def handle_events():
    global running
    global dir

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_q:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

open_canvas()

grass = load_image('res/grass.png')
character = load_image('res/character.png')

x = 800 // 2
dir = 0
running = True

while x < 800 and running:
    clear_canvas()

    grass.draw(400, 30)
    character.draw(x, 85)

    update_canvas()

    x += dir * 5
    delay(0.05)

    handle_events()

close_canvas()