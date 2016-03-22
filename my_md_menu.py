#!/usr/bin/python
# my module menu
import os



import test_mysql


def enter():
	print ("\n to access the main menu, press 'Enter'\n");
	input();
	menu();
	return 0;

def print_file(file):
	
	
	f_menu = open(file,'r')
	#("text/menu.txt",'r')
	while True:
		line = f_menu.readline()
		if len(line) == 0: 
			break
		print(line, end='')
	f_menu.close()
	return 0


def input_flad(flag):

	if (flag == "exit"):
		return 0;

	elif (flag == "1"):
		test_mysql.products_in_stock();
		print_file("text/sale_of_a_product.txt")
		flag = str(input())
		while True:
			if (flag=="1"):
				test_mysql.sale_of_a_product_id("new");break;
			elif (flag=="2"):
				test_mysql.sale_of_a_product_name();break;
			elif (flag == "exit"):
				menu();
			else:
				print("error (entered incorrect command)");flag = str(input())
		enter();

	elif (flag == "2"):
		test_mysql.popolnenie_suschestvuqchego_tovar_in_sklad();
		enter();

	elif (flag == "3"):
		test_mysql.sales_list();
		enter();

	elif (flag == "4"):
		test_mysql.products_in_stock();
		enter();

	else :
		print("error (entered incorrect command)"); 		input();		menu();


def menu():
	
	os.system('clear')
	print_file("text/menu.txt")
	input_flad(str(input()))
	
	return 0
