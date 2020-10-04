from math import pi
from CourseResources import easy_shaders as es
from CourseResources import basic_shapes as bs
from CourseResources import scene_graph as sg
from CourseResources import transformations as tr


class Wall(object):

    def __init__(self, grid_size):
        self.total_grid = grid_size
        self.grid_unit = 2 / self.total_grid

        gpu_brick_quad = es.toGPUShape(bs.createColorQuad(255 / 255, 153 / 255, 153 / 255))

        brick = sg.SceneGraphNode("Brick")
        brick.transform = tr.matmul(
            [tr.scale(self.grid_unit, self.grid_unit, 0), tr.translate(0, 0, 0)])
        brick.childs += [gpu_brick_quad]

        # Translation delta
        t_delta = self.grid_unit / 2
        wall_children = []
        i = -1 + t_delta
        while i < 1:
            new_brick = sg.SceneGraphNode("Brick " + str(i))
            new_brick.transform = tr.translate(1 - t_delta, i, 0)
            new_brick.childs += [brick]
            wall_children.append(new_brick)
            i += self.grid_unit

        a_wall = sg.SceneGraphNode("Wall")
        a_wall.transform = tr.identity()
        a_wall.childs += wall_children

        fort = sg.SceneGraphNode("Fort")
        fort.transform = tr.identity()
        walls = []
        for i in range(0, 4):
            wall = sg.SceneGraphNode("Wall " + str(i))
            wall.transform = tr.rotationZ(i * pi / 2)
            wall.childs += [a_wall]
            walls.append(wall)
        fort.childs += walls
        self.model = fort

    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, 'transform')
