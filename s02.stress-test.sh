#!/usr/bin/env bash

#get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
SCRIPT_HOME=$s

#coloring
HL='\033[1;33m' #high-lighted color
CM='\033[0;32m' #comment color
EC='\033[0m'    #end coloring


#region load input
  LOOP_TIME=3
  #loop time set via param $1 if any
  if [ ! -z "$1" ]; then
    LOOP_TIME=$1
  fi

  ASYNC_RUN=0 #0/1 means NOT-async/async
  #async run flag set via param $2 if any
  if [ ! -z "$2" ]; then
    ASYNC_RUN=$2
  fi

  ASYNC_SLEEP_TIME=0.5 #0/1 means NOT-async/async
  #sleep time between async runs via param $3 if any
  if [ ! -z "$3" ]; then
    ASYNC_SLEEP_TIME=$3
  fi
#endregion load input


if [ "$ASYNC_RUN" == '0' ]; then
  runAsAsync=''
else
  runAsAsync='&'
fi

sh="$SCRIPT_HOME/s01.run-test.sh $runAsAsync"


for ((i=1; i<=$LOOP_TIME; i++)); #loop n times ref. https://stackoverflow.com/a/3737771/248616
do
  #run test
  echo -e "Run ${HL}$i/$LOOP_TIME${EC}"
  eval $sh

  #take a rest; critical when run in async mode i.e. to separate log file
  sleep $ASYNC_SLEEP_TIME #sleep in millisecond ref. https://serverfault.com/a/469249/41015
done

wait #wait for all async runs, if any, to complete ref. https://ubuntuforums.org/showthread.php?t=1579261&p=9873068#post9873068
