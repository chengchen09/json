from unittest import TestCase
from ccjson import CCJson

# from http://json.org/JSON_checker/test/pass2.json
JSON = r'''
[[[[[[[[[[[[[[[[[[["Not too deep"]]]]]]]]]]]]]]]]]]]
'''

jfile = './test_pass2.json'

class TestPass2(TestCase):
    def runTest(self):
        cj = CCJson()
        cj.load(JSON, 's')
        f = open(jfile, 'w')
        cj.dump(f, 'j')
        f.close()
        res = CCJson()
        f = open(jfile, 'r')
        res.load(f, 'j')
        f.close()
        self.assertEquals(cj._dd, res._dd)
        print 'passed'
    
