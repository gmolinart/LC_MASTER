from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a lumbermill.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.SOFTWARE import lumbermill


class publishFiles(PreflightCheck):

    def getName(self):
        pass

    def run(self):

        self.shared_data['pub_version'] = publish(path_object)
        print
        self.shared_data['pub_version'].path_root
        if self.shared_data['pub_version']:
            self.pass_check('Files Published')
        else:
            self.fail_check('Files Not Published')

