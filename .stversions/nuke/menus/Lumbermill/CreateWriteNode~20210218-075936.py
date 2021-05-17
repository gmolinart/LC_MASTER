from cgl.core.path import PathObject
# noinspection PyPackageRequirements
import nuke
from cgl.plugins.nuke.gui import create_write_node

def run():
    write_node = create_write_node()
    print write_node

    matteKeywords = ['Matte','Key']
    nodeName = write_node['name'].getValue()
    for word in matteKeywords:
        if  word in nodeName:
            fileknob =  write_node['file'].getValue()
            keyName = fileknob.replace('exr','jpg').replace('elemMatte','key').replace('elemKey','key')
            write_node['file'].setValue(keyName)
            write_node['name'].setValue('key')
            write_node['file_type'].setValue('jpeg')
            write_node['_jpeg_sub_sampling'].setValue(1)
            write_node['_jpeg_quality'].setValue(1.0)
            nuke.createNode('LC_QC_Mattes')

