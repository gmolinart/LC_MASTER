from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.blender import alchemy as alc
from cgl.plugins.blender import utils
import bpy

from cgl.plugins.blender.tasks.anim import export_rigs
class WriteAnimationData(PreflightCheck):

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
        print('writting abc ')

        export_rigs()


        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
