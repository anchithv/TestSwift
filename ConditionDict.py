class ConditionDict(object):
	def __init__(self):
		self.condition = {
			'logical': None,
			'translation': {
				'name': [],
				'operator': [],
				'value': []
			}
		}

	def get(self):
		return self.condition
