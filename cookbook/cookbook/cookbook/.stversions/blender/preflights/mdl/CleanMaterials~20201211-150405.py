from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.blender import lumbermill as lm
from cgl.plugins.blender import utils
from cgl.plugins.blender.tasks import shd


class CleanMaterials(PreflightCheck):

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


        for object in utils.return_object_list('mdl'):
            lm.selection(object)

        material_check = shd.check_material_count()
        if material_check == []:
            self.pass_check('Check Passed')

        else:
            self.fail_check('following objects have multiple materiasl, '
                            'please just keep one: {}'.format(material_check))

        lm.selection(clear=True)



        # self.fail_check('Check Failed')
