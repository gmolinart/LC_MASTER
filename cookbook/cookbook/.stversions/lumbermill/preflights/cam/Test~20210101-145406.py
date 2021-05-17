from plugins.preflight.preflight_check import PreflightCheck


class Test(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        print 'Test'
        # self.pass_check('Check Passed')
        # self.fail_check('Check Failed')

