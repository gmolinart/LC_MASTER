from plugins.preflight.preflight_check import PreflightCheck


class AutoCuts(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        print 'AutoCuts'
        # self.pass_check('Check Passed')
        # self.fail_check('Check Failed')

