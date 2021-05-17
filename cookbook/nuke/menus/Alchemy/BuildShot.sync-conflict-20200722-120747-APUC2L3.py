import nuke
import nukescripts
from cgl.core.path import PathObject, lj_list_dir
from cgl.core.config import app_config
import os


from cgl.plugins.nuke.cgl_nuke import NukePathObject


def run():
    filepath = nuke.root().name()
    excludedElements = ['comp']
    spread = 0
    filepath = nuke.root().name()
    path_object = PathObject(filepath)


    CONFIG = app_config()

    if path_object.project in CONFIG['default']['proxy_resolution'].keys() :
        proxy_resolution = CONFIG['default']['proxy_resolution'][path_object.project]
    else:
        proxy_resolution = CONFIG['default']['proxy_resolution']['default']

    all_tasks = path_object.glob_project_element('task', full_path=True)
        
        
    def importLut():
        
        
        lutPath = r'Z:\COMPANIES\loneCoconut\render\project\assets\prod\LUT\lut\publish\001.000\high\prod_LUT_lut.nk'
    
        from cgl.core.path import PathObject
        path_object = PathObject(nuke.root().name())
        lutPath = lutPath.replace('project',path_object.project)
        print(lutPath)
        
        
        nuke.nodePaste(lutPath)
    
    def setAllProxies(path_object):
        filepath = nuke.root().name()
        for n in nuke.allNodes():
            
            CONFIG = app_config()
        
            if path_object.project in CONFIG['default']['proxy_resolution'].keys() :
                proxy_resolution = CONFIG['default']['proxy_resolution'][path_object.project]
            else:
                proxy_resolution = CONFIG['default']['proxy_resolution']['default']
        
            all_tasks = path_object.glob_project_element('task', full_path=True)
            
        
            if n.Class() == 'Read':
                proxyFile = n['file'].getValue().replace('high',proxy_resolution)
                n['proxy'].setValue(proxyFile)
            




    def import_media(filepath, name=None):
        """
        imports the filepath.  This assumes that sequences are formated as follows:
        [sequence] [sframe]-[eframe]
        sequence.####.dpx 1-234
        regular files are simply listed as a string with no frame numbers requred:
        bob.jpg
        this will also look for an HD proxy file, first jpgs and then exrs.
        :param filepath:
        :return:
        """
        read_node = nuke.createNode('Read')
        if name:
            read_node.knob('name').setValue(name)
        read_node.knob('file').fromUserText(filepath)
        path_object = NukePathObject(filepath)
        proxy_object = PathObject(filepath).copy(resolution=path_object.proxy_resolution, ext='exr')
        dir_ = os.path.dirname(proxy_object.path_root)
        if os.path.exists(dir_):
            read_node.knob('proxy').fromUserText(proxy_object.path_root)
        return read_node


    def makePathRelative():
        nuke.root().knob('project_directory').setValue('[python {nuke.script_directory()}]')

        for i in nuke.allNodes('Read'):


            filePath = i
            print i.name()

            relativePath = os.path.relpath(filePath['file'].value() ,nuke.script_directory())

            print
            filePath.knob('file').setValue(relativePath.replace(os.sep, '/'))

            # print relativePath

    def setCompDefaultSettings(proxy_res='1920x1080', readNode=nuke.toNode('plate_Read'), alert=False):
        if not readNode:
            readNode = nuke.selectedNode()

        selectedFormat = readNode['format'].value()
        nuke.root()['format'].setValue(selectedFormat)

        firstFrame = int(readNode.knob('first').getValue())
        lastFrame = int(readNode.knob('last').getValue())

        LC_PROXY = '%s LC_PROXY' % proxy_res.replace('x', ' ')

        # Setup proxy settings
        nuke.addFormat(LC_PROXY)
        nuke.root()['proxy_type'].setValue('format')
        nuke.root()['proxy_format'].setValue('LC_PROXY')
        nuke.root()['proxySetting'].setValue('if nearest')
        readNode['proxy_format'].setValue('LC_PROXY')
        nuke.root()['proxySetting'].setValue('if nearest')

        if alert:
            nuke.alert("Comp Size, duration and proxy set")


    def createWriteNodes(pathToElem, spread=0, backdrops=True):
        p_obj = pathToElem

        if not nuke.toNode(p_obj.task + '_Read'):

            import_media(os.path.join(p_obj.path_root, lj_list_dir(p_obj.path_root)[0]))
            readNode = nuke.selectedNode()


            readNode['xpos'].setValue(spread)


            if backdrops:
                backdrop = nukescripts.autoBackdrop()
                backdrop['label'].setValue(p_obj.task)
                backdrop['xpos'].setValue(spread)
                backdrop['name'].setValue(p_obj.task + '_Backdrop')

            readNode['name'].setValue(p_obj.task + '_Read')

        else:
            p_obj.task + ' already exists'



    for t in all_tasks:
        p_obj = PathObject(t).copy(context='render', user='publish', resolution='high', latest=True)
        if p_obj.task not in excludedElements:
            if os.path.isdir(p_obj.path_root):
                createWriteNodes(p_obj ,spread)
                spread += 250

        if p_obj.task == 'plate':
            nuke.toNode('plate_Read')['selected'].setValue(True)
            setCompDefaultSettings(proxy_resolution)
            nuke.root()['proxySetting'].setValue('always')
            
    importLut()
    setAllProxies(path_object)

    #makePathRelative()


