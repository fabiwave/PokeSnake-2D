from CourseResources import easy_shaders as es
from CourseResources import basic_shapes as bs
from CourseResources import scene_graph as sg
from CourseResources import transformations as tr


class Snake(object):

    def __init__(self, grid_size):
        self.total_grid = grid_size
        self.grid_unit = 2 / self.total_grid

        gpu_body_quad = es.toGPUShape(bs.createColorQuad(133 / 255, 94 / 255, 68 / 255))
        gpu_leg_quad = es.toGPUShape(bs.createColorQuad(255 / 255, 250 / 255, 218 / 255))

        # We create the body
        body = sg.SceneGraphNode("Body")
        body.transform = tr.uniformScale(1)
        body.childs += [gpu_body_quad]

        # We create the legs
        leg = sg.SceneGraphNode("Legs")
        leg.transform = tr.scale(0.25, 0.25, 1)
        leg.childs += [gpu_leg_quad]

        # Left legs
        leg_izq = sg.SceneGraphNode('legLeft')
        leg_izq.transform = tr.translate(-0.5, -0.5, 0)
        leg_izq.childs += [leg]

        leg_izq1 = sg.SceneGraphNode('legLeft1')
        leg_izq1.transform = tr.translate(-0.5, 0.5, 0)
        leg_izq1.childs += [leg]

        # Right legs
        leg_der = sg.SceneGraphNode('legRight')
        leg_der.transform = tr.translate(0.5, -0.5, 0)
        leg_der.childs += [leg]

        leg_der1 = sg.SceneGraphNode('legRight')
        leg_der1.transform = tr.translate(0.5, 0.5, 0)
        leg_der1.childs += [leg]

        # Translation delta
        t_delta = 0
        if self.total_grid % 2 == 0:
            t_delta = self.grid_unit / 2

        # We put together all the parts of the Snake (a.k.a Furret)
        snake = sg.SceneGraphNode('snake')
        snake.transform = tr.matmul(
            [tr.scale(self.grid_unit, self.grid_unit, 0), tr.translate(0, 0, 0)])
        snake.childs += [body, leg_izq, leg_der, leg_der1, leg_izq1]

        # We add the snake to the scene graph node
        transform_snake = sg.SceneGraphNode('snakeTR')
        transform_snake.childs += [snake]

        # We designate the previous snake as the model of this class
        self.model = transform_snake
        self.pos_x = t_delta
        self.pos_y = t_delta

        self.model.transform = tr.translate(t_delta, t_delta, 0)

    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, 'transform')

    def update_pos(self):
        self.model.transform = tr.translate(self.pos_x, self.pos_y, 0)

    def move_left(self):
        self.pos_x -= self.grid_unit
        self.update_pos()

    def move_right(self):
        self.pos_x += self.grid_unit
        self.update_pos()

    def move_down(self):
        self.pos_y -= self.grid_unit
        self.update_pos()

    def move_up(self):
        self.pos_y += self.grid_unit
        self.update_pos()
