from lib import manage_users as mu

inp = input('1. Add\n2. Modify\n3. Delete\n?\n')
if inp=='1': mu.adduser()
elif inp=='2': mu.modifyuser()
else: mu.deluser()
