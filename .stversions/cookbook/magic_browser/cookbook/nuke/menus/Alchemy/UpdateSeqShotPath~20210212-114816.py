import nuke
from cgl.core.path import PathObject
from os.path import dirname , isdir
from os import system





def robocopy(oldDir,newDir):
    
#    oldDir = 'Z:/COMPANIES/loneCoconut/render/MENUDO_CGL/shots/VFX_MDO_101/0030/elemKey2/ramon/000.001'
#    newDir = 'Z:/COMPANIES/loneCoconut/render/MENUDO_CGL/shots/VFX_MDO_105/0050/elemKey2/ramon/000.001'
#    
    command = 'robocopy %s %s /S' % (oldDir,newDir)
    
    system('cmd /c "%s"' % command)


#Z:\COMPANIES\loneCoconut\render\MENUDO_CGL\shots\VFX_MDO_101\0030\elemKey2\ramon\000.001


def run():
    
    readNode = nuke.selectedNode() #nodo que esta seleccionado   
    filepath = readNode['file'].getValue() #asigna a filepath el valor de lo que este escrito en file
    path_object = PathObject(filepath) #define un objeto path basando en ese archivo
    
    oldSeq = path_object.seq #me da la secuancia 
    oldShot = path_object.shot # me da el shot
    
    
    newfilepath = nuke.root().name() #asigna a newfilepath el valor del archivo
    newpath_object = PathObject(newfilepath) #define un objeto path basando en ese archivo
    
    newSeq = newpath_object.seq #me da la secuancia 
    newShot = newpath_object.shot # me da el shot
    
    
    
    newFilePath  = filepath.replace(oldShot,newShot).replace(oldSeq,newSeq)
    readNode['file'].setValue(newFilePath)
    
    print('____________')
    oldDir = dirname(dirname(filepath))
    newDir = dirname(dirname(newFilePath))
    
    if not isdir(newDir) and not readNode.Class() == 'Write':
        print newDir + 'does not exists, transfering '
        robocopy(oldDir,newDir)
            
    
  
