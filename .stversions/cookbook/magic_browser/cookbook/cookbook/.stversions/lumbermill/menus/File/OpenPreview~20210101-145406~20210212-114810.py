import sys
import os
from cgl.plugins.Qt import QtWidgets
from cgl.ui.widgets.base import LJDialog
from cgl.ui.widgets.combo import AdvComboBox
from cgl.core.path import PathObject
from cgl.core.util import cgl_copy



def run(lumbermill):
    path_object = PathObject(lumbermill.path_widget.text.replace('/*', ''))
    print(path_object.latest_version().path_root)
    previewDirectory = os.path.dirname(path_object.path_root).replace('source', 'render') + '/.preview'
    previewFile = os.path.join(previewDirectory, os.listdir(previewDirectory)[0])
    print(previewFile)
    os.system("start " + previewFile)