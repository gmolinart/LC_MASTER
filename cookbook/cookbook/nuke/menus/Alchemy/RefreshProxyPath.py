import nuke
import nukescripts
from cgl.core.path import PathObject, lj_list_dir

from cgl.plugins.nuke.cgl_nuke import get_proxy_resolution
from cgl.core.config import app_config
import os


def checkIfProxyExist():
    for n in nuke.allNodes():
        validNodeClasses = ['Read', 'Write']
        if n.Class() in validNodeClasses:
            proxydir = os.path.dirname(n['proxy'].getValue())
            if not os.path.isdir(proxydir):
                print('no such dir')
                print
                proxydir
                n['tile_color'].setValue(4278190335)
            else:
                n['tile_color'].setValue(0)


def setAllProxies(path_object):
    filepath = nuke.root().name()
    validNodeClasses = ['Read', 'Write']
    for n in nuke.allNodes():

        if n.Class() in validNodeClasses:
            filePathObject = PathObject(n['file'].getValue())

            proxyFile = filePathObject.copy(resolution=get_proxy_resolution()).path_root
            n['proxy'].setValue(proxyFile)


def run():
    filepath = nuke.root().name()
    path_object = PathObject(filepath)
    setAllProxies(path_object)
    checkIfProxyExist()
    print("all proxy paths set ")


