from cgl.core.path import PathObject, CreateProductionData
import nuke
import os

def run():
    
    filepath = nuke.root().name()
    path_object = PathObject(filepath)
    
    print path_object.user
    
    print path_object.next_major_version_number()
    next_version_object = path_object.next_major_version() # returns a pathObject reflecting the next version globally.
    nextPublishedVersion = next_version_object.path_root.replace(path_object.user,'publish')
    nextPublishedVersionDir = os.path.dirname(nextPublishedVersion)
    
    print(nextPublishedVersionDir)
    if nuke.ask('Do you want to publish this file????'):
        
        if not os.path.exists(nextPublishedVersionDir):
            os.makedirs(nextPublishedVersionDir)
        
        
        nuke.scriptSaveAs(nextPublishedVersion)
        
            
     