#!/usr/bin/python
# index.py


import sys;	sys.path.insert(0, "./module");	import my_md_menu

def data_in_file (name_file,data):
 
	f_url = open("database/"+name_file, 'w', encoding='UTF-8')
	f_url.write(data)
	f_url.close
	
	return 0

my_md_menu.menu()


