#!/usr/bin/env python

# inspired from
# https://github.com/monitoring-tools/telegraf-plugins/tree/master/netstat

import os
import time
import json
from telegraf_unixsocket_client import TelegrafUnixSocketClient
from mflog import getLogger
from mfutil import BashWrapper

MODULE_RUNTIME_HOME = os.environ["MODULE_RUNTIME_HOME"]
SOCKET_PATH = os.path.join(MODULE_RUNTIME_HOME, "var", "telegraf.socket")
LOGGER = getLogger("telegraf_collector_metwork_module")
MODULE = os.environ['MODULE']
CMD = "list_metwork_processes.py --output-format=json --include-current-family"


def get_stats():
    stats = {}
    results = BashWrapper(CMD)
    if not results:
        LOGGER.warning("can't execute %s: %s" % (CMD, results))
        return None
    try:
        processes = json.loads(results.stdout)
    except Exception:
        LOGGER.warning("can't parse %s output as JSON" % CMD)
        return None
    plugins = set([x['plugin'] if x['plugin'] != '' else '#core#'
                   for x in processes])
    for plugin in plugins:
        if plugin not in stats:
            stats[plugin] = {}
        for key in ('mem_percent', 'num_threads', 'cpu_percent', 'num_fds'):
            search_plugin = plugin if plugin != '#core#' else ''
            stats[plugin][key] = sum([x[key] for x in processes
                                      if x['plugin'] == search_plugin])
    return stats


while True:
    LOGGER.debug("waiting 10s...")
    time.sleep(10)
    client = TelegrafUnixSocketClient(SOCKET_PATH)
    try:
        client.connect()
    except Exception:
        LOGGER.warning("can't connect to %s, wait 10s and try again...",
                       SOCKET_PATH)
        continue
    stats = get_stats()
    if stats:
        for plugin, fields_dict in stats.items():
            msg = client.send_measurement("metwork_module", fields_dict,
                                          extra_tags={"plugin": plugin})
            LOGGER.debug("sended msg: %s" % msg)
    client.close()
