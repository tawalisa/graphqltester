from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import yaml
import sys

testresult = {}
testresult['total'] = 0
testresult['success'] = 0
testresult['fail'] = 0

def test(testfile, client):
    print("start test file:", testfile)
    testcases = yaml.load(open(testfile), Loader=yaml.FullLoader)
    for case in testcases['cases']:
        print(case['case'])
        t = case['case']
        _testcase(case['case'], client)


def assertResult(result, assertion):
    if 'errors' in result:
        print("----------------------------------", result['errors'], file=sys.stderr)
        testresult['fail'] += 1
        testresult['total'] += 1
    else:
        print("++++++++++++++++++++++++++++++++++", result)
        testresult['total'] += 1
        testresult['success'] += 1
    pass


def _testcase(testcase, client):
    if testcase:
        print("start test case:",testcase['name'])
        query = gql(testcase['query'])
        try:
            result = client.execute(query)
            assertResult(result, testcase['assertion'])
        except Exception as err:
            print("----------------------------------", err, file=sys.stderr)
            testresult['fail'] += 1
            testresult['total'] += 1
def printSummary():
    print('total :', testresult['total'], flush=True)
    print('success:', testresult['success'], flush=True)
    print('failed:', testresult['fail'], file=sys.stderr, flush=True)



docs = yaml.load_all(open('setting.yaml'), Loader=yaml.FullLoader)
filter = "*";
if len(sys.argv)>1:
    filter = sys.argv[1]

print("filter:", filter)
setting = {}
for doc in docs:
    print(doc.items())
    for k, v in doc.items():
        setting[k] = v

_transport = RequestsHTTPTransport(
    url=setting['url'],
    use_json=True,
)

client = Client(
    transport=_transport,
    fetch_schema_from_transport=False,
)
for testcase in setting['testcases']:
    if filter == "*" or testcase["label"] == filter:
        test(testcase['file'], client)
printSummary()
