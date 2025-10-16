name = input("tên học sinh: ")
score = float(input("điểm trung bình: "))
if not 0.0 <= score <= 10.0:
    print("Điểm không hợp lệ")
elif score >= 8.0 and ("A" or "a") in name:
    print("Xuất sắc")
elif score >= 9.0:
    print("Xuất sắc")
elif score >= 8.0:
    print("Giỏi")
elif score >= 6.0:
    print("Khá")
elif score >= 5.0:
    print("Trung bình")
else:
    print("Yếu")