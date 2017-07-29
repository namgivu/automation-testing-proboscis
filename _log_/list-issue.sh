#!/usr/bin/env bash

##region common bash util

  #get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
  s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ;
  SCRIPT_HOME=$s

##endregion common bash util


#search file that contain fail or error ref. https://superuser.com/a/614589/34893
# param i for case insensitive
# param E for regex
# param H for filename output
# param R for recursive search
# param m for matched count
grep -iEHR 'fail|error' --color=always  --include '*.log' -m 1 $SCRIPT_HOME
