import glfw
import sys


class Controller(object):

    def __init__(self):
        self.snake = None
        self.press_time = 0.0

    def set_snake(self, snake):
        self.snake = snake

    def on_key(self, window, key, scancode, action, mods):
        if not (action == glfw.PRESS or action == glfw.RELEASE):
            return

        if key == glfw.KEY_ESCAPE:
            sys.exit()

        elif (key == glfw.KEY_LEFT or key == glfw.KEY_A) and action == glfw.PRESS:
            self.snake.move_left()
            self.press_time = glfw.get_time()

        elif (key == glfw.KEY_RIGHT or key == glfw.KEY_D) and action == glfw.PRESS:
            self.snake.move_right()
            self.press_time = glfw.get_time()

        elif (key == glfw.KEY_UP or key == glfw.KEY_W) and action == glfw.PRESS:
            self.snake.move_up()
            self.press_time = glfw.get_time()

        elif (key == glfw.KEY_DOWN or key == glfw.KEY_S) and action == glfw.PRESS:
            self.snake.move_down()
            self.press_time = glfw.get_time()

        else:
            return

    # Returns the time of the last press of a key
    def get_time(self):
        return self.press_time

    # Adds time of the last press of a key
    def add_time(self, time):
        self.press_time += time
