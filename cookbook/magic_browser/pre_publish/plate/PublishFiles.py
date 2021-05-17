from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.magic_browser.alchemy import publish


class PublishFiles(PreflightCheck):

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
        path_object = self.shared_data['path_object']
        main_folder = path_object.copy(filename = None, resolution = None, ext=None)
        print(main_folder.path_root)
        publish(main_folder)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
