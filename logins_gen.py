#!/usr/bin/python
import sys 

class LoginGenerator:
	def __init__(self):
		self.main()


	def spliter(self,name_surname):
		splited = name_surname.split()
		name = splited[0].lower()
		surname = splited[1].lower()
		f_name = splited[0][0].lower()
		f_surname = splited[1][0].lower()
		return name, surname, f_name, f_surname
		

	def main(self):
		try:

			file_name = sys.argv[1] #input('Path: ')
			with open(file_name, 'r') as file1:
				word_lst = []
				chars = [' ', '_', '-', '+', '.', ',', '!']
				lines = file1.readlines()

				for line in lines:
					name, surname, f_name, f_surname = self.spliter(line)
					word_lst.append(name)
					word_lst.append(surname)
					word_lst.append(surname + name)
					word_lst.append(f_name + surname) 
					word_lst.append(surname + f_name)
					word_lst.append(f_surname + name) 
					word_lst.append(name + f_surname)

					for char in chars:
						word_lst.append(name + char + surname)
						word_lst.append(surname + char + name)
						word_lst.append(char + surname + name)
						word_lst.append(char + name + surname)
						word_lst.append(surname + name + char)
						word_lst.append(name + surname + char)
						word_lst.append(f_name + char + surname)
						word_lst.append(surname + char + f_name)
						word_lst.append(f_surname + char + name)
						word_lst.append(name + char + f_surname)

				new_file_name = f'{file_name[:-4]}_wordlist.txt'
				with open(new_file_name, 'w') as file2:
					for word in word_lst:
						file2.write(word + '\n')
						
		except:
			print('Wrong No path to the file!\nExample: longins_gen.py file_path.txt')


if __name__ == '__main__': LoginGenerator() 
