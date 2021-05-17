from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.nuke import alchemy as alc


class OpenSource(PreflightCheck):

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
        print('PreflightTemplate')
        scene = alc.scene_object()
        high_file = scene.copy(resolution='high')
        alc.open_file(high_file.path_root)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
