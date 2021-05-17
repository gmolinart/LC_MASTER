import os
from cgl.core.path import PathObject, CreateProductionData
import logging
from cgl.core.utils.general import split_all, cgl_copy, cgl_execute, clean_file_list
from cgl.ui.widgets.dialog import  InputDialog


def import_task_from(source , user ,version=None ,task=None):
    
    
    path_object = source
    

    if task == None:
        task = path_object.task

    
    if version == None:
        copy_from_path_object  = path_object.copy(user=user, task=task ).latest_version()

    else: 
        copy_from_path_object  = path_object.copy(user = user,version = version,task = task)
    
    
    
    
    current_source = path_object.copy(context='source', filename=None, ext=None).path_root
    current_render = path_object.copy(context='render', filename=None, ext=None).path_root
    
    from_source = copy_from_path_object.copy(context='source', filename=None, ext=None).path_root
    from_render = copy_from_path_object.copy(context='render', filename=None, ext=None).path_root
    
    cgl_copy(from_source,current_source)
    cgl_copy(from_render,current_render)
    
    print("_____________Transfers____________")
    print(current_source)
    print(current_render)
    
    print(from_source)
    print(from_render)






def run(lumbermill):
    
    inputObject = lumbermill.path_widget.text.replace('/*', '')
    path_to_file = inputObject.split(' ')[0]
    currentScene =  PathObject(path_to_file)

    
    dialog = InputDialog(title='import version ', line_edit = True , message='Type in user, version and task in that order, ie. : \nguillermo 000.001 comp\nguillermo latest key \nguillermo 001.000 \nguillermo')
    dialog.exec_()
    print(dialog.input_text)

    userInput = dialog.input_text.split(' ')
    if currentScene.filename:

        import_task_from(source=currentScene, user=userInput[0], version=userInput[1], task=userInput[2])

    else:
        print('please select valid directory')
    # currentScene = PathObject(nuke.root().name())
    #
    # if len(userInput) == 1:
    #     print('only user provided')
    #     import_task_from(source= currentScene, user = userInput[0])
    # if len(userInput) == 2:
    #     if userInput[1] == 'latest':
    #         print('user and latest')
    #         import_task_from(source= currentScene, user = userInput[0])
    #     else:
    #         print('user and version provided')
    #         import_task_from(source= currentScene, user = userInput[0], version =userInput[1])
    #
    # if len(userInput) == 3:
    #     if userInput[1] == 'latest':
    #         print('user ,latest vesion and task provided')
    #         #we should add rename here since it is implied that you are changing tasks
    #         import_task_from(source= currentScene, user = userInput[0], task = userInput[2])
    #
    #     else:
    #         print('user , version  and task provided')
            #we should add rename here since it is implied that you are changing tasks 

