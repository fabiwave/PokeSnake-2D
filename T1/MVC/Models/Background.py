from CourseResources import easy_shaders as es
from CourseResources import basic_shapes as bs
from CourseResources import scene_graph as sg
from CourseResources import transformations as tr


class Background(object):

    def __init__(self):

        # Creation of basic figure of the background
        gpu_background_quad = es.toGPUShape(bs.createColorQuad(118 / 255, 193 / 255, 159 / 255))
        background = sg.SceneGraphNode("Background")
        background.transform = tr.uniformScale(1)
        background.childs += [gpu_background_quad]

        # Translation and scale of the background
        background.transform = tr.matmul([tr.scale(2, 2, 0), tr.translate(0, 0, 0)])

        # Designation of the previous background as the model of this class
        self.model = background

    # Draws the background node into the scene
    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, 'transform')