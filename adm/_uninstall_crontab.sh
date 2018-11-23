#!/bin/bash

echo -n "- Uninstalling module crontab..."
echo_running

RES=0

if hash crontab 2>/dev/null; then

    START_LINE="##### BEGINNING OF METWORK ${MODULE} MODULE CRONTAB #####"
    STOP_LINE="##### END OF METWORK ${MODULE} MODULE CRONTAB #####"

    undeploycron_between "${START_LINE}" "${STOP_LINE}" >"${MODULE_RUNTIME_HOME}/tmp/undeploycron_errors.$$" 2>&1
    if test $? -eq 0; then

        N=$(crontab -l 2>/dev/null |grep "${START_LINE}" |wc -l)
        if test ${N} -gt 0; then
            echo_nok || RES=1
        else
            echo_ok
        fi

        PLUGINS=$(crontab -l |grep "##### BEGINNING OF METWORK ${MODULE} PLUGIN" |awk '{print $7;}')
        for PLUGIN in ${PLUGINS}; do
            echo -n "- Uninstalling plugin ${PLUGIN} crontab..."
            echo_running
            START_LINE="##### BEGINNING OF METWORK ${MODULE} PLUGIN ${PLUGIN} CRONTAB #####"
            STOP_LINE="##### END OF METWORK ${MODULE} PLUGIN ${PLUGIN} CRONTAB #####"
            undeploycron_between "${START_LINE}" "${STOP_LINE}" >>"${MODULE_RUNTIME_HOME}/tmp/undeploycron_errors.$$" 2>&1
            if test $? -eq 0; then
                N=$(crontab -l 2>/dev/null |grep "${START_LINE}" |wc -l)
                if test ${N} -gt 0; then
                    echo_nok || RES=1
                else
                    echo_ok
                fi
            else
                echo_nok "(can't uninstall plugin ${PLUGIN} crontab)" || RES=1
                echo_bold "ERROR: see ${MODULE_RUNTIME_HOME}/tmp/undeploycron_errors.$$ for details"
            fi
        done
    else
        echo_nok "(can't uninstall module crontab)" || RES=1
        echo_bold "ERROR: see ${MODULE_RUNTIME_HOME}/tmp/undeploycron_errors.$$ for details"
    fi
else
    echo_warning "(no crontab installed)"
fi

if test ${RES} -eq 0; then
    rm -f "${MODULE_RUNTIME_HOME}/tmp/undeploycron_errors.$$"
fi

exit ${RES}
