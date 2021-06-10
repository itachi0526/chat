def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Dio':
            person = 'Dio'
            continue
        elif line == 'Eric':
            person = 'Eric'
            continue
        if person:
            new.append(person + '：' + line)
    return new        

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')    

def main():    
    lines = read_file('001.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main() 