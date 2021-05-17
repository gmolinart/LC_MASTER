from plugins.preflight.preflight_check import PreflightCheck


class CreateExrProxy(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        # resolution determined from app_config()['default']['proxy_resolution']['project']
        # if not project name is found in globals 1920x1080 is proxy resolution.
        self.shared_data['publish_path_object'].make_proxy(ext='exr')
        self.pass_check('Check Passed')

