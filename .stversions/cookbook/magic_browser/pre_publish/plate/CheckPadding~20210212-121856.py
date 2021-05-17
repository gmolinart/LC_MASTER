from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.magic_browser import magic_browser
import os 


class CheckPadding(PreflightCheck):

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
        folder = path_object.copy(filename = '')
        files = os.listdir(folder.path_root)
        frame_lenght =len(files) 
        start_frame = int(path_object.project_info['start_frame'])
        current_frame = start_frame
        for file in os.listdir(folder.path_root):
            
            filename = os.path.splitext(file)[0]
            
            new_name = '{}_{}_{}_{}.{}'.format(path_object.seq,
                                            path_object.shot,
                                            path_object.task,
                                            current_frame,
                                            path_object.ext.split(' ')[0])
                                           
            old_name = "{}/{}".format(folder.path_root, file)
            new_name = "{}/{}".format(folder.path_root, new_name)
            print(old_name)
            print(new_name)
            if not file.startswith('.'):
                if old_name != new_name:
                    os.rename(old_name,new_name)

                current_frame +=1


        self.pass_check('Check Passed')
        
        # self.fail_check('Check Failed')
