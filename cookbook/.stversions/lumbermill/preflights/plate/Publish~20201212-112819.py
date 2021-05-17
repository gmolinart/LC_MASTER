from cgl.plugins.preflight.preflight_check import PreflightCheck
import os
# there is typically a lumbermill.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.SOFTWARE import lumbermill


class Publish(PreflightCheck):

    def getName(self):
        pass


    def run(self):
             
    	     
	path_to_file = inputObject.split(' ')[0].replace('/','\\')
    
	path_object = PathObject(path_to_file)
        sourceFolder = os.path.dirname(path_object.path).replace('render', 'source')

        path_object.publish()
        passes = path_object.publish()

        if passes:
            self.pass_check('Files Published')
        else:
            self.fail_check('Files Not Published')




