
# dic0: 한자 정규화
# dic1: 두음법칙 비적용 한자 목록 (없어도 될듯)
# dic2: 한중일 통합(공통) 한자 한자별 대표발음
# dic3: 한중일 호환(예외) 한자 한자별 대표발음
# dic4: 한자->한글 변환


def readfile(filepath):
    
    mapping = dict()
    
    with open(filepath, 'r', encoding='utf8') as fp:
        lines = fp.readlines()
        
    print('Total', len(lines), 'lines')
    
    for line in lines:
        if len(line) == 0:
            break
        if line.find('\t') == -1:
            continue
        if line[0] == '#':
            continue

        splited = line.rsplit('\t')
        if len(splited) <= 1:
            continue
        if len(splited) > 2:
            print('error. line len', len(splited))
            continue
        if len(splited[0]) == 0 or len(splited[1]) == 0:
            continue
        
        c_char = splited[0].strip()
        k_char = splited[1].strip()
        if len(c_char) != len(k_char):
            print('한자와 한글 길이가 다릅니다:', c_char, '->', k_char)
        mapping[c_char] = k_char
        
    return mapping


if __name__ == '__main__':
    m0 = readfile('dic0.txt')
    #m1 = readfile('dic1.txt')
    m2 = readfile('dic2.txt')
    m3 = readfile('dic3.txt')
    m4 = readfile('dic4.txt')
    