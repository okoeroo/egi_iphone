#!/bin/sh

JSON="data.json"
ENTERHOST="login2.nikhef.nl"
#ENTERHOST="login.nikhef.nl"
PUBLISH_DIR="/www/tmpfiles/egi2010/"
BACKUPDIR="${PUBLISH_DIR}/backup"


function backupfailed() {
    echo "Backup failed on remote service"
    exit 1
}
function publishingfailed() {
    echo "Publishing the ${JSON} file at ${ENTERHOST}:${PUBLISH_DIR}/${JSON} failed"
    exit 1
}


python indico_xml_to_hope_json.py || exit 1

ssh ${ENTERHOST} cp ${PUBLISH_DIR}/${JSON} ${BACKUPDIR}/data.json.`date +%Y%m%d%H%M` || backupfailed

scp ${JSON} ${ENTERHOST}:${PUBLISH_DIR}/${JSON} || publishingfailed
