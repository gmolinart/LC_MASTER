
from cgl.core.path import PathObject
from cgl.plugins.nuke.cgl_nuke import NukePathObject


import os 
import nuke

# imports previous published version




def import_media(filepath, name=None):
        """
        imports the filepath.  This assumes that sequences are formated as follows:
        [sequence] [sframe]-[eframe]
        sequence.####.dpx 1-234
        regular files are simply listed as a string with no frame numbers requred:
        bob.jpg
        this will also look for an HD proxy file, first jpgs and then exrs.
        :param filepath:
        :return:
        """
        read_node = nuke.createNode('Read')
        if name:
            read_node.knob('name').setValue(name)
        read_node.knob('file').fromUserText(filepath)
        path_object = NukePathObject(filepath)
        proxy_object = PathObject(filepath).copy(resolution=path_object.proxy_resolution, ext='exr')
        dir_ = os.path.dirname(proxy_object.path_root)
        if os.path.exists(dir_):
            read_node.knob('proxy').fromUserText(proxy_object.path_root)
        return read_node




def run():
    path_object = PathObject(nuke.selectedNode()['file'].getValue())
    latestPublishedVersion =  path_object.copy(user= 'publish',latest = True).path_root 
    first = int(nuke.selectedNode()['first'].getValue())
    last  = int(nuke.selectedNode()['last'].getValue())
    import_media(latestPublishedVersion + '%s-%s' % (first, last) , 'previousVersion')