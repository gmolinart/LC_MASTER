from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a lumbermill.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.SOFTWARE import lumbermill


class checkPublishedFiles(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Checking to see if there are files within the "render" folder area.  I should expect that i'm going to get a
        filename, but i will check for it anyway.
        :return:
        """
        path_object = self.shared_data['path_object']
        if path_object.filename:
            if path_object.context != 'render':
                path_object = PathObject.copy(path_object, context='render')
            render_dir = os.path.dirname(path_object.path_root)
            if os.path.exists(render_dir):
                if os.listdir(render_dir):
                    self.pass_check('Found Render Files')
                    return
        else:
            print 'File Name Not Defined'

        self.fail_check('No Render Files Found at: %s \nCheck Failed' % os.path.dirname(path_object.path_root))

