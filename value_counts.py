import pandas as pd

def value_count(s: pd.Series, print_total=False):
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
    
    if print_total == True:
        VC = pd.concat([
            VC,
            pd.DataFrame( 
                index=['--', 
                       'TOTAL'
                      ], 
                columns=[name, 'count', 'norm'],
                data=[['--',              '--',              '--'],
                      ['--', VC['count'].sum(),  VC['norm'].sum()]],              
            )
        ])
    return VC
