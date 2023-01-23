import json
import xmltodict


class DictionaryReader(object):
	"""

	"""
	# ------------------ #
	# Class attribute(s) #
	# ------------------ #

	# ----------- #
	# Constructor #
	# ----------- #
	def __init__(self, dict_path='dictionary.xml'):
		"""

		:param dict_path:
		"""
		self.dict_dict = None
		# self.get_value = None
		self.dict_path = dict_path

	# --------- #
	# Method(s) #
	# --------- #
	def start_reading(self):
		"""

		:return:
		"""
		with open(self.dict_path, "r") as dict_file:
			self.dict_dict = xmltodict.parse(dict_file.read())
		with open('dictionary.json', 'w') as json_file:
			json_dict = json.dumps(self.dict_dict)
			json_file.write(json_dict)


	def get_all_logical_objects_type(self):
		tmp = []
		load = self.dict_dict['Dictionary']['LogicalObjects']['LogicalObject']
		for lo in load:
			tmp.append(lo['@type'])
		return tmp

	def get_translation(self, translation=None, logtype=None):
		result = []
		tmp = []
		load = self.dict_dict['Dictionary']['LogicalObjects']['LogicalObject']
		for i in load:
			if logtype is not None:
				if i['@type'] != logtype:
					continue
			i = i.get('Translation', None)
			if i is None:
				continue
			for j in i:
				if j['@id'] == translation:
					tmp.append(j['LogicalOperator'])
					tmp.append(j['Condition'])
					result.append(tmp)
					tmp = []
		translation = [{
			'logical': None,
			'translation': {
				'name': [],
				'operator': [],
				'value': []
			}
		} for i in range(len(result))]
		for i, a in enumerate(result):
			translation[i]["logical"] = a[0]
			if not isinstance(a[1], list):
				if "=" in a[1]:
					word = a[1].split("=")
					translation[i]['translation']['name'].append(word[0])
					translation[i]['translation']['operator'].append("=")
					translation[i]['translation']['value'].append(word[1])
				elif "<>" in a[1]:
					word = a[1].split("<>")
					translation[i]['translation']['name'].append(word[0])
					translation[i]['translation']['operator'].append("<>")
					translation[i]['translation']['value'].append(word[1])
				elif "<" in a[1]:
					word = a[1].split("<")
					translation[i]['translation']['name'].append(word[0])
					translation[i]['translation']['operator'].append("<")
					translation[i]['translation']['value'].append(word[1])
				elif ">" in a[1]:
					word = a[1].split(">")
					translation[i]['translation']['name'].append(word[0])
					translation[i]['translation']['operator'].append(">")
					translation[i]['translation']['value'].append(word[1])
				continue
			for j in a[1]:
				if "=" in j:
					word = j.split("=")
					translation[i]['translation']['name'].append(word[0])
					translation[i]['translation']['operator'].append("=")
					translation[i]['translation']['value'].append(word[1])
				elif "<>" in j:
					word = j.split("<>")
					translation[i]['translation']['name'].append(word[0])
					translation[i]['translation']['operator'].append("<>")
					translation[i]['translation']['value'].append(word[1])
				elif "<" in j:
					word = j.split("<")
					translation[i]['translation']['name'].append(word[0])
					translation[i]['translation']['operator'].append("<")
					translation[i]['translation']['value'].append(word[1])
				elif ">" in j:
					word = j.split(">")
					translation[i]['translation']['name'].append(word[0])
					translation[i]['translation']['operator'].append(">")
					translation[i]['translation']['value'].append(word[1])
		return translation

	def get_translation_id(self, condition=None, logtype=None):
		result = []
		load = self.dict_dict['Dictionary']['LogicalObjects']['LogicalObject']
		for i in load:
			if logtype is not None:
				if i['@type'] != logtype:
					continue
			i = i.get('Translation', None)
			if i is None:
				continue
			for j in i:
				if self.check_condition(j, condition):
					result.append(j['@id'])
		return result

	@staticmethod
	def check_condition(dict_file, dict_user):
		if dict_file['LogicalOperator'] == dict_user['logical']:
			check = True
		else:
			check = False
			return check
		if not isinstance(dict_file['Condition'], list):
			dict_file['Condition'] = [dict_file['Condition']]
		if not isinstance(dict_user['translation']['name'], list):
			dict_user['translation']['name'] = [dict_user['translation']['name']]
		if not isinstance(dict_user['translation']['operator'], list):
			dict_user['translation']['operator'] = [dict_user['translation']['operator']]
		if not isinstance(dict_user['translation']['value'], list):
			dict_user['translation']['value'] = [dict_user['translation']['value']]
		if len(dict_file['Condition']) != len(dict_user['translation']['name']):
			check = check and False
			return check
		for i, c in enumerate(dict_file['Condition']):
			user = []
			for j, d in enumerate(dict_user['translation']['name']):
				user.append(d + dict_user['translation']['operator'][j] + dict_user['translation']['value'][j])
			if c in user:
				check = check and True
			else:
				check = check and False
				return check
		return check
