from pico2d import *

def handle_events():
    global running
    global x

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_q:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x += 10
            elif event.key == SDLK_LEFT:
                x -= 10
            elif event.key == SDLK_ESCAPE:
                running = False

open_canvas()

grass = load_image('res/grass.png')
character = load_image('res/character.png')

x = 800 // 2
frame = 0
running = True

while x < 800 and running:
    clear_canvas()

    grass.draw(400, 30)
    character.draw(x, 85)

    update_canvas()
    handle_events()

close_canvas()