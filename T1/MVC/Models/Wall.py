from math import pi
from CourseResources import easy_shaders as es
from CourseResources import basic_shapes as bs
from CourseResources import scene_graph as sg
from CourseResources import transformations as tr
from OpenGL.GL import *


class Wall(object):

    def __init__(self, grid_size):

        # Basics variables set up
        self.total_grid = grid_size
        self.grid_unit = 2 / self.total_grid

        # Creation of basic figure of the Wall
        gpu_brick_quad = es.toGPUShape(
            bs.createTextureQuad("/home/fabiwave/PycharmProjects/T1C-poke-snake/T1/MVC/Models/Images/bush.png"),
            GL_REPEAT, GL_NEAREST)

        # Creation of the a generic brick node
        brick = sg.SceneGraphNode("Brick")
        brick.transform = tr.matmul(
            [tr.scale(self.grid_unit, self.grid_unit, 0), tr.translate(0, 0, 0)])
        brick.childs += [gpu_brick_quad]

        # Translation delta for adjustment of the wall in the grid
        t_delta = self.grid_unit / 2
        wall_children = []
        i = -1 + t_delta

        # Creation of a generic wall
        while i < 1:
            new_brick = sg.SceneGraphNode("Brick " + str(i))
            new_brick.transform = tr.translate(1 - t_delta, i, 0)
            new_brick.childs += [brick]
            wall_children.append(new_brick)
            i += self.grid_unit

        a_wall = sg.SceneGraphNode("Wall")
        a_wall.transform = tr.identity()
        a_wall.childs += wall_children

        # Creation of a fort with 4 walls
        fort = sg.SceneGraphNode("Fort")
        fort.transform = tr.identity()
        walls = []
        for i in range(0, 4):
            wall = sg.SceneGraphNode("Wall " + str(i))
            wall.transform = tr.rotationZ(i * pi / 2)
            wall.childs += [a_wall]
            walls.append(wall)
        fort.childs += walls

        # Designation of the previous fort as the model of this class
        self.model = fort

    # Draws the wall node into the scene
    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, 'transform')
