import bpy


class switch rig(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Switch Rig'
    bl_label = bl_category

    def draw(self, context):
        """
        in here we'll have all the buttons for the Panel in the order that lumbermill saves them in.
        :param context:
        :return:
        """
        # ADD BUTTONS
        pass




