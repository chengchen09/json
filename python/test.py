#!/usr/bin/env python

'''
Author: Chen Cheng
Description: a collection of test for the class CCJson
'''
from ccjson import CCJson
from test_pass1 import TestPass1 
from test_pass2 import TestPass2 

def get_json():
    cj1 = CCJson()
    cj1[0] = ['1', '2']
    # only json object
    cj2 = CCJson()
    cj2['a'] = 'abnormal'
    cj2['b'] = 'black'
    # array + object
    cj3 = CCJson()
    cj3[0] = [1.1, False, True, 1.4e-10]
    cj3[1] = ['a', 'b', 'c']
    cj3['a'] = 'abnormal'
    cj3['b'] = 'black'
    cj3['c'] = None
    # nested
    cj4 = CCJson()
    cj4._dd = cj3._dd
    cj4._dd[0].append(cj2._dd)
    cj4._dd['d'] = [1, 2]

    return cj4

def test_get_set_del():
    cj = CCJson()
    cj['haha'] = '1'
    print cj['haha']
    print cj['null']
    del cj['haha']
    print cj['haha']
    del cj['null']

def test_update():
    cj = CCJson()
    cj['name'] = 'chen'
    cj.jprint()
    d = {'a': 21, 'name': 'CHEN'}
    cj.update(d)
    cj.jprint()

def test_jprint():
    # only json array
    cj1 = CCJson()
    cj1[0] = ['1', '2']
    #cj1.jprint()
    # only json object
    cj2 = CCJson()
    cj2['a'] = 'abnormal'
    cj2['b'] = 'black'
    #cj2.jprint()
    # array + object
    cj3 = CCJson()
    cj3[0] = [1.1, False, True, 1.4e-10]
    cj3[1] = ['a', 'b', 'c']
    cj3['a'] = 'abnormal'
    cj3['b'] = 'black'
    cj3['c'] = None
    #cj3.jprint()
    # nested
    cj4 = CCJson()
    cj4._dd = cj3._dd
    cj4._dd[0].append(cj2._dd)
    cj4._dd['d'] = [1, 2]
    cj4.jprint()

def test_dump():
    cj = get_json()
    f = open('./test.json', 'w')
    cj.dump(f)
    f.close

def test_load():
    f = open('./test.json', 'r')
    cj = CCJson()
    cj.load(f)
    f.close
    cj.jprint()

if __name__ == '__main__':
    #test_get_set_del()
    #test_jprint()
    #test_update()
    #test_dump()
    #test_load()
    print 'test 1:'
    tt = TestPass1()
    tt.runTest()
    print 'test 2:'
    tt = TestPass2()
    tt.runTest()
