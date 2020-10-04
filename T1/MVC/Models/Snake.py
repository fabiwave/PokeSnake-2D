from CourseResources import easy_shaders as es
from CourseResources import basic_shapes as bs
from CourseResources import scene_graph as sg
from CourseResources import transformations as tr


class Snake(object):

    def __init__(self, grid_size):

        # Basics variables set up
        self.total_grid = grid_size
        self.grid_unit = 2 / self.total_grid

        # Creation of basic figure of the Snake
        gpu_body_quad = es.toGPUShape(bs.createColorQuad(133 / 255, 94 / 255, 68 / 255))
        gpu_leg_quad = es.toGPUShape(bs.createColorQuad(255 / 255, 250 / 255, 218 / 255))

        # Creation of the body
        body = sg.SceneGraphNode("Body")
        body.transform = tr.uniformScale(1)
        body.childs += [gpu_body_quad]

        # Creation of a generic leg
        leg = sg.SceneGraphNode("Legs")
        leg.transform = tr.scale(0.25, 0.25, 1)
        leg.childs += [gpu_leg_quad]

        # Creation of lower left leg
        leg_izq = sg.SceneGraphNode('legLeft')
        leg_izq.transform = tr.translate(-0.5, -0.5, 0)
        leg_izq.childs += [leg]

        # Creation of upper left leg
        leg_izq1 = sg.SceneGraphNode('legLeft1')
        leg_izq1.transform = tr.translate(-0.5, 0.5, 0)
        leg_izq1.childs += [leg]

        # Creation of lower right leg
        leg_der = sg.SceneGraphNode('legRight')
        leg_der.transform = tr.translate(0.5, -0.5, 0)
        leg_der.childs += [leg]

        # Creation of upper right leg
        leg_der1 = sg.SceneGraphNode('legRight')
        leg_der1.transform = tr.translate(0.5, 0.5, 0)
        leg_der1.childs += [leg]

        # Translation delta for adjustment of the snake in the grid
        self.t_delta = 0
        if self.total_grid % 2 == 0:
            self.t_delta = self.grid_unit / 2

        # Get together all the parts of the Snake
        snake = sg.SceneGraphNode('snake')
        snake.transform = tr.matmul(
            [tr.scale(self.grid_unit, self.grid_unit, 0), tr.translate(0, 0, 0)])
        snake.childs += [body, leg_izq, leg_der, leg_der1, leg_izq1]

        # Addition the snake to the scene graph node
        transform_snake = sg.SceneGraphNode('snakeTR')
        transform_snake.childs += [snake]

        # Designation of the previous snake as the model of this class
        self.model = transform_snake
        self.pos_x = self.t_delta
        self.pos_y = self.t_delta
        self.alive = True

        # Translation of the snake to the center position
        self.model.transform = tr.translate(self.t_delta, self.t_delta, 0)

    # Draws the snake node into the scene
    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, 'transform')

    # Updates the position of the model
    def update_pos(self):
        self.model.transform = tr.translate(self.pos_x, self.pos_y, 0)

    # Moves the model to the left in the grid
    def move_left(self):
        if self.alive:
            self.pos_x -= self.grid_unit
            self.update_pos()

    # Moves the model to the right in the grid
    def move_right(self):
        if self.alive:
            self.pos_x += self.grid_unit
            self.update_pos()

    # Moves the model down in the grid
    def move_down(self):
        if self.alive:
            self.pos_y -= self.grid_unit
            self.update_pos()

    # Moves the model up in the grid
    def move_up(self):
        if self.alive:
            self.pos_y += self.grid_unit
            self.update_pos()

    # Returns if the snake is colliding into a wall
    def collision(self):
        wall_boolean = False
        wall_pos = 1 - self.grid_unit + self.t_delta

        if self.pos_x == wall_pos or self.pos_x == -wall_pos or self.pos_y == wall_pos or self.pos_y == -wall_pos:
            self.alive = False

        return wall_boolean

    # Returns the position of the apple
    def get_position(self):
        return [self.pos_x, self.pos_y]
