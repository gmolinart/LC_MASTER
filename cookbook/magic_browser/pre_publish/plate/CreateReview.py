from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.magic_browser.alchemy import review


class CreateReview(PreflightCheck):

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
        print('Creating Review')
        path_object = self.shared_data['path_object']
        review_return = False
        review_return = review(path_object)
        if review_return:
            self.pass_check('Check Passed')
        else:
            self.fail_check('Check Failed')

        self.pass_check