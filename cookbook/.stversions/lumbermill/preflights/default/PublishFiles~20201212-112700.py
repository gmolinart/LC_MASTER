from cgl.plugins.preflight.preflight_check import PreflightCheck
import os
# there is typically a lumbermill.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.SOFTWARE import lumbermill


class PublishFiles(PreflightCheck):

    def getName(self):
        pass


    def run(self):
        path_object = self.shared_data['path_object']
        sourceFolder = os.path.dirname(path_object.path).replace('render', 'source')

        if not os.path.isdir(sourceFolder):
            #os.mkdir(sourceFolder)
            print('%s Folder Created' % sourceFolder)

        path_object.publish()
        passes = path_object.publish()
        if passes:
            self.pass_check('Files Published')
        else:
            self.fail_check('Files Not Published')




