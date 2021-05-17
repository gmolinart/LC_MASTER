import nuke


#print nuke.selectedNode().knob('colorspace').getValue()

aces_config = "ACES - ACEScct"


def convertRoot():

    nuke.Root().knob('colorManagement').setValue('OCIO')
    nuke.Root().knob('OCIO_config').setValue('aces_1.0.3')


def convertReads():
    ReadNodes = nuke.allNodes('Read')

    for r in ReadNodes:
        print r.name()

        if r.knob('colorspace').getValue() == 6.0:
            r.knob('colorspace').setValue("Utility - Curve - sRGB")
        else:

            r.knob('colorspace').setValue(aces_config)
            r.knob('raw').setValue(True)


def convertOCIOS():
    OCIONodes = nuke.allNodes('OCIOCDLTransform')

    for n in OCIONodes:
        n.knob("working_space").setValue(1)


def convertWrites():

    WriteNodes = nuke.allNodes('Write')
    for w in WriteNodes:
        print w.name()
        w.knob('colorspace').setValue(aces_config)
        w.knob('raw').setValue(True)


def run():
    convertRoot()
    convertReads()
    convertWrites()
    convertOCIOS()

