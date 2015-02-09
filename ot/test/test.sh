#! /bin/bash
cd ..
nosetests "$@" --with-coverage --cover-package=ot --cover-erase --cover-branches --cover-html
