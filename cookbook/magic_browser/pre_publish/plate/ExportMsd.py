from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.magic_browser import magic_browser
from cgl.plugins.magic_browser.tasks.plate import create_msd
from cgl.plugins.magic_browser import alchemy


class ExportMsd(PreflightCheck):

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
        import os
        path_object.start_frame = path_object.project_info['start_frame']
        print(path_object.path_root)
        files_in_folder  = len(os.listdir(path_object.copy(filename = None).path_root))
        path_object.end_frame = int(files_in_folder) + int(path_object.start_frame)
        padding = '#' * int(path_object.project_info['padding'])
        path_object.filename = '{}_{}_{}_{}.{} {}-{}'.format(path_object.seq,
                                            path_object.shot,
                                            path_object.task,
                                            padding,
                                            path_object.ext,
                                            path_object.start_frame,
                                            path_object.end_frame)


        for i in self.shared_data:
            print(i)
        create_msd(path_object.path_root)
        #create_msd(path_object.path_root,user = path_object.user)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
