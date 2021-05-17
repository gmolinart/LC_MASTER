from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.magic_browser import magic_browser
from os import rename
import os


class CheckElemName(PreflightCheck):

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
        folder = path_object.copy(filename='', context = 'source')
        files = os.listdir(folder.path_root)
        frame_lenght = len(files)
        start_frame = int(path_object.project_info['start_frame'])
        current_frame = start_frame

        for file in os.listdir(folder.path_root):

            filename = os.path.splitext(file)[0]

            new_name = '{}_{}_plate_{}.exr'.format(path_object.seq,
                                                     path_object.shot,
                                                     current_frame)

            old_name = "{}/{}".format(folder.path_root, file)
            new_name = "{}/{}".format(folder.path_root, new_name)
            print(old_name)
            print(new_name)
            if not file.startswith('.'):
                try:


                    os.rename(old_name, new_name)

                    current_frame += 1
                except FileExistsError:
                    print('cant rename a file that already exists')
                    pass

        self.pass_check('Check Passed')

