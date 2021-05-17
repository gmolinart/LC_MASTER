import bpy
# from cgl.plugins.blender import lumbermill as lm

class CurrentFrame(bpy.types.Operator):
    """
    This class is required to register a button in blender.
    """
    bl_idname = 'object.current_frame'
    bl_label = 'Current Frame'

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        run()
        return {'FINISHED'}


def run():
    """
    This run statement is what's executed when your button is pressed in blender.
    :return:
    """

    for area in bpy.context.screen.areas:
        if area.type == 'DOPESHEET_EDITOR':
            for region in area.regions:
                if region.type == 'WINDOW':
                    ctx = bpy.context.copy()
                    ctx['area'] = area
                    ctx['region'] = region
                    ctx['mode'] = 'TIMELINE'
                    bpy.ops.action.view_all(ctx)

    print('Hello World!: button_template')
