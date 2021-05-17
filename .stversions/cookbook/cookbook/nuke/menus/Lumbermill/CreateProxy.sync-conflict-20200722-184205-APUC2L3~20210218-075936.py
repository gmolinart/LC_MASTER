
import nuke
import os
from cgl.core.path import PathObject


def run():
    selectedNode = nuke.selectedNode()

        
    if selectedNode.Class() == 'Read' or selectedNode.Class() == 'Write':
        
        proxyWidth, proxyHeight = nuke.root()['proxy_format'].value().width(), nuke.root()['proxy_format'].value().height()
        defaultFormat = 'exr'    
        proxyDefault = '%sx%s %s' % (proxyWidth,proxyHeight,defaultFormat)
        proxySettings = nuke.getInput("Create proxy for %s  with resolution:" % nuke.selectedNode().name(), proxyDefault)
    
        if proxySettings:
            path_object = PathObject(selectedNode['file'].getValue())
            proxyExtension = proxySettings.split(' ')[1]
            
            proxyPath = selectedNode['file'].getValue().replace(path_object.resolution,proxySettings.split(' ')[0] )
            print 11111111111111111
            

            if '.exr' in proxyPath:
                proxyPath = proxyPath.replace('.exr','.%s' % proxySettings.split(' ')[1])

            elif '.jpg' in proxyPath:
                proxyPath = proxyPath.replace('.jpg','.%s' % proxySettings.split(' ')[1])
            
            print proxyPath    
            directoryPath = os.path.dirname(proxyPath)
            if os.path.isdir(directoryPath):
                #if os.listdir(os.path.dirname(proxyPath)) == '' :

                path_object.make_proxy(resolution = proxySettings.split(' ')[0] ,ext= proxyExtension)
            
            else : 
                os.makedirs(directoryPath)
                path_object.make_proxy(resolution = proxySettings.split(' ')[0] ,ext= proxyExtension)
            
                print(proxyPath)            
            selectedNode['proxy'].setValue(proxyPath)
        else: 
            print('canceled')
    else:
        nuke.message('Please select a read Node')
