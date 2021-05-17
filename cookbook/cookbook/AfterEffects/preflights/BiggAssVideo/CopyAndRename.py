from plugins.preflight.preflight_check import PreflightCheck


class CopyAndRename(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        print 'CopyAndRename'
        # self.pass_check('Check Passed')
        # self.fail_check('Check Failed')

