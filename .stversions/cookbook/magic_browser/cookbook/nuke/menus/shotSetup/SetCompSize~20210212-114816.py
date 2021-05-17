import nuke
import nukescripts
from cgl.core.path import PathObject, lj_list_dir
from cgl.core.config import app_config
from cgl.plugins.nuke.cgl_nuke import NukePathObject
from cgl.core.config import app_config
from cgl.plugins.nuke.cgl_nuke import set_comp_default_settings



def run():
    set_comp_default_settings()