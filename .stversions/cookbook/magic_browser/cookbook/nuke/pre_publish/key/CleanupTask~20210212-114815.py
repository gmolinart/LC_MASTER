from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.nuke import alchemy as alc
from cgl.plugins.nuke import utils

class CleanupTask(PreflightCheck):

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
        print('REvisa el archivo y borra todo o que no este en el backdrop')



        utils.keep_tagged_nodes(value = 'key')
        self.pass_check('REvisa el archivo y borra todo o que no este en el backdrop')
        # self.fail_check('Check Failed')
