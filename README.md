# The graphqlTester is a light tool which can run some integration test for develop.

# The graphqlTester supports 2 ways to run. Docker and localrun.

## Docker

### build images

run `build.bat` as cmd

### edit graphql server url.

edit correct url in `src/setting.yaml`

### need test case if needed.

edit `src/testcases.yaml` or add your testcases.yaml to `src/setting.yaml`

### run test 

run 'run.bat' as cmd

## local run

### you need to install python3 and install package via pip

run 'pip install gql pyyaml' as cmd

### run test

goto `src` folder and run `python app.py` as cmd