from cgl.plugins.nuke import alchemy as alc

def run():
    print("hello world: Pre Publish")
    alc.launch_preflight()
