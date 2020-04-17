
import os
from os import system
#Каталог из которого будем брать изображения
directory = os.path.abspath(os.curdir)
slr = '''
import sys
from os import system
system('dir')
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
'''
#Получаем список файлов в переменную files
files = os.listdir(directory)
for i in range(12, 0, -1):
	if f'test{i}.txt' in files:
		result = f'test{i}'
		system(f'rmdir /s /q "{result}"')
for i in range(12, 0, -1):
	if f'test{i}.txt' in files:
		result = f'test{i}'
		system(f'mkdir "{result}"')
for i in range(12, 0, -1):
	if f'test{i}.txt' in files:
		dsin = directory + f'/test{i}/input.txt'
		dsout = directory + f'/test{i}/output.txt'
		dsf = directory + f'/test{i}/setup.py'
		setup = open(f'test{i}.txt', 'r').readlines()
		s1 = open('setup.py', 'r').read()
		s2 = open(dsf, 'w')
		s1 = slr + s1
		s2.write(s1)
		s2.close()
		d1 = open(dsin, 'w')
		for j in setup:
			print(j == 'Input: \n')
			if not (j == 'Input: \n' or j == 'Input:\n'):
				if j.lower() == 'output: \n' or j.lower() == 'output:\n':
					break
				else: d1.write(j)
		d1.close()
		d2 = open(dsout, 'w')
		d2.close()
for i in range(12, 0, -1):
	if f'test{i}.txt' in files:
		filename = directory + f'/test{i}/setup.py'
		cds = directory + f'/test{i}'
		system(f'python {filename}')
		riko = f'test{i}.txt'
		riko2 = f'{directory}/test{i}/output.txt'
		ready = 0
		mentos = ''
		riko = open(riko, 'r').readlines()
		riko2 = open(riko2, 'r').readlines()
		for j in riko:
			if j.lower() == 'output: \n' or j.lower() == 'output:\n':
				ready = 1
			elif ready:
				mentos += j
		if mentos == riko2:
			print(f'test{i}: ✔')
		else: print(f'test{i}: ❌')
'''
Input:
3
1 2 3
8 9 4
7 6 5
Output:

'''