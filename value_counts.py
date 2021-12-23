import pandas as pd

def value_count(s: pd.Series):
    """
    ``add docs later``
    """
    name = s.name
    VC = s.value_counts().reset_index().rename(columns={
        'index' : name,
        name : 'count'})
    VC = pd.concat([
        VC,
        pd.DataFrame(
            data=[['--', s.isna().sum()]], 
            index=['NaNs'], 
            columns=[name, 'count']
        )])
    VC['norm'] = VC['count'] / VC['count'].sum()
    return VC
