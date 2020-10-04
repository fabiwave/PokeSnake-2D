from CourseResources import easy_shaders as es
from CourseResources import basic_shapes as bs
from CourseResources import scene_graph as sg
from CourseResources import transformations as tr
from random import randint


class Apple(object):

    def __init__(self, grid_size):
        # Basics variables set up
        self.total_grid = grid_size
        self.grid_unit = 2 / self.total_grid

        # Basic color shapes
        gpu_center_vertical_quad = es.toGPUShape(bs.createColorQuad(240 / 255, 85 / 255, 94 / 255))
        gpu_center_horizontal_quad = es.toGPUShape(bs.createColorQuad(240 / 255, 85 / 255, 94 / 255))
        gpu_berry_part_quad = es.toGPUShape(bs.createColorQuad(240 / 255, 85 / 255, 94 / 255))
        gpu_leaf_quad = es.toGPUShape(bs.createColorQuad(160 / 255, 235 / 255, 73 / 255))

        # We create a center vertical body for the body
        berry_center_vertical_body = sg.SceneGraphNode("VerticalBerry")
        berry_center_vertical_body.transform = tr.scale(5 / 9, 0.8, 1)
        berry_center_vertical_body.childs += [gpu_center_vertical_quad]

        # We create a center horizontal body for the body
        berry_center_horizontal_body = sg.SceneGraphNode("HorizontalBerry")
        berry_center_horizontal_body.transform = tr.scale(9 / 9, 0.2, 1)
        berry_center_horizontal_body.childs += [gpu_center_horizontal_quad]

        # We create a generic berry part
        berry_part = sg.SceneGraphNode("GenericBerry")
        berry_part.transform = tr.scale(7 / 9, 0.2, 1)
        berry_part.childs += [gpu_berry_part_quad]

        # We create the specific down part of the berry
        berry_part_down = sg.SceneGraphNode('BerryDown')
        berry_part_down.transform = tr.translate(0, -1.5 / 9, 0)
        berry_part_down.childs += [berry_part]

        # We create the specific down part of the berry
        berry_part_up = sg.SceneGraphNode('BerryUp')
        berry_part_up.transform = tr.translate(0, 1.5 / 9, 0)
        berry_part_up.childs += [berry_part]

        # We create a generic leaf
        leaf = sg.SceneGraphNode('Leaf')
        leaf.transform = tr.scale(1.5 / 9, 1.5 / 9, 1)
        leaf.childs += [gpu_leaf_quad]

        # We create the first leaf
        leaf_1 = sg.SceneGraphNode('Leaf1')
        leaf_1.transform = tr.translate(1 / 9, 4 / 9, 0)
        leaf_1.childs += [leaf]

        # We create the second leaf
        leaf_2 = sg.SceneGraphNode('Leaf2')
        leaf_2.transform = tr.translate(-1 / 9, 4 / 9, 0)
        leaf_2.childs += [leaf]

        # We create the second leaf
        leaf_3 = sg.SceneGraphNode('Leaf3')
        leaf_3.transform = tr.translate(0, 3 / 9, 0)
        leaf_3.childs += [leaf]

        # Translation delta for adjustment of the snake in the grid
        self.t_delta = 0
        if self.total_grid % 2 == 0:
            self.t_delta = self.grid_unit / 2

        # We put together all the parts of the Apple
        apple = sg.SceneGraphNode('apple')
        apple.transform = tr.matmul([tr.scale(self.grid_unit, self.grid_unit, 0), tr.translate(0, 0, 0)])
        apple.childs += [berry_center_vertical_body, berry_center_horizontal_body, berry_part_down, berry_part_up,
                         leaf_1, leaf_2, leaf_3]

        # We add the apple to the scene graph node
        transform_apple = sg.SceneGraphNode('appleTR')
        transform_apple.childs += [apple]

        # Designation of the previous apple as the model of this class
        half_grid = int((self.total_grid - 2) / 2)
        if self.total_grid % 2 == 0:
            half_grid = half_grid - 1

        random_x = randint(-half_grid, half_grid)
        random_y = randint(-half_grid, half_grid)

        self.model = transform_apple
        self.pos_x = self.t_delta + (random_x * self.grid_unit)
        self.pos_y = self.t_delta + (random_y * self.grid_unit)

        # Translation of the Apple to the random position
        self.model.transform = tr.translate(self.t_delta + (random_x * self.grid_unit),
                                            self.t_delta + (random_y * self.grid_unit), 0)

    # Draws the snake node into the scene
    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, 'transform')

    # Returns the position of the apple
    def get_position(self):
        return [self.pos_x, self.pos_y]

    # Updates the position of the model
    def update_pos(self):
        self.model.transform = tr.translate(self.pos_x, self.pos_y, 0)

    # Changes the position of the apple in the grid
    def respawn(self):
        half_grid = int((self.total_grid - 2) / 2)
        if self.total_grid % 2 == 0:
            half_grid = half_grid - 1
        random_x = randint(-half_grid, half_grid)
        random_y = randint(-half_grid, half_grid)
        self.pos_x = self.t_delta + (random_x * self.grid_unit)
        self.pos_y = self.t_delta + (random_y * self.grid_unit)
        self.update_pos()
