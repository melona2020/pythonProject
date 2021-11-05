def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


#!/bin/bash
echo '#### Create python3 Virtual enviroment ####'
source scl_souce enable rh-python36

VIRTUAL_ENV_NAME='virtual-enviroment'
python -m venv $VIRTUAL_ENV_NAME

echo '#### Activate Virtual Enviroment ####'
source $VIRTUAL_ENV_NAME/bin/activate

echo '#### Install reqirements ####'
pip install -r ./requirements.txt

#Jump to that path
cd /var/lib/jenkins/workspace/$JOB_NAME/

echo '#### Run Tests ####'
pytest mytest --junitxmals./xmlReport/output.xml

echo '#### deactivate virtual enviroment and exit scl ####'
deactivate
exit