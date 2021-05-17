import nuke
import os
from plugins.preflight.preflight_check import PreflightCheck
from cgl.core.path import PathObject

from cgl.core.config import app_config



class MakeProxy(PreflightCheck):

    def getName(self):
        pass
    
    
    def run(self):
        if nuke.root()['proxy'].getValue == 'false':
            proxyPath = nuke.selectedNode()['file'].getValue()
            path_object = PathObject(proxyPath)

            #if len(os.listdir(os.path.dirname(proxyPath))) <= 2 :
                
            proxyWidth, proxyHeight = nuke.root()['proxy_format'].value().width(), nuke.root()['proxy_format'].value().height()
            proxyDefault = '%sx%s' % (proxyWidth,proxyHeight)

            print proxyPath   

            if '.exr' in proxyPath:
                extension = 'exr'

            elif '.jpg' in proxyPath:
                extension = 'jpg'
            
            
            path_object.make_proxy(resolution = proxyDefault , ext= extension)
    
            self.pass_check('Check Passed')
            # self.fail_check('Check Failed')

