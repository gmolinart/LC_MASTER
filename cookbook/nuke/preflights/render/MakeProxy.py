import nuke
import os
from plugins.preflight.preflight_check import PreflightCheck
from cgl.core.path import PathObject

from cgl.core.config import app_config



class MakeProxy(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        if not nuke.root()['proxy'].getValue():
            proxyPath = nuke.selectedNode()['file'].getValue()
            path_object = PathObject(proxyPath)

            #if len(os.listdir(os.path.dirname(proxyPath))) <= 2 :
                
            proxyWidth, proxyHeight = nuke.root()['proxy_format'].value().width(), nuke.root()['proxy_format'].value().height()
            proxyDefault = '%sx%s' % (proxyWidth, proxyHeight)
            if '.exr' in proxyPath:
                extension = 'exr'

            elif '.jpg' in proxyPath:
                extension = 'jpg'
            path_object.make_proxy(resolution=proxyDefault, ext=extension)
            self.pass_check('Check Passed')
        else:
            self.fail_check('Check Failed: proxy is set to True continue?? ')
