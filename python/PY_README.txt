1. ����
github address: https://github.com/chengchen09/json.git
���ʵ�ְ���2���ļ���ccjson.py��jsonparser.py������ccjson�е���CCJson�������û��ṩ�˲���Json��ʽ����API��API�ľ�����Ŀ���£�
class CCJson:
	load(self, f)����file����л��json��ʽ�����ݡ�
	loads(self, ss): ��python string�л��json��ʽ�����ݡ�
	load_python(self, f): ��file����л��python��ʽ�����ݡ�
	dump(self, f)����json��ʽ������д�뵽file f�С�
	dumps(self): ����json��ʽ��python string��
	dump_python(self, f)����json����д�뵽file f�С�
	update(self, d)��dΪpython���ֵ䣬���ڸ���json��������Ϣ��
	append(self, v)�����ڶ�json��array����append������
	�ṩ���ֵ�ģʽ�Ķ���д��ɾ���Լ�keys()�Ĺ��ܡ�

2. �����ļ�
����test.py��test_pass1.py������test.py���ɽ��в��ԡ����Ի�����test_pass1.json, test_pass1.pj, test_pass2.json, test_pass2.pj�ĸ��ļ�

