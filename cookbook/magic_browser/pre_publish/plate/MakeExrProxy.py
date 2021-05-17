from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.magic_browser import magic_browser
from cgl.plugins.magic_browser.utils import image_sequence_exists
from cgl.plugins.magic_browser.tasks.plate import check_frames


class MakeExrProxy(PreflightCheck):

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
        path_object = self.shared_data['path_object']
        proxy_res = path_object.project_info['proxy_resolution']
        padding = '#' * int(path_object.project_info['padding'])
        from cgl.core.path import PathObject
        if check_frames(path_object.path_root, resolutions=['proxy_resolution']) is not []:
            render = path_object.copy(context='render')
            render.filename = '{}_{}_{}_{}'.format(render.seq,
                                                                render.shot,
                                                                render.task,
                                                                padding)

            render_path_object = PathObject(render.path_root.split(' ')[0])
            render_path_object.ext = 'exr {}'.format(render.path_root.split(' ')[1])
            render_path_object.make_proxy(ext='exr', resolution=proxy_res)

        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')