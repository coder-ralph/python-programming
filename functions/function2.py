# functions
def employeepay(hrswork, rateperhr, ratedduct):
    empnetpay = (hrswork * rateperhr) - ratedduct
    return empnetpay

epay = employeepay(10,800,250)
yearlyepay = epay * 12

print("salary for 12 months:%s" %(yearlyepay))