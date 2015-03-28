# broctl-setcap
Broctl plugin for automatically executing 'setcap' on each node after an install

## On the Bro Manager
1. Drop the setcap.py plugin into /opt/bro/lib/broctl/plugins/
2. Add the following lines to broctl.cfg (adjust accordingly for your installation)
```
setcap.enabled=1
setcap.command=sudo /sbin/setcap cap_net_raw,cap_net_admin=eip /opt/bro/bin/bro && sudo /sbin/setcap cap_net_raw,cap_net_admin=eip /opt/bro/bin/capstats
```
## On each Node
Edit the sudoers file (use `visudo`) and add the following line to allow sudo execution (w/o password) of setcap (if you're running Bro as a different user adjust as necessary as well):

`bro	ALL=NOPASSWD: /sbin/setcap`

## Test it Out
    [BroControl] > install
    removing old policies in /data/bro/spool/installed-scripts-do-not-touch/site ... done.
    removing old policies in /data/bro/spool/installed-scripts-do-not-touch/auto ... done.
    creating policy directories ... done.
    installing site policies ... done.
    generating cluster-layout.bro ... done.
    generating local-networks.bro ... done.
    generating broctl-config.bro ... done.
    updating nodes ... done.
    setcap plugin: executing setcap on each node:
    10.1.2.141 - Executing setcap: SUCCESS
    10.1.2.142 - Executing setcap: SUCCESS
    10.1.2.143 - Executing setcap: SUCCESS
    
