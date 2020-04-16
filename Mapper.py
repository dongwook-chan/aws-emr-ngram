#!/usr/bin/python
# -*- coding: utf-8 -*-:

from sys import stdin, stdout

# EOF까지 readline
while True:
    # readline & strip
    line = stdin.readline().strip()
    if len(line) == 0:
        break;

    words = line.split() # split
    count = len(words)  # 단어 개수
    count = count - 1   # 단어 개수 decrement
    if count != 0:  # 단어 1개인 문장은 무시
        for i in range(count): # 연속된 두 단어와 그 빈도를 1로 출력
            stdout.write(words[i] + " " + words[i+1] + "\t1\n")
