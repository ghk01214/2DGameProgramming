from pico2d import *
import time

running = True
stack = None
frame_interval = 0.01
delta_time = 0

def quit():
	global running
	running = False

def run(state):
	global running
	global stack

	running = True
	stack = [state]

	open_canvas()

	state.enter()

	global delta_time
	last_time = time.time()

	while running:
		now = time.time()
		delta_time = now - last_time
		last_time = now

		events = get_events()
		for e in events:
			stack[-1].handle_event(e)

		stack[-1].update()

		clear_canvas()
		stack[-1].draw()
		update_canvas()

		delay(frame_interval)

	while len(stack) > 0:
		stack[-1].exit()
		stack.pop()

	close_canvas()

def change(state):
	global stack

	if len(stack) > 0:
		stack.pop().exit()

	stack.append(state)
	state.enter()

def push(state):
	global stack

	if len(stack) > 0:
		stack[-1].pause()

	stack.append(state)
	state.enter()

def pop():
	global stack
	size = len(stack)

	if size == 1:
		quit()
	elif size > 1:
		stack[-1].exit()
		stack.pop()
		stack[-1].resume()

def run_main():
	from sys import modules
	main_module = modules['__main__']
	run(main_module)