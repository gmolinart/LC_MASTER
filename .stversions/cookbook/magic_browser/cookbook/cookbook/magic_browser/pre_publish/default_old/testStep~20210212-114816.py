from plugins.preflight.preflight_check import PreflightCheck

class testStep(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        print 'testStep'
        # self.pass_check('Check Passed')
        # self.fail_check('Check Failed')

