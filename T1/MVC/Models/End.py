from CourseResources import easy_shaders as es
from CourseResources import basic_shapes as bs
from CourseResources import scene_graph as sg
from CourseResources import transformations as tr
from math import pi


class End(object):

    def __init__(self):
        # Creation of basic figure of the end scene
        gpu_background_quad = es.toGPUShape(bs.createColorQuad(0 / 255, 0 / 255, 0 / 255))
        end_scene = sg.SceneGraphNode("End")
        end_scene.transform = tr.uniformScale(1)
        end_scene.childs += [gpu_background_quad]

        # Translation and scale of the end scene
        end_scene.transform = tr.matmul([tr.scale(1.25, 1, 0), tr.translate(0, 0, 0)])

        # Designation of the previous background as the model of this class
        self.model = end_scene

    # Draws the end node into the scene
    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, 'transform')
