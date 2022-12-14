"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
Алгоритм RLE

in
Enter the name of the file with the text:
'text_words.txt'
Enter the file name to record:
'text_code_words.txt'
Enter the name of the file to decode:
'text_code_words.txt'

out
aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

out in file
'text_words.txt'
aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
vbbwwPPuuuTTYyWWQQ

'text_code_words.txt'
5a29v4s3D3d2F4g2O3i2a1
1v2b2w2P3u2T1Y1y2W2Q"""

file = open('text_words.txt', 'w', encoding='UTF-8')
file.write(input('Напишите текст необходимый для сжатия: '))
file = open('text_words.txt', 'r')
my_txt = file.readline()
file.close()
txt_compr = my_txt.split()



def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond
    
def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


txt_compr = file_encod(my_txt)

file = open('text_code_words.txt', 'w', encoding='UTF-8')
file.write(f'{txt_compr}')
file.close()
print(f"Текст шифрованный {txt_compr}")

print(f"Текст после дешифровки: {decoding(txt_compr)}")