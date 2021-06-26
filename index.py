from market import api
tr = 'false'
print(api.news())
while(tr != 'true'):
    action = input("\nDe quelle action voulez avoir les informations ?\n")
    if(action == 'news'):
        print(api.news())
    else:   
        if(action != 'end'):
            act = api.all(action)
            print("\n" + act)
        else:
            tr = 'true'
            print("\nFin")