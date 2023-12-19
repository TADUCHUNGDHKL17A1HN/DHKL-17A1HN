def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/(chieu_cao*chieu_cao)
    if bmi < 18.5:
        print("chỉ số bmi cua bạn là", bmi ,"(gầy)")
    elif (bmi>=18.5 and bmi<=24.99):
        print("chỉ số bmi của bạn là", bmi ," (bình thường)" )
    else:
        print("chỉ số bmi của bạn là", bmi ,"(thừa cân)" )
    return bmi
w=float(input("cho biết cân nặng của bạn :"))
h=float(input("cho biết chiều cao của bạn :"))
tinh_bmi(can_nang=w,chieu_cao=h)