from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.nuke import alchemy as alc
from cgl.plugins.nuke.utils import select_node

class CheckLutInScene(PreflightCheck):

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
        
                
        lut = select_node('LUT')

        if lut.name() == 'LUT':
            print('LUT NODE FOUND')
            self.pass_check('Check Passed')
        
        else:
            print('Couldnt find Lut, pleas add an OcioCdlTransform and rename it to LUT all caps')
            self.fail_check('Couldnt find Lut, pleas add an OcioCdlTransform and rename it to LUT all caps')
