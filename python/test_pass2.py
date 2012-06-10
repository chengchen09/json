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
        cj.load(JSON, 's')

        # json format
        f = open(jfile, 'w')
        cj.dump(f, 'j')
        f.close()
        jres = CCJson()
        f = open(jfile, 'r')
        jres.load(f, 'j')
        f.close()
        self.assertEquals(cj._dd, jres._dd)
        
        # python format
        f = open(pfile, 'w')
        cj.dump(f, 'p')
        f.close()
        pres = CCJson()
        f = open(pfile, 'r')
        pres.load(f, 'p')
        f.close()
        self.assertEquals(cj._dd, pres._dd)
