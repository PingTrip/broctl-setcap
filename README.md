# zeekctl-setcap
Zeekctl plugin for automatically executing 'setcap' on each node after an install

## On the Zeek Manager
1. Drop the setcap.py plugin into /opt/bro/lib/zeekctl/plugins/
2. Add the following lines to zeekctl.cfg (adjust accordingly for your installation)
```
setcap.enabled=1
setcap.command=sudo /sbin/setcap cap_net_raw,cap_net_admin=eip /opt/bro/bin/zeek && sudo /sbin/setcap cap_net_raw,cap_net_admin=eip /opt/bro/bin/capstats
```
## On each Node
Edit the sudoers file (use `visudo`) and add the following lines to allow sudo execution (w/o password or tty) of setcap. If you're running Zeek as a different user, or from a different directory, adjust as necessary:

```
Cmnd_Alias ZEEK_SETCAP = /sbin/setcap cap_net_raw\,cap_net_admin=eip /opt/bro/bin/zeek
Cmnd_Alias CAPSTATS_SETCAP = /sbin/setcap cap_net_raw\,cap_net_admin=eip /opt/bro/bin/capstats
zeek ALL=NOPASSWD: ZEEK_SETCAP, CAPSTATS_SETCAP
Defaults!/sbin/setcap !requiretty
```

## Test it Out
    [ZeekControl] > install
    removing old policies in /data/bro/spool/installed-scripts-do-not-touch/site ... done.
    removing old policies in /data/bro/spool/installed-scripts-do-not-touch/auto ... done.
    creating policy directories ... done.
    installing site policies ... done.
    generating cluster-layout.zeek ... done.
    generating local-networks.zeek ... done.
    generating zeekctl-config.zeek ... done.
    updating nodes ... done.
    setcap plugin: executing setcap on each node:
    10.1.2.141 - Executing setcap: SUCCESS
    10.1.2.142 - Executing setcap: SUCCESS
    10.1.2.143 - Executing setcap: SUCCESS
    
