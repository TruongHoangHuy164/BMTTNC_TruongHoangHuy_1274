def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1  # Sửa thụt dòng
    return count_dict  # Đưa return ra ngoài vòng lặp

# Nhập danh sách từ người dùng
input_string = input("Nhập danh sách các từ: ")
word_lst = input_string.split()

# Gọi hàm đếm số lần xuất hiện
slxh = dem_so_lan_xuat_hien(word_lst)

# In kết quả
print("Số lần xuất hiện:", slxh)
