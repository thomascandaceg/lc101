def get_initials(fullname):
    newList = fullname.split()
    initials = ""

    for i in newList:      
        initials = initials + i[0]
    return(initials.upper())

