#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin, stdout

library = {}
# EOF까지 readline
while True:
    # readline & strip
    line = stdin.readline().strip()
    if line == "":
        break
    # 단어 조합과 빈도로 split
    word, cnt = line.split('\t')
    # library 사전에 단어 조합이 존재하면
    if word in library:
        library[word] = library[word] + int(cnt)    # 빈도 increment
    else:
        library[word] = int(cnt)    # 빈도 initialize

# library 사전의 key인 단어 조합을 정렬 후 traverse
for word in sorted(library.keys()):
    stdout.write(word + "\t" + str(library[word]) + "\n")   # 종합된 단어 조합과 빈도 출력