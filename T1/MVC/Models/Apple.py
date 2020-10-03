from CourseResources import easy_shaders as es
from CourseResources import basic_shapes as bs
from CourseResources import scene_graph as sg
from CourseResources import transformations as tr


class Apple(object):

    def __init__(self):
        gpu_body_quad = es.toGPUShape(bs.createColorQuad(255 / 255, 153 / 255, 153 / 255))
        gpu_leaf_quad = es.toGPUShape(bs.createColorQuad(153 / 255, 255 / 255, 153 / 255))

        # We create the body
        body = sg.SceneGraphNode("Body")
        body.transform = tr.uniformScale(1)
        body.childs += [gpu_body_quad]

        # We create a generic leaf
        leaves = sg.SceneGraphNode('leaf')
        leaves.transform = tr.scale(0.25, 0.25, 1)
        leaves.childs += [gpu_leaf_quad]

        # We create a centered leaf
        leaf = sg.SceneGraphNode('CenterLeaf')
        leaf.transform = tr.translate(0, 0.5, 0)
        leaf.childs += [leaves]

        # We put together all the parts of the Apple
        apple = sg.SceneGraphNode('apple')
        apple.transform = tr.matmul([tr.scale(0.4, 0.4, 0), tr.translate(0, -1.25, 0)])
        apple.childs += [body, leaf]

        # We add the apple to the scene graph node
        transform_apple = sg.SceneGraphNode('appleTR')
        transform_apple.childs += [apple]

        # We designate the previous apple as the model of this class
        self.model = transform_apple
        self.x = 0.5
        self.y = 1

    def draw(self, pipeline):
        self.model.transform = tr.translate(self.x, self.y, 0)
        sg.drawSceneGraphNode(self.model, pipeline, 'transform')
