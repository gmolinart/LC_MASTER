from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.nuke import alchemy as alc
from cgl.plugins.nuke import utils

class RenderProxy(PreflightCheck):

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

        utils.switch_proxy(True)
        scene = alc.scene_object()
        padding = '#' * int(path_object.project_info['padding'])
        proxy_file = scene.copy(resolution = scene.project_info['proxy_resolution'])
        proxy_file.filename = '{}_{}_{}_{}.{} {}-{}'.format(proxy_file.seq,
                                                             proxy_file.shot,
                                                             proxy_file.task,
                                                             padding,
                                                             proxy_file.ext,
                                                             proxy_file.start_frame,
                                                             proxy_file.end_frame)

        alc.save_file(proxy_file.path_root)
        alc.render(proxy=True)

        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
