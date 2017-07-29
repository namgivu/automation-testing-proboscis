#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

  #coloring
  CM='\033[0;32m' #comment color
  EC='\033[0m'    #end coloring

##endregion common bash util


#prepare log
LOG_HOME="$SCRIPT_HOME/_log_"
timestamp=$(date +%Y%m%d-%H%M%S-%3N) #timestamp in bash ref. https://stackoverflow.com/a/43114970/248616
FILENAME="$timestamp"
LOG_RAW_FILE="$LOG_HOME/$FILENAME.log"
LOG_HTML_FILE="$LOG_HOME/$FILENAME.html"
consoleOutput2File="2>&1 | tee -a $LOG_RAW_FILE" #write console output to file ref. https://stackoverflow.com/a/418899/248616

#print log file name
echo -e "
log=${CM}$LOG_RAW_FILE${EC}
    ${CM}$LOG_HTML_FILE${EC}
"

#print code vs test stats - can be TURNED OFF to speed up a test run
#eval "${SCRIPT_HOME}/s03.code-test-stats.sh ${consoleOutput2File}"


#proboscis param
optWITH_YANC='--with-yanc' #make colorful test log ref. https://pypi.python.org/pypi/yanc/
optNOCAPTURE='--nocapture' #allow to see print() output ref. https://stackoverflow.com/a/5975555/248616


#run test
eval "python ${SCRIPT_HOME}/run_test.py  $@  ${optWITH_YANC} ${optNOCAPTURE}  ${consoleOutput2File}" #$@ to bypass params to inner command ref. https://stackoverflow.com/a/4824637/248616

#convert log file to html file ref. https://askubuntu.com/a/502456/22308
cat $LOG_RAW_FILE | aha --black --title 'autotest log' > $LOG_HTML_FILE
