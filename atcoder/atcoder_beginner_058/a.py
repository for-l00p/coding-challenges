#!/usr/bin/python3
# https://abc058.contest.atcoder.jp/tasks/abc058_a

a, b, c = map(int, input().split())
print('YES') if b - a == c - b else print('NO')
