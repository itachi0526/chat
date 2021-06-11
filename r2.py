def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None

    eric_word_count = 0
    denny_word_count = 0
    jacky_word_count = 0
    lolicon_word_count = 0

    eric_sticker_count = 0
    denny_sticker_count = 0
    jacky_sticker_count = 0
    lolicon_sticker_count = 0

    e_image = 0
    d_image = 0
    j_image = 0
    l_image = 0
    for line in lines:
        s = line.split(' ') # 切割完會變清單
        time = s[0]
        name = s[1]
        if name == '黃永升':
            if s[2] == '貼圖':
                eric_sticker_count += 1
            elif s[2] == '圖片':
                e_image += 1
            else:    
                for m in s[2:]:
                    eric_word_count += len(m)       
        elif name == '陳庭宇':
            if s[2] == '貼圖':
                denny_sticker_count += 1
            elif s[2] == '圖片':
                d_image += 1    
            else:                
                for m in s[2:]:
                    denny_word_count += len(m)
        elif name == '陳松杰':
            if s[2] == '貼圖':
                jacky_sticker_count += 1
            elif s[2] == '圖片':
                j_image += 1    
            else:    
                for m in s[2:]:
                    jacky_word_count += len(m)
        elif name == '錦宏':
            if s[2] == '貼圖':
                lolicon_sticker_count += 1
            elif s[2] == '圖片':
                l_image += 1    
            else:    
                for m in s[2:]:
                    lolicon_word_count += len(m)

    print('黃永升說了', eric_word_count, '個字且傳了', eric_sticker_count, '個貼圖，還傳了', e_image, '個圖片')
    print('陳庭宇說了', denny_word_count, '個字且傳了', denny_sticker_count, '個貼圖，還傳了', d_image, '個圖片')
    print('陳松杰說了', jacky_word_count, '個字且傳了', jacky_sticker_count, '個貼圖，還傳了', j_image, '個圖片')
    print('錦宏說了', lolicon_word_count, '個字且傳了', lolicon_sticker_count, '個貼圖，還傳了', l_image, '個圖片')       
        # print(s)       

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')    

def main():    
    lines = read_file('line.txt')
    lines = convert(lines)
    # write_file('output.txt', lines)

main() 