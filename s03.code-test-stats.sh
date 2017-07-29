#!/usr/bin/env bash

#what is this step for ref. https://trello.com/c/P1N21wBN
#TODO consider to use github API to speed up ref. https://stackoverflow.com/questions/45253392/git-ls-remote-command-parameter-to-limit-the-number-of-returned-rows#comment77487854_45253392

#coloring
CM='\033[0;32m' #comment color
EC='\033[0m'    #end coloring

#print code vs test stats
CODE_GITHUB_URL='git@github.com:YOUR_GIT_USER/YOUR_GIT_REPO.git'
DEV_BRANCH='YOUR_DEV_BRANCH'
TEST_BRANCH='YOUR_TEST_BRANCH'

getLastLine='tail -n 1'  #ref. https://unix.stackexchange.com/a/139099/17671
getLast4Char='tail -c 5' #ref. https://stackoverflow.com/a/9220013/248616

#get latest tag @ branch master ref. https://stackoverflow.com/a/12704727/248616
master=`git ls-remote --tags ${CODE_GITHUB_URL} | sort -t '/' -k 3 -V | ${getLastLine} | cut -f 2`

#get latest commit @ branch dev-master ref. https://stackoverflow.com/a/15679887/248616
dev=`git ls-remote --heads ${CODE_GITHUB_URL} | grep refs/heads/${DEV_BRANCH} | cut -f 1 | ${getLast4Char}`

#get latest commit @ branch test-auto ref. https://stackoverflow.com/a/15679887/248616
testauto=`git ls-remote --heads ${CODE_GITHUB_URL} | grep refs/heads/${TEST_BRANCH} | cut -f 1 | ${getLast4Char}`

#combine the outcome
GIT_CODE_STATS="master=${CM}$master${EC} dev=${CM}$dev${EC} test-auto=${CM}$testauto${EC}"
echo -e $GIT_CODE_STATS
