from plugins.nuke.cgl_nuke import version_up_selected_write_node
import nuke
from cgl.core.path import PathObject
from cgl.core.config import app_config


def setAllProxies(path_object):
            filepath = nuke.root().name()
            validNodeClasses = ['Read', 'Write']
            for n in nuke.selectedNodes():
                
                CONFIG = app_config()
            
                if path_object.project in CONFIG['default']['proxy_resolution'].keys() :
                    proxy_resolution = CONFIG['default']['proxy_resolution'][path_object.project]
                else:
                    proxy_resolution = CONFIG['default']['proxy_resolution']['default']
            
                all_tasks = path_object.glob_project_element('task', full_path=True)
                
            
                if n.Class() in validNodeClasses:
                    proxyFile = n['file'].getValue().replace('high',proxy_resolution)
                    n['proxy'].setValue(proxyFile)

def run():
    
    sel = nuke.selectedNode()
    if sel.Class() == 'Write':
        version_up_selected_write_node()

    if sel.Class() == 'Read':
        path_object = PathObject(sel['file'].getValue())
        sel['file'].setValue(path_object.copy(latest=True,user= 'publish').path_root)
        setAllProxies(path_object)

