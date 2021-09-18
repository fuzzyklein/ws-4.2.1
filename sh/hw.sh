#! /usr/bin/env bash

virtual=0
venv=.venv
installed_just_now=1

accept=d
__debug__=1

function venv() {
  printf "Virtual environment $venv does not exist.\n"
  printf "Do you want to create it? (y/n): "
  read answer;
  case $answer in
    y)
      printf "OK, let's do that then.\n"
      python3.9 -m venv --upgrade-deps $venv
      virtual=0
      installed_just_now=0
  esac
}

if [ ! -d ${venv} ]; then
   virtual=1; venv a
fi
[[ $virtual ]] && source $venv/bin/activate
[[ $installed_just_now -eq 0 ]] && pip install -r requirements.txt


if [[ " $@ " =~ " -d " ]]; then
  python hw $@
else
  python -O hw $@
fi

[[ $virtual ]] && deactivate
