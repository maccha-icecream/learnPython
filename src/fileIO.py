import sys

def last_line(name):
    f = open(name, 'r')
    while True:
        line = f.readline()
        if line == '':
            print(line)
            f.close()
            break

def number_of_characters(name):
    with open(name, 'r') as f:
        return len(f.read())

def file_upper(infile, outfile):
    with open(infile,'r') as source, open(outfile, 'a') as dist:
        line = source.read()
        dist.write(line.upper())

def file_encode():
    with open('text/shift-jis.txt', 'a', encoding='utf-8') as f:
        # print(f.read())
        f.write('\nかきくけこ')

if __name__ == "__main__":
    with open('text/source.txt', 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            print(line)
    print('------ 末尾の改行文字を削除すると以下のようになります-------')
    with open('text/source.txt', 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            print(line.rstrip('\n'))