'''
Simple power factor calculator.

a and b can be any of ['s', 'p', 'q', ['pf', 'angle']]
a_value and b_value correspond to selected a and b variables

returns dictonary including results ['s', 'p', 'q', 'pf', 'angle']
'''

import math

def power_factor(a, a_value, b, b_value, rounding=4):
	values = {}
	values['input_a'] = a
	values['input_b'] = b
	values[a] = a_value
	values[b] = b_value
	
	if 'pf' in values or 'angle' in values:
		if 'angle' in values:
			values['pf'] = math.cos(math.radians(values['angle']))
		else:
			values['angle'] = math.degrees(math.acos(values['pf']))

		if 's' in values and 'pf' in values:
			values['p'] = values['s'] * values['pf']
			values['q'] = math.sqrt(values['s']**2 - values['p']**2)
		elif 'p' in values and 'pf' in values:
			values['s'] = values['p'] / values['pf']
			values['q'] = math.sqrt(values['s']**2 - values['p']**2)
		elif 'q' in values and 'pf' in values:
			if values['pf'] == 0:
				values['s'] = values['q']
				values['p'] = 0
			else:
				values['s'] = values['q'] / math.sin(math.radians(values['angle']))
				values['p'] = math.sqrt(values['s']**2 - values['q']**2)
		else:
			return False
	else:
		if 's' in values and 'p' in values:
			values['q'] = math.sqrt(values['s']**2 - values['p']**2)
		elif 's' in values and 'q' in values:
			values['p'] = math.sqrt(values['s']**2 - values['q']**2)
		elif 'p' in values and 'q' in values:
			values['s'] = math.sqrt(values['p']**2 + values['q']**2)
		else:
			return False
		
		values['pf'] = values['p'] / values['s']
		values['angle'] = math.degrees(math.acos(values['pf']))
	
	for key, value in values.items():
		if isinstance(value, float):
			values[key] = round(value, rounding)

	return values
