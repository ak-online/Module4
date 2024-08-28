def divide(first, second):
    if second == 0:
        return "Error"
    else :
        res = round(first / second,2)
        return res
#end of divide

#print(divide(1,0))