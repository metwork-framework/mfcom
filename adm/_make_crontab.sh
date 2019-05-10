#!/bin/bash

set -eu

if ! test -s "${MODULE_HOME}/config/crontab"; then
    exit 0
fi

RUNTIME_SUFFIX=""
if test "${MODULE_RUNTIME_SUFFIX:-}" != ""; then
    RUNTIME_SUFFIX="export MODULE_RUNTIME_SUFFIX=${MODULE_RUNTIME_SUFFIX} ; "
fi
export RUNTIME_SUFFIX

cat "${MODULE_HOME}/config/crontab" |envtpl

if test -d "${MODULE_RUNTIME_HOME}/var/plugins"; then
    for TMP in $(plugins.list --raw); do
        BDIR=$(echo "${TMP}" |awk -F '~~~' '{print $4;}')
        NAME=$(echo "${TMP}" |awk -F '~~~' '{print $1;}')
        if test -s "${BDIR}/crontab"; then
            echo "##### BEGINNING OF METWORK ${MODULE} PLUGIN ${NAME} CRONTAB #####"
            cat "${BDIR}/crontab" | envtpl
            echo "##### END OF METWORK ${MODULE} PLUGIN ${NAME} CRONTAB #####"
        fi
    done
fi
