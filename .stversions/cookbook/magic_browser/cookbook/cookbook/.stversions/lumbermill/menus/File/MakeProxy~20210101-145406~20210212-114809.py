
import os
from cgl.core.path import PathObject, CreateProductionData
from cgl.plugins.nuke.cgl_nuke import get_proxy_resolution
def run(lumbermill):
    print("create proxy")

    inputObject = lumbermill.path_widget.text.replace('/*', '')

    path_to_file = inputObject.split(' ')[0]
    
    path_object = PathObject(path_to_file)
    path_object.make_proxy(resolution=get_proxy_resolution(), ext='exr')
    