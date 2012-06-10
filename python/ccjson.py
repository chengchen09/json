'''
Author: Chen Cheng
Description: a class used to handle json
'''
import pickle
from jsonparser import JsonParser, JsonParseError

def _jv_to_str(jv):
    '''transform the json value to a string'''
    ss = ''
    if type(jv) == type(''):
        ss = '"' + jv + '"'
    elif type(jv) == type({}):
        ss += '{'
        key_flag = False
        for key in jv.keys():
            if type(key) == type(''):
                key_flag = True
                ss += '"' + key + '": ' + _jv_to_str(jv[key]) + ', '
        if key_flag:
            ss = ss[:-2]
        ss += '}'
    elif type(jv) == type([]):
        ss += '['
        if len(jv) > 0:
            ss += _jv_to_str(jv[0])
        for i in range(1, len(jv)):
            ss += ',\n' + _jv_to_str(jv[i])
        ss += ']'
    elif jv == True:
        ss += 'true'
    elif jv == False:
        ss += 'false'
    elif jv == None:
        ss += 'null'
    else:
        ss = str(jv)
    return ss

class CCJson:
    def __init__(self):
        self._dd = None

    def load(self, f, mode='j'):
        '''load data from a json/python format file'''
        ss = ''
        if mode == 'p':
            self._dd = pickle.load(f)
            return
        elif mode == 'j':
            ss = f.read()
        elif mode == 's':
            ss = f
        else:
            print 'invalid mode:', mode
            return
        jparser = JsonParser(ss)
        self._dd = jparser.parse()

    def dump(self, f, mode='j'):
        '''dump data as json/python format into a file'''
        if mode == 'p':
            pickle.dump(self._dd, f)
        elif mode == 'j':
            f.write(self._str())
        else:
            print 'invalid mode'
        
    def update(self, d):
        '''update data from a python dictionary'''
        if type(self._dd) == type([]):
            keys = d.keys()
            keys.sort()
            for key in keys:
                self._dd[key] = d[key] 
        else:
            self._dd.update(d)

    def append(self, v):
        if type(self._dd) == type([]):
            self._dd.append(v)
        elif self._dd == None:
            self._dd = []
            self._dd.append(v)
        else:
            print "json object can't be append"

    def jprint(self):
        '''print the data as json format'''
        print self._str()

    def __setitem__(self, key, value):
        if self._dd == None:
            if type(key) == type(''):
                self._dd = {}
            elif type(key) == type(1):
                self._dd = []
            else:
                raise KeyError
        if (type(self._dd) == type([]) and type(key) != type(1)):
            raise IndexError
        elif type(self._dd) == type({}) and type(key) != type(''):
            raise KeyError
        self._dd[key] = value

    def __getitem__(self, key):
        return self._dd[key]

    def __delitem__(self, key):
        if type(self._dd) == type({}):
            del self._dd[key]
        elif type(self._dd) == type([]):
            self._dd.pop(key)
        else:
            raise KeyError
    
    def keys(self):
        if type(self._dd) == type({}):
            return self._dd.keys()
        elif type(self._dd) == type([]):
            return range(len(self._dd))
        else:
            return None

    def _str(self):
        '''return json format string'''
        return _jv_to_str(self._dd)
