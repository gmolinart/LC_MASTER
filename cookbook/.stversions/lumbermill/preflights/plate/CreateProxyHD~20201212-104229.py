import glob
import os
from plugins.preflight.preflight_check import PreflightCheck
from cglcore.path import PathObject, CreateProductionData
from cglcore.convert import create_hd_proxy


class CreateProxyHD(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        path_object = self.shared_data['pub_version']
        self.shared_data['hdProxy'] = create_hd_proxy(path_object.path_root)
        self.pass_check('Finished Creating Proxies')
        # self.fail_check('Check Failed')

