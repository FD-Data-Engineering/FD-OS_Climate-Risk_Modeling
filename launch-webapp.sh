#!/usr/bin/env bash
#
# python3 is required as main python
#
PATTERN_X="^(MINGW64_NT-10.0-19044$|MINGW64_NT-10.*-*$|Unix*$)"
if [[ $(uname) =~ $PATTERN_X ]]; then
    export PYTHON_BUILD_COMMAND=python
else
    export PYTHON_BUILD_COMMAND=python.exe
fi
# idenpotent local build egg and launch webapp server
rm -rf Modeling/python-library/webapp/output/osf_model_app-0.0.1-py3.11.egg
cd Modeling/python-library/webapp/
$PYTHON_BUILD_COMMAND create_webapp.py
cd ..
export MODEL_NAME=""
export RUNMODE="2"
$PYTHON_BUILD_COMMAND launch_model_webapp.py
#