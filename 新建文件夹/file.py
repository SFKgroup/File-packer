try:
    thing_list=['''''']
    name_list=['']
    for a,b in zip(thing_list,name_list):
        grand=open(b,'wb')
        grand.write(bytes.fromhex(a))
        grand.close()
except:pass