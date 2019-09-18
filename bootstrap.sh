#!/bin/bash

set -eu

function get_abs_filename() {
    echo "$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
}

function usage() {
    echo "usage: ./bootstrap.sh INSTALL_PREFIX_DIRECTORY MFEXT_INSTALL_ROOT_DIRECTORY"
}
if test "${1:-}" = "" -o "${2:-}" = ""; then
    usage
    exit 1
fi
MFEXT_HOME=$(get_abs_filename "$2")
export MFEXT_HOME
if ! test -d "${MFEXT_HOME}"; then
    usage
    echo "ERROR: ${MFEXT_HOME} is not a directory"
    exit 1
fi
MFCOM_HOME=$(get_abs_filename "$1")
export MFCOM_HOME
MFCOM_VERSION=$("${MFEXT_HOME}/bin/guess_version.sh")
export MFCOM_VERSION
MFEXT_VERSION=$(cat "${MFEXT_HOME}/config/version")
export MFEXT_VERSION
export MFMODULE_VERSION=${MFCOM_VERSION}


if test "${1:-}" = "--help"; then
    usage
    exit 1
fi

PREFIX=$(get_abs_filename "$1")
export PREFIX
if ! test -d "${PREFIX}"; then
    usage
    echo "ERROR: ${PREFIX} is not a directory"
    exit 1
fi
MFEXT_HOME=$(get_abs_filename "${MFEXT_HOME}")
export MFEXT_HOME

    if ! test -f "${MFEXT_HOME}/bin/guess_version.sh"; then
        echo "ERROR: configured mfext home (${MFEXT_HOME}) is not a mfext home"
        exit 1
    fi



MFMODULE_HOME=$(get_abs_filename "${PREFIX}")
export MFMODULE_HOME
export MFMODULE=MFCOM
export MFMODULE_LOWERCASE=mfcom
SRC_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export SRC_DIR




rm -f adm/root.mk
touch adm/root.mk


ROOT_PATH=${MFCOM_HOME}/bin:${MFEXT_HOME}/bin:${MFEXT_HOME}/opt/core/bin:/usr/sbin:/usr/bin:/sbin:/bin
ROOT_LD_LIBRARY_PATH=""
ROOT_PKG_CONFIG_PATH=""
ROOT_LAYERAPI2_LAYERS_PATH=${MFCOM_HOME}/opt:${MFCOM_HOME}:${MFEXT_HOME}/opt:${MFEXT_HOME}


echo "Making adm/root.mk..."
rm -f adm/root.mk
touch adm/root.mk

echo "export MFMODULE := ${MFMODULE}" >>adm/root.mk
echo "export MFMODULE_LOWERCASE := $(echo ${MFMODULE} | tr '[:upper:]' '[:lower:]')" >>adm/root.mk
echo "export LAYERAPI2_LAYERS_PATH := ${ROOT_LAYERAPI2_LAYERS_PATH}" >>adm/root.mk
echo "export MFEXT_HOME := ${MFEXT_HOME}" >>adm/root.mk
echo "export MFEXT_VERSION := ${MFEXT_VERSION}" >>adm/root.mk
echo "export MFMODULE_HOME := ${MFMODULE_HOME}" >>adm/root.mk
echo "export MFMODULE_VERSION := ${MFCOM_VERSION}" >>adm/root.mk
echo "export SRC_DIR := ${SRC_DIR}" >>adm/root.mk
echo "ifeq (\$(FORCED_PATHS),)" >>adm/root.mk
echo "  export PATH := ${ROOT_PATH}" >>adm/root.mk
echo "  export LD_LIBRARY_PATH := ${ROOT_LD_LIBRARY_PATH}" >>adm/root.mk
echo "  export PKG_CONFIG_PATH := ${ROOT_PKG_CONFIG_PATH}" >>adm/root.mk
echo "  LAYER_ENVS:=\$(shell env |grep '^LAYERAPI2_LAYER_.*_LOADED=1\$\$' |awk -F '=' '{print \$\$1;}')" >>adm/root.mk
echo "  \$(foreach LAYER_ENV, \$(LAYER_ENVS), \$(eval unexport \$(LAYER_ENV)))" >>adm/root.mk
echo "endif" >>adm/root.mk

        echo "export MFCOM_HOME := ${MFCOM_HOME}" >>adm/root.mk
        echo "export MFCOM_VERSION := ${MFCOM_VERSION}" >>adm/root.mk

    if test "${MODULE_HAS_HOME_DIR:-}" = "1"; then
    echo "export MODULE_HAS_HOME_DIR := 1" >>adm/root.mk
    fi
    #echo "export PREFIX := ${MFMODULE_HOME}" >>adm/root.mk


# FIXME: do not hardcode this
# FIXME: move to layer root extra_env ?
echo "export PYTHON2_SHORT_VERSION := 2.7" >>adm/root.mk
echo "export PYTHON3_SHORT_VERSION := 3.7" >>adm/root.mk

echo "BOOTSTRAP DONE !"
echo "MFEXT_HOME=${MFEXT_HOME}"

    echo "MFCOM_HOME=${MFCOM_HOME}"
