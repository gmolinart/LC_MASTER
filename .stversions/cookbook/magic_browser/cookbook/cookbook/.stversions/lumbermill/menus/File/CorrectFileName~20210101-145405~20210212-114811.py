import os
from cgl.core.path import PathObject

def renameSequence(inputObject):
     
    path_to_file = inputObject.split(' ')[0].replace('/','\\')
    
    path_object = PathObject(path_to_file)
   
    
    
    inName =  path_object.ext
    frame = 1001 
    baseDir = os.path.dirname(path_to_file)
    print(1111111111111111111)
    print(baseDir)
    #current_directory = os.path.dirname(path_object.path_root)
    files = []

    files = (file for file in os.listdir(baseDir) 
         if os.path.isfile(os.path.join(baseDir, file)))
    for file in files: 
        print(file)
        newName = '%s_%s_%s.%04d.%s' % (path_object.seq , path_object.shot,path_object.task, frame, path_object.ext)
        frame +=1
        current = os.path.join(baseDir,file)
        new = os.path.join(baseDir,newName)
        
        os.rename(current,new)
        #print( os.path.join(baseDir,newName))  
    

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


    elif len(inputObject.split(' ')) == 2:
        renameSequence(inputObject)
        
        #print('sequenceRenamed')

