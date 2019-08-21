def meeting(s):
    string = s.replace(";",' ').replace(":", ",").upper()
    names = string.split(" ")
    result = []
    for name in names:
        namebank = []
        namebank = name.split(',')
        flippedname = namebank[1] + ', ' + namebank[0]
        result.append(flippedname)
    result.sort()
    meetings = ""

    ### could adjust to return list instead of string ###
    for word in result:
        meetings += ("("+word+")")
    return meetings