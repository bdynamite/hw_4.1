# coding: utf-8

import pandas as pd

PATH = 'C:\\Users\\а\\PycharmProjects\\names'


def get_tables(years):
    tables = []
    colums = ['Name', 'Gender', 'Count']
    for year in years:
        path = '\\yob'.join([PATH, '.'.join([str(year), 'txt'])])
        try:
            table = pd.read_csv(path, names = colums)
            tables.append(table)
        except OSError as e:
            print('table {} not found'.format('.'.join([str(year), 'txt'])))
            continue
    return tables


def count_top_n(years, n):
    tables = get_tables(years)
    final_table = pd.DataFrame({'Name':[], 'Gender':[], 'Count':[]})
    for table in tables:
        final_table = final_table.append(table)
    final_table = final_table.groupby(('Gender', 'Name')).sum().reset_index().sort_values(by='Count', ascending=False)
    print(list(final_table.iloc[0:n]['Name'].get_values()))


def count_dynamics(years):
    tables = get_tables(years)
    result = {'M': [], 'F': []}
    male = []
    female = []
    for table in tables:
        table = table.groupby(('Gender')).sum().reset_index().sort_values(by='Gender')
        result['M'].append(table.iloc[1]['Count'])
        result['F'].append(table.iloc[0]['Count'])
    print(result)


count_top_n([1990, 1989], 5)
count_dynamics([1990, 1789])
