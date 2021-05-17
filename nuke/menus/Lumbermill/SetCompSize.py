import nuke
import nukescripts
from cgl.core.path import PathObject, lj_list_dir
from cgl.core.config import app_config
from cgl.plugins.nuke.cgl_nuke import NukePathObject



def run():
    
    filepath = nuke.root().name()
    path_object = PathObject(filepath)
    
    
    CONFIG = app_config()
    
    if path_object.project in CONFIG['default']['proxy_resolution'].keys() :
        proxy_resolution = CONFIG['default']['proxy_resolution'][path_object.project]
    else:
        proxy_resolution = CONFIG['default']['proxy_resolution']['default']
    
    
    
    def setCompDefaultSettings(proxy_res='1920x1080', readNode=nuke.toNode('plate_Read'), alert=False):
        if not readNode:
            readNode = nuke.selectedNode()
    
        selectedFormat = readNode['format'].value()
        nuke.root()['format'].setValue(selectedFormat)
        
        firstFrame = int(readNode.knob('first').getValue())
        lastFrame = int(readNode.knob('last').getValue())
    
        LC_PROXY = '%s LC_PROXY' % proxy_res.replace('x', ' ')
    
        # Setup proxy settings
        nuke.addFormat(LC_PROXY)
        nuke.root()['proxy_type'].setValue('format')
        nuke.root()['proxy_format'].setValue('LC_PROXY')
        nuke.root()['proxySetting'].setValue('if nearest')
        readNode['proxy_format'].setValue('LC_PROXY')
        nuke.root()['proxySetting'].setValue('if nearest')
    
        if alert:
            nuke.alert("Comp Size, duration and proxy set")
    
    
    
    
    
    setCompDefaultSettings(proxy_res = proxy_resolution, readNode = nuke.selectedNode(), alert = True)
