
import os
from cgl.core.path import PathObject, CreateProductionData
import logging
from cgl.core.utils.general import split_all, cgl_copy, cgl_execute, clean_file_list
def run(lumbermill):
    

    inputObject = lumbermill.path_widget.text.replace('/*', '')
    
    path_to_file = inputObject.split(' ')[0]
    
    path_object = PathObject(path_to_file)


    current_source = path_object.copy(context='source', filename=None, ext=None).path_root
    current_render = path_object.copy(context='render', filename=None, ext=None).path_root
    # create the next major version folders to copy to
    next_major = path_object.copy(context='source', filename=None, ext=None)
    next_major = next_major.next_major_version()
    next_major_render = next_major.copy(context='render').path_root
    next_major_source = next_major.path_root
    publish = next_major.copy(user='publish')
    publish_source = publish.path_root
    path_object.publish_source = publish_source
    publish_render_object = publish.copy(context='render')
    publish_render = publish_render_object.path_root
    path_object.publish_render = publish_render
    logging.debug('Publishing %s to %s' % (current_source, next_major_source))
    cgl_copy(current_source, next_major_source)
    logging.debug('Publishing %s to %s' % (current_source, publish_source))
    cgl_copy(current_source, publish_source)
    logging.debug('Publishing %s to %s' % (current_render, next_major_render))
    cgl_copy(current_render, next_major_render)
    logging.debug('Publishing %s to %s' % (current_render, publish_render))
    cgl_copy(current_render, publish_render)
    logging.debug('--------- Finished Publishing')
    return publish_render_object
    
    #prod_data = CreateProductionData(path_object)
    #prod_data.create_default_file()
    