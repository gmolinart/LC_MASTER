import glob
import os
from plugins.preflight.preflight_check import PreflightCheck
from cglcore.path import PathObject, CreateProductionData
from cglcore.convert import create_proxy, create_proxy


class CreateProxy(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        # get the sequence to be converted
        path_object = self.shared_data['pub_version']
        print path_object.path_root
        self.shared_data['proxy'] = create_proxy(path_object.path_root)
        print self.shared_data['proxy']
        self.pass_check('Finished Creating Proxies')
        # self.fail_check('Check Failed')