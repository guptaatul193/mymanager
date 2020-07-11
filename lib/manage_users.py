import os,datetime
from lib import helper


hdr = 'usrid,usrnm,lvl,doj,lwd,mob'
hdr_dict = { '1':'usrnm' , '2':'lvl' , '3':'mob' }

class User:
	
	def __init__ ( self , usrid , usrnm , lvl , doj , lwd , mob ):

		self.usrid = usrid
		self.usrnm =  usrnm
		self.lvl = lvl
		self.doj = doj
		self.mob = mob
		self.lwd = lwd

def adduser ( ):
	getusr = gulpuser()
	newusr = {}
	print ( 'Please provide the below inputs :' )
	for cont in hdr.split(','):
		while (True):
			if cont in ('doj','lwd'): break
			newusr [cont] = str(input('%s : ' %(cont.upper()))).lower().strip()
			if len( [ getattr(i,cont) for i in getusr if newusr[cont] == getattr(i,cont) and getattr(i,'lwd') == 'na'] ) >0 and cont=='usrid':
				print('ID already taken, please try again !! ')
				continue
			elif len( [ getattr(i,cont) for i in getusr if newusr[cont] == getattr(i,cont) ] ) >0 and cont=='usrid':
				return reactivate_user ( getusr, newusr[cont])
			break
	newusr ['doj'] = str(datetime.date.today().strftime(helper.get_datefmt()))
	newusr ['lwd'] = 'na'
	i = User ( newusr['usrid'] , newusr['usrnm'] , newusr['lvl'] , newusr['doj'] , newusr['lwd'] , newusr['mob'] )
	if validate_user (i.__dict__):
		getusr.append ( User ( newusr['usrid'] , newusr['usrnm'] , newusr['lvl'] , newusr['doj'] , newusr['lwd'] , newusr['mob'] ) )
		writeout( getusr )

def reactivate_user ( getusr, uid):
	print ('A matching DEACTIVATED User ID found. Cannot add a new user with the same ID. Want to reactivate "%s" ?' %( [getattr (u,'usrnm') for u in getusr if u.usrid == uid ][0]))		
	if input('Y/N : ').strip().lower() == 'y':
		x = [i for i in getusr if i.usrid == uid and i.lwd != 'na'][0].lwd = 'na'
		writeout (getusr)
		return True
	return False
		
	
def modifyuser ():
	getusr = gulpuser()
	if len( [i for i in getusr if i.lwd == 'na'] ) == 0 :
		return False
	while(True):
		inp = input('Please enter the User ID ( Modify User ): ')
		usrid_mod = [i for i in getusr if i.usrid == inp.strip().lower() and i.lwd == 'na']
		if len( usrid_mod ) == 0:
			print ('User ID not found !!!')
			continue
		print (hdr_dict)
		ch = input ('Your choice? :')
		try: 
			val = input ( hdr_dict[ch] + ' : ' )
			if validate_user ( {hdr_dict[ch] : val } ): 
				setattr ( usrid_mod[0], hdr_dict[ch], val )
				writeout (getusr)
		except:
			print('Invalid Choice, please try again !!')
			continue
		break

def deluser ( ):
	getusr = gulpuser()
	if len( [i for i in getusr if i.lwd == 'na'] ) == 0 :
		return False
	inp = input('Please enter the User ID ( Delete User ): ')
	match = [i for i in getusr if i.usrid == inp.strip().lower() and i.lwd == 'na']
	if len(match)>0:
		match[0].lwd = datetime.date.today().strftime(helper.get_datefmt())
	else: return False
	writeout( getusr )
	

def gulpuser ():
	usrlst = []
	with open ( os.path.abspath(r'AppData\Users.csv') , 'r' ) as u:
		tmp = u.readlines()[1:]
	if (len(tmp)==0): return []
	for i in tmp:
		m = i.replace('\n','').split(',')
		usrlst.append(User ( m[0] , m[1] , m[2] , m[3] , m[4] , m[5] ))
	return usrlst

def writeout ( obj ):
	with open (os.path.abspath(r'AppData\Users.csv') , 'w' ) as u:
		u.write (hdr+'\n')
		for i in obj:
			u.write ('%s,%s,%s,%s,%s,%s\n' %( i.usrid, i.usrnm, i.lvl, i.doj, i.lwd, i.mob ))


def validate_user ( info ):
	out = True
	if len ( list ( info.keys() ) ) == 0: return False
	for i in list(info.keys()):
		if i in ( 'doj', 'lwd' ): continue

		if i == 'usrid':
			if ',' in info [i]: out = False
			if ' ' in info [i]: out = False
			if len ( info[i] ) > 10: out = False

		if i == 'usrnm':
			if len([j for j in info[i].strip().split() if j.isalpha() == False]) > 0: out = False
			if ',' in info [i]: out = False
			if len ( info[i] ) > 30: out = False
		
		if i == 'lvl':
			if info[i].lower() not in ['admin','user']: out = False

		if i == 'mob':
			if ',' in info [i]: out = False
			if len([j for j in info[i].strip().split() if j.isnumeric() == False]) > 0: out = False
			if len ( info[i] ) > 15: out = False
	return out
			

