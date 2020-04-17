
import sys
from os import system
system('dir')
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
n = int(input())
print(n+2)