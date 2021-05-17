import glob
import os
from plugins.preflight.preflight_check import PreflightCheck
from cglcore.path import PathObject, lj_list_dir
from cglcore.convert import create_gif_proxy, create_gif_thumb


class CreateProxyGif(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        # get the sequence to be converted
        from_file = self.shared_data['hdProxy']
        create_gif_proxy(from_file)
        create_gif_thumb(from_file)
        self.pass_check('Finished Creating Gifs!')

