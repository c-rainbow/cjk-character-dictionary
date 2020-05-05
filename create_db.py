import sqlite3
import os

from kldp_masoris import create_mapping as m_mapping
from kldp_nikl import create_mapping as n_mapping

DIR_MASORIS = 'kldp_masoris'
DIC_FILES_MASORIS = ('dic0.txt', 'dic2.txt', 'dic3.txt', 'dic4.txt')

DIR_NIKL = 'kldp_nikl'
DIC_FILES_NIKL = ('hanja_type1.txt', 'hanja_type2_1.txt', 'hanja_type2_2_1.txt', 'hanja_type3_1_1.txt')


def InsertIntoTable(mapping):
    mapping_list = list(mapping.items())
    print('mapping_list len:', len(mapping_list))

    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    commited = 0
    #while commited < len(mapping_list):
    cursor = c.executemany(
        'REPLACE INTO HanjaToHangul(hanja, hangul) VALUES(?,?)', mapping_list)
    print('row_count:', cursor.rowcount)
    #    commited = cursor.rowcount
    conn.commit()
        
    conn.close()
    
    
if __name__ == '__main__':
    
    for filename in DIC_FILES_MASORIS:
        filepath = os.path.join(DIR_MASORIS, filename)
        mapping = m_mapping.readfile(filepath)
        InsertIntoTable(mapping)
    
    for filename in DIC_FILES_NIKL:
        filepath = os.path.join(DIR_NIKL, filename)
        mapping = n_mapping.readfile(filepath)
        InsertIntoTable(mapping)
        
    print('Done')