#!/usr/bin/python

import cgitb;	cgitb.enable();		import pymysql;

conn = pymysql.connect(db='laba_1_database',user='root',passwd='dss25',host='localhost');		c = conn.cursor();		conn.commit();


def mysql_print(text):

	c.execute(text);
	conn.commit();

	return c

#IN CHECK MODULE!!!!!!!!!

def check_input_id_base(id):

	mysql_print('''SELECT * FROM tovar ''')
	for row in c.fetchall(): 
		 if (str(row[0]) == str(id)):
			 return True;
	print('this id does not exist');
	
	return False ;

def check_id():

	while 1:
		count = input()
		try:
			count = int(count) 
			if( check_input_id_base( count ) ):
				break
		except ValueError:
			print('error (you must enter the number)')

	return count

def check_number():
	while 1:
		count = input()
		try:
			count = int(count) 
			if(count > 0):
				break
			else:
				print('error (you must enter the number)')# PRINT CORRECT
		except ValueError:
			print('error (you must enter the number)')

	return count;

def check_delta_amt(): ########## MYSQL ERROR
	
	print("Введите количество товара:");
	delta_amt = check_number();

	if(int(delta_amt)> 0):
		return delta_amt;
	else:print("error (enter a number greater than zero)");check_delta_amt();

def check_input_name_base(name):

	mysql_print('''SELECT * FROM tovar ''')
	for row in c.fetchall(): 
		 if (str(row[1]) == str(name)):
			 return True;
	print('this name does not exist');
	
	return False ;

#IN CHECK MODULE!!!!!!!!!

def input_sele_list_id(id,delta_amt,new_id,fl):
	
	
	if(fl=="new"):
		mysql_print("SELECT * FROM tovar WHERE id='"+str(id)+"';")
		for row in c: 
			tovar_name = row[1]
			prise_1 = float(row[2]);
		mysql_print("INSERT INTO sale VALUES ("+str(new_id)+",  "+ str(prise_1 * delta_amt)+"  ,' "+  str(tovar_name)+" ("+str(delta_amt)+") = "+str(prise_1 * delta_amt)  +" ')"); #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	elif(fl=="old"):
		mysql_print("SELECT * FROM tovar WHERE id='"+str(id)+"';")
		for row in c: 
			tovar_name = row[1]
			prise_1 = float(row[2]);
			mysql_print("INSERT INTO sale VALUES ("+str(new_id)+",  "+ str(prise_1 * delta_amt)+"  ,' "+  str(tovar_name)+" ("+str(delta_amt)+") = "+str(prise_1 * delta_amt)  +" ')"); #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			#mysql_print(" UPDATE sale SET comments = comments + ___  WHERE id = '"+str(new_id)+"' ")

	
	return 0;

def input_sele_list_name(name,delta_amt):
	mysql_print("SELECT * FROM tovar WHERE name='"+str(name)+"';")
	for row in c: 
		tovar_name = row[1]
		prise_1 = float(row[2]);
	
	mysql_print("INSERT INTO sale VALUES (1,  "+ str(prise_1 * delta_amt)+"  ,' "+  str(tovar_name)+" ("+str(delta_amt)+") = "+str(prise_1 * delta_amt)  +" ')"); #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	return 0;



def sales_list():

	print("\n Sales list: \n");

	mysql_print('''SELECT * FROM sale ORDER BY id''')

	for row in c: 
		
		#print(' id: %id'%row[0])
		print (' id:',row[0],'  price:',row[1],'\n comments:',row[2])
		#print(row)

	return 0;


def products_in_stock():

	print("\n Products in stock: \n");

	mysql_print('''SELECT * FROM tovar ORDER BY id''')

	for row in c: 
		print (" id:",row[0],'  name:',row[1],'  price:',row[2],'  amt:',row[3],'\n','comments:',row[4],'\n')
	return 0;


def popolnenie_suschestvuqchego_tovar_in_sklad(): ##########ERROR

	products_in_stock();

	print("\nПополнение товара...\n");
	print("Выберите существующий id товара из списка:");id = check_id();
	print("Введите количество поставленных единиц:");delta_amt = check_number();

	if (delta_amt > 0)and(1):	#ERROR!!!!!!!!!!!!!!!
		mysql_print(" UPDATE tovar SET amt = amt+'"+str(delta_amt)+"' WHERE id = '"+str(id)+"' ");

	return 0;


def sale_of_a_product_name():

	print("Введите имя товара для продажи: ");
	name = str(input());
	if ( check_input_name_base(name) ): 
		delta_amt = check_delta_amt()
		mysql_print(" UPDATE tovar SET amt = amt-'"+str(delta_amt)+"' WHERE name = '"+str(name)+"' ")
		input_sele_list_name(name,delta_amt);

	else:
		sale_of_a_product_name();



# mysql_print();

	return 0;





def sale_of_a_product_id(fl):

	print("Введите id товара для продажи: ");

	id = check_id();
	
	delta_amt = check_delta_amt();

	mysql_print(" UPDATE tovar SET amt = amt-'"+str(delta_amt)+"' WHERE id = '"+str(id)+"' ");




	if(fl=="new"):
		mysql_print('''SELECT max( id ) FROM sale ;''')
		for row in c: 
			new_id = (int(row[0])+1)
		input_sele_list_id(id,delta_amt,new_id,"new");
	elif(fl == "old"):
		mysql_print('''SELECT max( id ) FROM sale ;''')
		for row in c: 
			new_id=int(row[0])
		input_sele_list_id(id,delta_amt,new_id,"old")

	print("Продолжить продажу? (y)");
	if( str(input()) == "y" ):
		sale_of_a_product_id("old");
	else:
		return 0;


