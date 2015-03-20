#!/bin/sh
/sbin/setcap cap_net_raw,cap_net_admin=eip /opt/bro/bin/bro
/sbin/setcap cap_net_raw,cap_net_admin=eip /opt/bro/bin/capstats
