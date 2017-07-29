#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

##endregion common bash util


##region load param $1 as config file

  #load param
  CONFIG_FILE=$1
  if [ -z $CONFIG_FILE ]; then
    echo 'Param $1 as CONFIG_FILE is required'
  fi

  #load config file
  CONFIG_LOCAL="$SCRIPT_HOME/config_local.py"
  cp -f $CONFIG_FILE $CONFIG_LOCAL
  echo "
Config file loaded
  from $CONFIG_FILE
  to   $CONFIG_LOCAL
"

  #aftermath check
  echo "
Aftermath check
$(cat $CONFIG_LOCAL | grep HOME_PAGE_URL)
"

##endregion load param $1 as config file
