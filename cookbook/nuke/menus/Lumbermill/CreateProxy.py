import nuke
import os
from cgl.core.path import PathObject
from cgl.plugins.nuke.cgl_nuke import get_proxy_resolution


def run():
    selectedNode = nuke.selectedNode()

    if selectedNode.Class() == 'Read' or selectedNode.Class() == 'Write':

        # proxyWidth, proxyHeight = nuke.root()['proxy_format'].value().width(), nuke.root()['proxy_format'].value().height()
        defaultFormat = 'exr'
        proxyDefault = '%s %s' % (get_proxy_resolution(), defaultFormat)
        proxySettings = nuke.getInput("Create proxy for %s  with resolution:" % nuke.selectedNode().name(),
                                      proxyDefault)
        path_object = PathObject(selectedNode['file'].getValue())

        if proxySettings:
            proxySettings = proxySettings.split(' ')

            proxyExtension = proxySettings[1]

            proxyResolution = proxySettings[0]
            proxyPathObject = path_object.copy(resolution=str(proxyResolution))

            proxyPath = proxyPathObject.copy(extension=proxySettings[1])

            print(proxyPath.path_root)
            directoryPath = proxyPath.copy(filename='').path_root

            if os.path.isdir(directoryPath):
                # if os.listdir(os.path.dirname(proxyPath)) == '' :
                print(proxyPath.resolution)
                path_object.make_proxy(resolution=proxyPath.resolution, ext=proxyPath.ext)

            else:
                os.makedirs(directoryPath)
                path_object.make_proxy(resolution=proxyPath.resolution, ext=proxyPath.ext)

            selectedNode['proxy'].setValue(proxyPath.path_root)
        else:
            print('canceled')
    else:
        nuke.message('Please select a read Node')


#run()

