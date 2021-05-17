from plugins.preflight.preflight_check import PreflightCheck
from cglcore.path import publish


class publish_files(PreflightCheck):

    def getName(self):
        pass

    def run(self):
         
        self.shared_data['pub_version'] = publish(path_object)
        print self.shared_data['pub_version'].path_root
        if self.shared_data['pub_version']:
            self.pass_check('Files Published')
        else:
            self.fail_check('Files Not Published')

	