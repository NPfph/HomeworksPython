import pandas as pd

print('-'*30)
print('Информация об отделах')

dep_card = {
        'Отдел': ['M','CI','CS','A','D'],
        'Номер отдела' : ['1','2','3','4','5'],
        'Блок': ['A','B','C','D','E'],
        'ID' : ['01','02','03','04','05']
}
    
cc = pd.DataFrame(data = dep_card)

with open('departments.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{cc}')
        cl.write('\n')
    
print(cc)

