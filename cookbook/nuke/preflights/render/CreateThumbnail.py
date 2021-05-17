from plugins.preflight.preflight_check import PreflightCheck
from cgl.core.config import UserConfig
PROCESSING_METHOD = UserConfig().d['methodology']
class CreateThumbnail(PreflightCheck):
    def getName(self):
        pass
    def run(self):
        print 'CreateThumbnail'
        if PROCESSING_METHOD == 'local':
            print self.shared_data['thumb_path']
            self.shared_data['render_path_object'].make_thumbnail()
            self.pass_check('Check Passed')
            # self.fail_check('Check Failed')
        else:
            self.pass_check("Check Passed, thumb was created on the farm already.")