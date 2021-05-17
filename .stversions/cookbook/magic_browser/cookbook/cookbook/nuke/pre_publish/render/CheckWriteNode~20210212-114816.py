
import nuke
import os
from plugins.preflight.preflight_check import PreflightCheck
from cgl.core.path import PathObject
from cgl.core.config import app_config



class CheckWriteNode(PreflightCheck):
        
    def getName(self):
        pass
    

    def getProxyPath(self):
        path_object = PathObject(nuke.selectedNode()['file'].getValue())
        print(path_object.path)

        CONFIG = app_config()
        
        if path_object.project in CONFIG['default']['proxy_resolution'].keys() :
            proxy_resolution = CONFIG['default']['proxy_resolution'][path_object.project]
        else:
            proxy_resolution = CONFIG['default']['proxy_resolution']['default']
        proxyPath = path_object.path_root
        
        if 'elem'  in nuke.selectedNode().name():
            proxyPath = path_object.path_root.replace('high', proxy_resolution)
        else: 
            #proxyPath = path_object.path_root
            proxyPath = path_object.path_root.replace('high', proxy_resolution)
        print proxyPath
        nuke.selectedNode()['proxy'].setValue(proxyPath)
        if not os.path.isdir(os.path.dirname(proxyPath)):

            os.makedirs(os.path.dirname(proxyPath))
            os.makedirs(os.path.dirname(proxyPath).replace('render','source'))
                    
 
   
    def run(self):
        print 'Checking to see if a valid write node exists'
        self.getProxyPath()
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')




        

        
        
        