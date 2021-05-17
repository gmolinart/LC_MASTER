from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.blender import lumbermill as lm
# from cgl.plugins.blender import utils
import bpy

class CheckHirarchy(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        script to be executed when the preflight is run.

        If the preflight is successful:
        self.pass_check('Message about a passed Check')

        if the preflight fails:
        self.fail_check('Message about a failed check')
        :return:
        """
        print('Checkhirarchy')

        model = lm.get_object('mdl')
        resolution = lm.get_object('high')

        if model:
            if resolution:
                if resolution.parent == model:
                    self.pass_check('Check Passed')
                else:
                    self.fail_check('resolution not parented to mdl task')
            else:
                self.fail_check('no "high" resolution group found, please create it or click the build button')
        else:
            self.fail_check('no "mdl" group found, please create it or click the build button')


        # self.fail_check('Check Failed')
