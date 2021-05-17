import nuke

from cgl.core.path import PathObject
from cgl.plugins.nuke import alchemy as alc
from cgl.plugins.nuke import utils 


def run():
    node = utils.get_selection()

    if utils.check_type(node, "Read") or utils.check_type(node, "Write"):
        scene = alc.scene_object()
        extension = scene.project_info['ext']
        proxy_res = scene.project_info['proxy']
        object = utils.get_path_object_from_node(node)
        object.make_proxy(ext = extension, resolution = proxy_res,copy_input_padding=True)


