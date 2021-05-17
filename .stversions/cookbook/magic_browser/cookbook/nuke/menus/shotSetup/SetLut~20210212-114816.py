import nuke
import nukescripts
from cgl.core.path import PathObject, lj_list_dir
from cgl.core.config import app_config
import os
from cgl.core.path import PathObject


def importLut():
    current_shot = PathObject(nuke.root().name())

    dict_ = {'company': 'loneCoconut',
             'context': 'render',
             'project': current_shot.project,
             'scope': 'assets',
             'seq': 'lib',
             'shot': 'LUT',
             'task': 'lut',
             'user': 'publish',
             'resolution': 'high',
             'filename': 'lib_LUT_lut.nk'
             }

    path_object = PathObject(dict_)
    lutPath = path_object.latest_version().path_root




    path_object = PathObject(nuke.root().name())
    lutPath = lutPath.replace('project',path_object.project)
    print(lutPath)
    
    
    nuke.nodePaste(lutPath)




def duplicate_node(node, to_file = None):
    """Slightly convoluted but reliable(?) way duplicate a node, using
    the same functionality as the regular copy and paste.
    Could almost be done tidily by doinglu:
    for knobname in src_node.knobs():
        value = src_node[knobname].toScript()
        new_node[knobname].fromScript(value)
    ..but this lacks some subtly like handling custom knobs
    to_file can be set to a string, and the node will be written to a
    file instead of duplicated in the tree
    """

    # Store selection
    orig_selection = nuke.selectedNodes()

    # Select only the target node
    [n.setSelected(False) for n in nuke.selectedNodes()]
    node.setSelected(True)

    # If writing to a file, do that, restore the selection and return
    if to_file is not None:
        nuke.nodeCopy(to_file)
        [n.setSelected(False) for n in orig_selection]
        return


    # Copy the selected node and clear selection again
    nuke.nodeCopy("%clipboard%")
    node.setSelected(False)

    if to_file is None:
        # If not writing to a file, call paste function, and the new node
        # becomes the selected
        nuke.nodePaste("%clipboard%")
        new_node = nuke.selectedNode()

    # Restore original selection
    [n.setSelected(False) for n in nuke.selectedNodes()] # Deselect all
    [n.setSelected(True) for n in orig_selection] # Select originally selected

    return new_node



def createDuplicate():
    sourceLut = nuke.selectedNode()
    newNode = duplicate_node(sourceLut)
    
    
    
    newNode['name'].setValue(sourceLut['name'].getValue() + '_inverted')
    newNode['direction'].setValue(1)
    newNode.setInput(0,sourceLut)
    newNode['xpos'].setValue(sourceLut['xpos'].getValue())
    newNode['disable'].setExpression('proxy')
    inputProcess = duplicate_node(newNode)
    inputProcess['direction'].setValue(0)
    inputProcess['name'].setValue('VIEWER_INPUT')


def run():
    if nuke.Root().selectedNode():
        createDuplicate()
    else : 
        importLut()