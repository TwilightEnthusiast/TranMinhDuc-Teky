x=float(input("Nhập cân nặng của bạn tính theo kg: "))
y=float(input("Nhập cân nặng của bạn tính theo mét: "))
if x/y^2<16:
    print("Gầy cấp độ 3")   
elif x/y^2<17:
    print("Gầy cấp độ 2") 
elif x/y^2<18.5:
    print("Gầy cấp độ 1") 
elif x/y^2<25:
    print("Bình thường")
elif x/y^2<30:
    print("thằng béo")
elif x/y^2<35:
    print("thằng béo cấp độ 1")
elif x/y^2<40:
    print("thằng béo cấp độ 2")
else:
    print("thằng béo cấp độ 3")
    
