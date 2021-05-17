from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.magic_browser import magic_browser


class MoveFilesToRender(PreflightCheck):

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
        from cgl.core.utils.general import cgl_copy
        import os
        
        path_object = self.shared_data['path_object']
        if path_object.context == 'source':
            source_dir = path_object.copy(filename= '')
            render_dir = path_object.copy(filename= '',context = 'render')
            cgl_copy(source_dir.path_root,render_dir.path_root)
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
