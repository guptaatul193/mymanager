import os,datetime

dtfmt_all = { 'DD-MM-YYYY' : '%d-%m-%Y' , 'DD-MM-YY' : '%d-%m-%y' , 'DD/MM/YYYY' : '%d/%m/%Y' , 'DD/MM/YY' : '%d/%m/%y' , 'DD-Mon-YYYY' : '%d-%b-%Y' , 'DD/Mon/YYYY' : '%d/%b/%Y' , 'DD/Mon/YYYY' : '%d/%b/%Y', 'DD/Mon/YY' : '%d/%b/%y' }


def get_datefmt ():
	return dtfmt_all [gulpconf()['date']]

def gulpconf ( ):
	with open ( os.path.abspath( r'AppData\conf.txt'),'r' ) as pf:
		fl = pf.readlines()
	conf = {}
	for i in fl:
		if '=' in i:
			conf [ i.strip().split('=')[0].strip() ] = i.strip().split('=')[1].strip()
	return conf