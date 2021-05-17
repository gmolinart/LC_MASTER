import bpy
import json
from os.path import isdir, isfile
from cgl.plugins.blender import lumbermill as lm
from cgl.plugins.blender import utils as utils


class Build(bpy.types.Operator):
    """
    Builds the shot with all the avilable elements
    """
    bl_idname = 'object.build'
    bl_label = 'Build'

    def execute(self, context):
        run()
        return {'FINISHED'}


def defaultShotSettings():
    scene = bpy.context.scene
    scene.eevee.taa_render_samples = 1
    scene.eevee.taa_samples = 1
    scene.eevee.shadow_cube_size = '2048'


def gather_dependencies():
    current = lm.scene_object()

    # Gather Dependencies
    light_file = current.copy(task='light', filename='%s_%s_%s.blend' % (
        current.seq, current.asset, 'light')).latest_version()

    anim_file = current.copy(task='anim', filename='%s_%s_%s.blend' % (
        current.seq, current.asset, 'anim')).latest_version()

    layout_file = current.copy(task='lay',
                               filename='{}_{}_{}'.format(current.seq, current.asset, 'lay'),
                               ext='json',
                               user='publish').latest_version()

    camera_file = current.copy(task='cam',
                               filename='{}_{}_{}'.format(current.seq, current.asset, 'cam'),
                               ext='fbx',
                               user='publish').latest_version()

    dependencies = [light_file, anim_file, layout_file, camera_file]

    return dependencies


def required_dependencies():
    requirements = []
    current = lm.scene_object()

    if current.task == 'lay':
        requirements.append('lay')
        requirements.append('cam')

    if current.task == 'anim':
        requirements.append('lay')
        requirements.append('cam')
    return requirements


def import_dependencies():
    for depObject in gather_dependencies():
        print(depObject.path_root)
        print(depObject.task)

        if depObject.task in required_dependencies():
            if isfile(depObject.path_root):
                print('{} exists'.format(depObject.path_root))

                if depObject.task == 'lay':
                    print('_____LAYOUT______')
                    print(depObject.filename)
                    utils.read_layout()
                    burn_in_image()

                if depObject.task == 'cam':
                    print('_________CAMERA____________')
                    print(depObject.filename)
                    print(111111111111111)
                    json = depObject.copy(ext='json')
                    print(json)
                    lm.import_file(depObject.path_root)
                    set_shot_duration(json)

                if depObject.task == 'anim':
                    print('_____ANIM______')
                    print(depObject.filename)
                    utils.read_layout()
                    burn_in_image()

            else:
                print('{} object not Available'.format(depObject.task))

        else:
            print('{} object not Required'.format(depObject.task))


def burn_in_image():
    current = bpy.context.scene
    mSettings = current.render
    sceneObject = lm.scene_object()

    current.name = sceneObject.filename_base
    mSettings.stamp_font_size = 26
    mSettings.use_stamp = 1
    mSettings.use_stamp_camera = 1
    mSettings.use_stamp_date = 0
    mSettings.use_stamp_frame = True
    mSettings.use_stamp_frame_range = 0
    mSettings.use_stamp_hostname = 0
    mSettings.use_stamp_labels = 0
    mSettings.use_stamp_lens = 1
    mSettings.use_stamp_marker = 0
    mSettings.use_stamp_memory = 0
    mSettings.use_stamp_note = 0
    mSettings.use_stamp_render_time = 0
    mSettings.use_stamp_scene = 1
    mSettings.use_stamp_sequencer_strip = 0
    mSettings.use_stamp_strip_meta = 0
    mSettings.use_stamp_time = 1


def set_shot_duration(camJson):
    # dependencies  = gather_dependencies()
    # print(dependencies)
    default_start_frame = 1000
    current = lm.scene_object()
    filename = camJson

    # filename = '{}_{}_{}.json'.format(current.seq, current.asset, 'cam')
    # outFile = lm.scene_object().copy(task='cam', filename=filename).path_root
    outFile = camJson.path_root

    with open(outFile) as json_file:
        data = json.load(json_file)

    bpy.context.scene.frame_start = 1001
    print('________________________frameset____________')
    print('{} start'.format(data['frame_start']))
    print('{} end'.format(data['frame_end']))

    endFrame = data['frame_end'] - data['frame_start']
    bpy.context.scene.frame_end = 1001 + int(endFrame)
    bpy.context.scene.frame_current = 1001
    print(endFrame)


def buildShot():
    defaultShotSettings()
    import_dependencies()
    burn_in_image()


def run():
    """
    This run statement is what's executed when your button is pressed in blender.
    :return:
    """
    buildShot()
