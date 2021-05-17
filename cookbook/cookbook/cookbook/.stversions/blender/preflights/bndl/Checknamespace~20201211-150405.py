from cgl.plugins.preflight.preflight_check import PreflightCheck
# from cgl.plugins.blender import lumbermill as lm
from cgl.plugins.blender import utils


class Checknamespace(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        script to be executed when the preflight is run.

        If the preflight is successful:
        self.pass_check('Message about a passed Check')

        if the preflight fails:
        self.fail_check('Message about a failed check')
        :return:
        """
        print('Checknamespace')
        failed_objects = []
        for obj in bpy.data.objects:
            if obj.is_instancer:
                if ':' not in obj.name:
                    failed_objects.append(obj.name)

        if failed_objects == []:

            self.pass_check('Check Passed')

        else:
            self.fail_check(
                'the object has no namespace, this could be because referenced in incorrectly , '
                'Please re reference : {}'.format(
                    failed_objects))

