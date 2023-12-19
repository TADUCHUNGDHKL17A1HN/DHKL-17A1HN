# bài 9.1
def tinh_nam_am_lich(nam_duong_lich):
    can = ["Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm"]
    chi = ["Hợi", "Tí", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất"]

    can_index = (nam_duong_lich - 4) % 10
    chi_index = (nam_duong_lich - 4) % 12

    nam_am_lich = "{} {}".format(can[can_index], chi[chi_index])

    return nam_am_lich

# Ví dụ sử dụng hàm
nam_duong_lich = 2023
nam_am_lich = tinh_nam_am_lich(nam_duong_lich)

print("Năm âm lịch tương ứng với năm {} là: {}".format(nam_duong_lich, nam_am_lich))
