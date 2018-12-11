#!/usr/bin/env python3

import os
import psutil
import sys
import argparse
import time
import json

from mflog import getLogger

LOG = getLogger('list_metwork_processes')
USER = os.environ.get('MODULE_RUNTIME_USER', None)
MODULE = os.environ.get('MODULE', None)
MODULE_RUNTIME_HOME = os.environ.get('MODULE_RUNTIME_HOME', None)
MODULE_RUNTIME_HOME_TMP = MODULE_RUNTIME_HOME + "/tmp" if MODULE_RUNTIME_HOME \
    is not None else None
if USER is None:
    LOG.critical("can't read MODULE_RUNTIME_USER env var")
    sys.exit(1)
if MODULE is None:
    LOG.critical("can't read MODULE env var")
    sys.exit(1)
CURRENT_PROCESS = psutil.Process()
CURRENT_PLUGIN_ENV_VAR = "%s_CURRENT_PLUGIN_NAME" % MODULE


def is_same_family(child, proc):
    if child.pid == proc.pid:
        return True
    try:
        parent = child.parent()
    except Exception:
        return False
    if parent is None:
        return False
    return is_same_family(parent, proc)


def get_processes(exclude_same_family=CURRENT_PROCESS, exclude_terminal=True,
                  include_cwd_startswith=MODULE_RUNTIME_HOME_TMP,
                  include_children=True):
    def add_process_and_children(processes, proc):
        processes.add(proc)
        try:
            children = proc.children(recursive=True)
        except Exception:
            return
        for child in children:
            child.metwork_plugin_name = proc.metwork_plugin_name
            processes.add(child)
        return
    processes = set()
    for proc in psutil.process_iter():
        if proc.username() != USER:
            continue
        if exclude_same_family is not None:
            if is_same_family(exclude_same_family, proc):
                continue
        cwd = ""
        try:
            cwd = proc.cwd()
        except Exception:
            pass
        try:
            env = proc.environ()
        except psutil.Error:
            continue
        if CURRENT_PLUGIN_ENV_VAR in env:
            proc.metwork_plugin_name = env[CURRENT_PLUGIN_ENV_VAR]
        else:
            proc.metwork_plugin_name = ""
        if env.get('METWORK_LIST_PROCESSES_FORCE', None) == '1':
            add_process_and_children(processes, proc)
            continue
        if env.get('METWORK_LIST_PROCESSES_FORCE', None) == '0':
            continue
        if exclude_terminal:
            if proc.terminal() is not None:
                continue
        if include_cwd_startswith is not None:
            if cwd.startswith(include_cwd_startswith):
                add_process_and_children(processes, proc)
                continue
        if 'MODULE' not in env:
            continue
        if env['MODULE'] != MODULE:
            continue
        add_process_and_children(processes, proc)
    return processes


argparser = argparse.ArgumentParser(description="list metwork processes")
argparser.add_argument("--pids-only", action="store_true",
                       help="show only pids")
argparser.add_argument("--include-current-family", action="store_true",
                       help="include current process family")
argparser.add_argument("--output-format", default="text",
                       help="output format (text (default) or json")
args = argparser.parse_args()
if args.output_format not in ("text", "json"):
    print("ERROR: bad output format")
    sys.exit(1)

if args.include_current_family:
    processes = get_processes(exclude_same_family=None)
else:
    processes = get_processes()

if args.pids_only:
    if args.output_format == 'json':
        print(json.dumps([x.pid for x in processes], indent=4))
        sys.exit(0)
    else:
        for proc in processes:
            print(proc.pid)
        sys.exit(0)

for proc in processes:
    try:
        # see https://psutil.readthedocs.io/en/latest/
        # #psutil.Process.cpu_percent
        proc.cpu_percent()
    except Exception:
        pass
time.sleep(1)

processes_count = 0
json_list = []
for proc in processes:
    try:
        name = proc.name()
        pid = proc.pid
        cmdline = " ".join(proc.cmdline()).strip()
        num_fds = proc.num_fds()
        num_threads = proc.num_threads()
        cpu_percent = proc.cpu_percent()
        mem_percent = proc.memory_percent(memtype="pss")
        plugin = proc.metwork_plugin_name
    except Exception:
        continue
    if args.output_format == 'json':
        json_list.append({
            "cmdline": cmdline,
            "num_fds": num_fds,
            "num_threads": num_threads,
            "cpu_percent": cpu_percent,
            "mem_percent": mem_percent,
            "plugin": plugin
        })
        continue
    print("- Process %s (pid=%i):" % (name, pid))
    print("    - cmdline          : %s" % cmdline)
    print("    - num fdsi         : %i" % num_fds)
    print("    - num threads      : %i" % num_threads)
    print("    - cpu_percent      : %f" % cpu_percent)
    print("    - mem_percent (pss): %f" % mem_percent)
    print("    - plugin           : %s" % plugin)
    processes_count = processes_count + 1

if args.output_format == 'json':
    print(json.dumps(json_list, indent=4))
else:
    print()
    print("Total: %i processes" % processes_count)

sys.exit(0)
