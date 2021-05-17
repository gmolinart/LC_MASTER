
import os
from cgl.core.path import PathObject, CreateProductionData

def run(lumbermill):
    print("hello world: Copy Default File")

    inputObject = lumbermill.path_widget.text.replace('/*', '')

    path_to_file = inputObject.split(' ')[0]
    
    path_object = PathObject(path_to_file)
    prod_data = CreateProductionData(path_object)
    prod_data.create_default_file()
    