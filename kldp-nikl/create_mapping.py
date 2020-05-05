



def readfile(filepath):
    with open(filepath, 'r', encoding='utf8') as fp:
        lines = fp.readlines()
        
    mapping = dict()
    for line in lines:
        splited = line.split(':')
        if len(splited) != 3:
            print('line length is not 3:', line)
        korean = splited[0].strip()
        chinese = splited[1].strip()
        
        if len(korean) != len(chinese):
            print('length diff:', korean, chinese)
           
        mapping[chinese] = korean
        
    print('Finished reading', len(mapping), 'mappings')
    return mapping
    
    
if __name__ == '__main__':
    m1 = readfile('hanja_type1.txt')
    m2_1 = readfile('hanja_type2_1.txt')
    m2_2_1 = readfile('hanja_type2_2_1.txt')
    m3_1_1 = readfile('hanja_type3_1_1.txt')
    
    print(m3_1_1)
    print('done')