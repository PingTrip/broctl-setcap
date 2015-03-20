# setcap plugin for Broctl
#
# This plugin will execute 'setcap' on each node after an install
#
# Options:
#    The plugin is off by default. To enable it, add "setcap.enabled=1" to broctl.cfg.
#    Set the full path of the 'bro_setcap.sh' script modify "setcap.script_path' in broctl.cfg
#
# Dave Crawford (@pingtrip)

import BroControl.plugin

class setcap(BroControl.plugin.Plugin):
    def __init__(self):
        super(setcap, self).__init__(apiversion=1)

    def name(self):
        return "setcap"

    def prefix(self):
        return "setcap"

    def pluginVersion(self):
        return 1

    def init(self):
        if self.getOption("enabled") == "0":
            return False

        return True

    def options(self):
        return [("enabled", "string", "0", "Set to enable plugin"),
        ("script_path", "string", "/opt/bro/bin/bro_setcap.sh", "Full path to the bro_setcap.sh script")]

    def cmd_install_post(self):
        self.message("setcap plugin: executing setcap on each node:")
        uniq_nodes = {}

        for n in self.nodes():
            if n.type == 'standalone' or n.type == 'worker':
                uniq_nodes[n.host] = n
        
        cmd = "sudo {0}".format(self.getOption('script_path'))
        cmds = [(n, cmd) for n in uniq_nodes.values()]

        for (n, success, output) in self.executeParallel(cmds):
            self.message("{0} - Executing setcap: {1}".format(n.host, 'SUCCESS' if success else 'FAIL'))
