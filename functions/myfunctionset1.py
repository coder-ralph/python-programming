def greetme(myname):
    print('hello %s. good pm' %(myname))
    print("how are you %s" %(myname))
    print(showcompanynumber())

def employeepay(hrswork, rateperhr, ratedduct):
    empnetpay = (hrswork * rateperhr) - ratedduct
    return empnetpay

def showcompanynumber():
    return "98877665544"