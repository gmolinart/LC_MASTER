from plugins.preflight.preflight_check import PreflightCheck
from plugins.nuke.cgl_nuke import save_file
import nuke 

from cgl.core.path import PathObject
import os 
import shutil

class SaveScene(PreflightCheck):

    def getName(self):
        pass
        
    def renameFile(self,inputObject):
        path_object = PathObject(inputObject)
        current_directory = os.path.dirname(path_object.path_root)
        correctName = '%s_%s_%s.%s' % (path_object.seq,
                                    path_object.shot,
                                    path_object.task,
                                    path_object.ext)
        correctNamePath = current_directory + '/' + correctName
        



        return correctNamePath

    def createSourceCopy(self):
        #os.rename(path_object.path_root, correctNamePath)
        
        selectedNode = nuke.selectedNode()
        path_object = PathObject(selectedNode['file'].getValue())
        
        nodeName = selectedNode['name'].getValue()
        if 'elem' in nodeName or 'key' in nodeName :
        
            fileName = path_object.task + '.nk'
            dirname = os.path.dirname(path_object.path_root).replace('render','source')
            
            newFile = self.renameFile(dirname + '/' + fileName)
            source =  nuke.root().name() 
            print 1
            print newFile
            print source
            
            if not os.path.isdir(dirname):
                os.makedirs(dirname)

            
            shutil.copy(source,newFile) 

    def run(self):
        save_file()
        self.createSourceCopy()
        self.pass_check('Check Passed: Scene Saved')
        # self.fail_check('Check Failed')

