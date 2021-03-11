#!/bin/bash

. init/logbot/logbot.sh
. init/utils.sh
. init/checks.sh

trap handleSigTerm TERM
trap handleSigInt INT

initxdecha() {
    printLogo
    assertPrerequisites
    sendMessage "Initializing xdecha ..."
    assertEnvironment
    editLastMessage "Starting xdecha ..."
    printLine
}

startxdecha() {
    startLogBotPolling
    runPythonModule xdecha "$@"
}

stopxdecha() {
    sendMessage "Exiting xdecha ..."
    endLogBotPolling
    exit 0
}

handleSigTerm() {
    log "Exiting With SIGTERM (143) ..."
    stopxdecha
    exit 143
}

handleSigInt() {
    log "Exiting With SIGINT (130) ..."
    stopxdecha
    exit 130
}

runxdecha() {
    initxdecha
    startxdecha "$@"
    stopxdecha
}
