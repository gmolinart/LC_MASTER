
import nuke
import os 
from cgl.core.path import PathObject


def writeGeo(geoFile):
    readGeo = nuke.createNode('WriteGeo')
    readGeo['file'].setValue(geoFile)
    readGeo['storageFormat'].setValue('Ogawa')
    


def run():
    
    filePath = nuke.root()['name'].value()
    
    path_object = PathObject(filePath)
    trackPathFile = filePath.replace('comp','track').replace('.nk','.abc')
    path_object = PathObject(trackPathFile)

    if os.path.isdir(os.path.dirname(trackPathFile)):
        os.makedirs(os.path.dirname(path_object.next_major_version().path_root))
        print('path Exists')
        writeGeo(path_object.next_major_version().path_root)
    
    
    else:
        print('path does not exist') 
        os.makedirs(os.path.dirname(trackPathFile))
        writeGeo(trackPathFile)
