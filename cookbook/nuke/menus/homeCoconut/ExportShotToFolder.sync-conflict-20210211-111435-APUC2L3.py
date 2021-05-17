import nuke
import os 
from subprocess import call
from cgl.core.path import PathObject, CreateProductionData






def run():
    
    
    
    
    def publishVersion():
        
        filepath = nuke.root().name()
        path_object = PathObject(filepath)
        
        
        
        
        next_version_object = path_object.new_minor_version_object() # returns a pathObject reflecting the next version globally.
        nextPublishedVersion = next_version_object.path_root
        nextPublishedVersionDir = os.path.dirname(nextPublishedVersion)
        
        
            
        if not os.path.exists(nextPublishedVersionDir):
            os.makedirs(nextPublishedVersionDir)
        
        
        nuke.scriptSaveAs(nextPublishedVersion)
         
    
    
    
    
    
    def setProject(driveLetter ='Z:/'):
    
        nuke.root()['project_directory'].setValue(driveLetter)
    
        filepaths = []
    
        for node in nuke.allNodes(recurseGroups=True):
            for knob in node.allKnobs():
                if knob.Class() == "File_Knob":
                    filepath = knob.getEvaluatedValue()
                    if filepath:
                        node['file'].setValue(node['file'].getValue().replace(driveLetter,''))
        
    
    
    def swapPath(path,drive,server ='Z:'): # hay que ponerle 2 punto si no se jode 
        newPath = path.replace(server,drive)
        return newPath
    
    
    
        
    
    
    drive = nuke.getInput('path of exported project') + ':'
    
    
    if drive : 
    
        
    
        
        #drive = 'E'+ ':'
        server = 'Z:'
        setProject()
        publishVersion()
        
        shotName = '/'.join(nuke.root().name().split('/')[:-5])
        sourcePath,renderPath = shotName, shotName.replace('source','render') 
        
        
        
        call(["robocopy", sourcePath, swapPath(sourcePath,drive), "/S"])
        call(["robocopy", renderPath, swapPath(renderPath,drive), "/S"])
        
        
    
