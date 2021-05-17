from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.core.path import PathObject


class Publish(PreflightCheck):

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

