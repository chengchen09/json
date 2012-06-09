'''
Author: Chen Cheng
Description: a class used to parse the json format string
'''

_ESCAPE_STR = ' \n\t\r'
_QUOTE_STR = '"\\/bfnrtu'
_ERR_MSG = 'Json parse error'

class JsonParser:
    
    def __init__(self, ss=None):
        self._ss = ss
        self._index = 0
        self._line = 1
        self._pres = -1
        self._dd = {}

    def parse(self):
        try:
            narray = 0
            while self._index < len(self._ss):
                c = self._ss[self._index]
                if c == '{':
                    self._index += 1
                    self._dd.update(self._parse_object())
                elif c == '[':
                    self._index += 1
                    self._dd[narray] = self._parse_array()
                    narray += 1
                else:
                    self._index += 1
            return self._dd
        except JsonParseError as e:
            e.err_msg()

    def _parse_object(self):
        try:
            dd = {}
            self._escape()
            # empty object {}
            if self._ss[self._index] == '}':
                self._index += 1
                return dd
            elif self._ss[self._index] != '"':
                raise JsonParseError(_ERR_MSG, self._ss, self._index)
            
            self._index += 1
            while True:
                key = self._parse_string()
                self._escape()
                if self._ss[self._index] != ':':
                    raise JsonParseError(_ERR_MSG, self._ss, self._index)
                self._index = self._index + 1
                self._escape()
                dd[key] = self._parse_value()
                self._escape()
                if self._ss[self._index] == '}':
                    self._index = self._index + 1
                    break
                elif self._ss[self._index] == ',':
                    self._index = self._index + 1
                    self._escape()

                if self._ss[self._index] != '"':
                    raise JsonParseError(_ERR_MSG, self._ss, self._index)
                self._index = self._index + 1
            return dd
        except JsonParseError as e:
            e.err_msg()

    def _parse_array(self):
        ll = []
        self._escape()
        # empty array []
        if self._ss[self._index] == ']':
            self._index += 1
            return ll
        while True:
            v = self._parse_value()
            ll.append(v)
            self._escape()
            if self._ss[self._index] == ',':
                self._index = self._index + 1
                self._escape()
            elif self._ss[self._index] == ']':
                self._index = self._index + 1
                return ll
            else:
                raise JsonParseError(_ERR_MSG, self._ss, self._index)

    def _parse_string(self):
        begin = end = self._index
        try:
            while self._ss[end] != '"':
                if self._ss[end] == '\\':
                    end = end + 1
                    if self._ss[end] not in _QUOTE_STR:
                        raise JsonParseError(_ERR_MSG, self._ss, self._index)
                end = end + 1
        except IndexError:
            raise JsonParseError(_ERR_MSG, self._ss, self._index)
        self._index = end + 1
        return self._ss[begin:end]
    
    def _parse_number(self):
        begin = end = self._index
        end_str = _ESCAPE_STR + ',}]'
        try:
            while self._ss[end] not in end_str:
                end = end + 1
            ns = self._ss[begin:end]
            if '.' in ns or 'e' in ns or 'E' in ns or ns == 'int' or ns == '-inf':
                n = float(ns)
            else:
                n = int(ns)
            self._index = end
            return n
        except IndexError:
            raise JsonParseError(_ERR_MSG, self._ss, self._index)

    def _parse_value(self):
        v = None
        c = self._ss[self._index]
        if c == '{':
            self._index = self._index + 1
            v = self._parse_object()
        elif c == '[':
            self._index = self._index + 1
            v = self._parse_array()
        elif c == '"':
            self._index = self._index + 1
            v = self._parse_string()
        elif c == 'n' and self._ss[self._index: self._index + 4] == 'null':
            self._index = self._index + 4
            v = None
        elif c == 't' and self._ss[self._index: self._index + 4] == 'true':
            self._index = self._index + 4
            v = True
        elif c == 'f' and self._ss[self._index: self._index + 5] == 'false':
            self._index = self._index + 5
            v = False
        else:
            v = self._parse_number()
        return v

    def _escape(self):
        try:
            while self._ss[self._index] in _ESCAPE_STR:
                self._index = self._index + 1
        except IndexError:
            raise JsonParseError(_ERR_MSG, self._ss, self._index)

class JsonParseError(ValueError):
    def __init__(self, msg, ss, index):
        self._msg = msg
        self._ss = ss
        self._index = index
        self._count_line_col()
        #self.err_msg()
        #assert(0)

    def err_msg(self):
        print '%s: line %d column %d char %s' % (self._msg, self._line, self._col, self._ss[self._index])

    def _count_line_col(self):
        self._line = self._ss.count('\n', 0, self._index) + 1
        if self._line == 1:
            self._col = self._index
        else:
            self._col = self._index - self._ss.rindex('\n', 0, self._index)
