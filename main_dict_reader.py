from DictionaryReader import DictionaryReader


def test_single():
	c = {
		'logical': 'and',
		'translation': {
			'name': ['C_VB', 'C_TSR'],
			'operator': ['=', '='],
			'value': ['1', '9']
		}
	}
	print(dict_reader.get_translation_id(c, 'LTRACK'))

def test_loop():
	for c_vb in [0, 1, 2, 3, 5, 6, 7]:
		for c_tsr in [0, 5, 6, 9, 10]:
			c = {
				'logical': 'and',
				'translation': {
					'name': ['C_VB', 'C_TSR'],
					'operator': ['=', '='],
					'value': ['{}'.format(c_vb), '{}'.format(c_tsr)]
				}
			}
			print('C_VB: {},\tC_TSR: {},\tLABEL: {}'.format(c_vb, c_tsr, dict_reader.get_translation_id(c, 'LTRACK')))

if __name__ == "__main__":
	dict_reader = DictionaryReader()
	dict_reader.start_reading()

	test_loop()
	