from plugins.preflight.preflight_check import PreflightCheck
import nuke

class TurnOffProxy(PreflightCheck):

    def getName(self):
        pass
    def checkProxy(self):
        	if 'elem'  in nuke.selectedNode().name():
        	    nuke.root().setProxy(False)
    def run(self):
        self.checkProxy()
        self.pass_check('Check Passed')
        #self.fail_check('Check Failed')

