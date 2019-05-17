# setcap plugin for Zeekctl
#
# This plugin will execute 'setcap' on each node after an install
#
# Options:
#    The plugin is off by default. To enable it, add "setcap.enabled=1" to zeekctl.cfg.
#
# Orig: Dave Crawford (@pingtrip)
# Updated: John Bradley (@userjack6880)

import ZeekControl.plugin

class setcap(ZeekControl.plugin.Plugin):
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
        ("command", "string", "", "Full command to execute on each node.")]

    def cmd_install_post(self):
        self.message("setcap plugin: executing setcap on each node:")
        uniq_nodes = {}
                                                                                                                                                 
        for n in self.nodes():
            if n.type == 'standalone' or n.type == 'worker':
                uniq_nodes[n.host] = n
                                     
        cmds = [(n, self.getOption('command')) for n in uniq_nodes.values()]

        for (n, success, output) in self.executeParallel(cmds):
            self.message("{0} - Executing setcap: {1}".format(n.host, 'SUCCESS' if success else 'FAIL: ' + output[0]))
