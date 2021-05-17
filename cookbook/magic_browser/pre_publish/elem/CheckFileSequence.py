from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.magic_browser import magic_browser
from cgl.plugins.magic_browser.tasks.plate import check_frames
import os 

class CheckFileSequence(PreflightCheck):

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
        frame_match = check_frames(path_object.path_root)
        source_dir = path_object.copy(filename= '')
        try:
            #for source_file in os.listdir(source_dir.path_root):
            os.remove(source_dir.path_root)
            os.makedirs(source_dir.path_root)
        except:
            print('error removing source files')
            pass

        if frame_match == []:

            self.pass_check('Check Passed')
        else: 
            self.fail_check('Check Failed, {}'.format(frame_match))
