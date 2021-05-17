from cgl.plugins.preflight.preflight_check import PreflightCheck
import os
from cgl.core.path import PathObject
from cgl.core.config.config import ProjectConfig


class CreateProxyHd(PreflightCheck):
    def getName(self):
        pass

    def run(self):
        path_object = self.shared_data['path_object']

        path_object.make_proxy()

        self.pass_check('Check Passed')

        # else:
        #     self.fail_check('Check Failed: proxy is set to True continue?? ')
