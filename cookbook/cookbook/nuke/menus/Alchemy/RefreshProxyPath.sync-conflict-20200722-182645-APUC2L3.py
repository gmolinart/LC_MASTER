import nuke
import nukescripts
from cgl.core.path import PathObject, lj_list_dir
from cgl.core.config import app_config
import os





def checkIfProxyExist():
    
    for n in nuke.allNodes(): 
        validNodeClasses = ['Read', 'Write']
        if n.Class() in validNodeClasses:
            proxydir = os.path.dirname(n['proxy'].getValue())
            if not  os.path.isdir(proxydir):
                print('no such dir')
                print proxydir
                n['tile_color'].setValue(4278190335)
            else : 
                n['tile_color'].setValue(0)
                
            

def setAllProxies(path_object):
    filepath = nuke.root().name()
    validNodeClasses = ['Read', 'Write']
    for n in nuke.allNodes():
        
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
    filepath = nuke.root().name()
    path_object = PathObject(filepath)
    setAllProxies(path_object)
    checkIfProxyExist()
    print("all proxy paths set ")

