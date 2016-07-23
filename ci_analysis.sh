#! /bin/sh

PATH=${WORKSPACE}/venv/bin:$PATH

PYLINT=coverage

if [ ! -d "venv" ]; then
	virtualenv venv
fi
chmod +x ./venv/bin/activate

./venv/bin/activate
pip install --trusted-host scmesos06 -i http://scmesos06:3141/simple -r requirements_dev.txt --cache-dir=/tmp/${JOB_NAME}

${PYLINT} -f parseable -d meerkat | tee pylint.out