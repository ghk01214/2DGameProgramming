from pico2d import *

def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_q:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

grass = load_image('res/grass.png')
character = load_image('res/run_animation.png')

x = 0
frame = 0
running = True

while x < 800 and running:
    clear_canvas()
    
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 85)

    update_canvas()

    frame = (frame + 1) % 8
    x += 5
    
    delay(0.03)

    handle_events()

close_canvas()