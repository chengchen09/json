'''
Author: Chen Cheng
Description: a class used to handle json
'''

from jsonparser import JsonParser, JsonParseError

def _jv_to_str(jv):
    '''transform the json value to a string'''
    ss = ''
    if type(jv) == type(''):
        ss = '"' + jv + '"'

    elif type(jv) == type({}):
        ss += '{'
        keys = jv.keys()
        if len(keys) > 0:
            ss += '"' + keys[0] + '": ' + _jv_to_str(jv[keys[0]])
        for i in range(1, len(keys)):
            ss += ', "' + keys[i] + '": ' + _jv_to_str(jv[keys[i]])
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
        self._dd = {}

    def load(self, f, mode='j'):
        '''load data from a json/python format file'''
        ss = ''
        if mode == 'p':
            pass
        elif mode == 'j':
            ss = f.read()
        elif mode == 's':
            ss = f
        else:
            print 'invalid mode'
            #TODO: 
            return
        jparser = JsonParser(ss)
        self._dd = jparser.parse()

    def dump(self, f, mode='j'):
        '''dump data as json/python format into a file'''
        if mode == 'p':
            pass
        elif mode == 'j':
            f.write(self._str())
        else:
            print 'invalid mode'
        
    def update(self, d):
        '''update data from a python dictionary'''
        # TODO: handle the key is string or number self._dd.update(d)

    def jprint(self):
        '''print the data as json format'''
        print self._str()

    def __setitem__(self, key, value):
        self._dd[key] = value

    def __getitem__(self, key):
        return self._dd.get(key, None)

    def __delitem__(self, key):
        if self._dd.get(key, None) != None:
            del self._dd[key]
    
    def keys(self):
        return self._dd.keys()

    def _str(self):
        '''return json format string'''
        keys = self._dd.keys()
        keys.sort()
        ss = ''
         
        if len(keys):
            pos = 0
            if type(keys[0]) == type(0):
                while pos < len(keys):
                    if type(keys[pos]) == type(0):
                        ss += _jv_to_str(self._dd[keys[pos]]) + '\n'
                        pos = pos + 1
                    else:
                        break
            if pos < len(keys):
                ss += '{\n'
                ss += '"' + keys[pos] + '": ' + _jv_to_str(self._dd[keys[pos]])
                pos = pos + 1
                while pos < len(keys):
                    ss += ',\n"' + keys[pos] + '": ' + _jv_to_str(self._dd[keys[pos]])
                    pos = pos + 1
                ss += '\n}\n'

        return ss
