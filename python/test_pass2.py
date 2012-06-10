from unittest import TestCase
from ccjson import CCJson

# from http://json.org/JSON_checker/test/pass2.json
JSON = r'''
[[[[[[[[[[[[[[[[[[["Not too deep"]]]]]]]]]]]]]]]]]]]
'''

jfile = './test_pass2.json'
pfile = './test_pass2.python'

class TestPass2(TestCase):
    def runTest(self):
        cj = CCJson()
        cj.loads(JSON)

        # json format
        f = open(jfile, 'w')
        cj.dump(f)
        f.close()
        jres = CCJson()
        f = open(jfile, 'r')
        jres.load(f)
        f.close()
        self.assertEquals(cj._dd, jres._dd)
        
        # python format
        f = open(pfile, 'w')
        cj.dump_python(f)
        f.close()
        pres = CCJson()
        f = open(pfile, 'r')
        pres.load_python(f)
        f.close()
        self.assertEquals(cj._dd, pres._dd)
