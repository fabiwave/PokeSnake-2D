import glfw
import sys


class Controller(object):

    def __init__(self):
        self.snake = None

    def set_snake(self, snake):
        self.snake = snake

    def on_key(self, window, key, scancode, action, mods):
        if not (action == glfw.PRESS or action == glfw.RELEASE):
            return

        if key == glfw.KEY_ESCAPE:
            sys.exit()

        elif key == glfw.KEY_LEFT and action == glfw.PRESS:
            self.snake.move_left()

        elif key == glfw.KEY_RIGHT and action == glfw.PRESS:
            self.snake.move_right()

        elif key == glfw.KEY_UP and action == glfw.PRESS:
            self.snake.move_up()

        elif key == glfw.KEY_DOWN and action == glfw.PRESS:
            self.snake.move_down()

        else:
            print('Unknown key')
