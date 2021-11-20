import pandas as pd

def value_count(s: pd.Series):
	"""
	``add docs later``
	"""
	name = s.name
	VC = s.value_counts().reset_index().rename(columns={
		'index' : name,
		name : 'count'})
	VC['norm'] = VC['count'] / VC['count'].sum()
	return VC
