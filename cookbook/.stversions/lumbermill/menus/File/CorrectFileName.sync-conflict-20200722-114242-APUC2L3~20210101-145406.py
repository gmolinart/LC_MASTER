import os
from cgl.core.path import PathObject

def renameSequence(inputObject):
     
    pathtoFile = inputObject.split(' ')[0]
    
    path_object = PathObject(pathtoFile)
    
    
    inName =  path_object.filename_base.split('.')[0]
    frame = 1 
    baseDir = os.path.dirname(path_object.path_root)
    
    for i in os.listdir(baseDir):
        if  i.split('.')[0] == inName:
            newName = '%s_%s_%s.%08d.%s' % (path_object.seq , path_object.shot,path_object.task, frame, path_object.ext)
            frame +=1
            os.rename(os.path.join(baseDir, i) ,  os.path.join(baseDir,newName))    


def run(lumbermill):
    inputObject = lumbermill.path_widget.text.replace('/*', '')
    print(inputObject)

    if len(inputObject.split(' ')) == 1 : 
    
        path_object = PathObject(inputObject)
        current_directory = os.path.dirname(path_object.path_root)
        correctName = '%s_%s_%s.%s' % (path_object.seq,
                                    path_object.shot,
                                    path_object.task,
                                    path_object.ext)
        correctNamePath = os.path.join(current_directory,correctName)
        os.rename(path_object.path_root, correctNamePath)


    if len(inputObject.split(' ')) == 2:
        renameSequence(inputObject)
        print('sequenceRenamed')
