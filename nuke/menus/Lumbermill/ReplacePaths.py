import cgl.ui.widgets.path_fixer as path_fixer
import nuke

def run():
    reload(path_fixer)
    write_nodes = nuke.allNodes('Write')
    read_nodes = nuke.allNodes('Read')
    all_nodes = write_nodes + read_nodes
    dialog = path_fixer.PathFixer(nodes=all_nodes)
    dialog.exec_()
