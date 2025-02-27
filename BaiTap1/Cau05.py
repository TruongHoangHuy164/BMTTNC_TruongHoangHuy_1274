sogiolam =float(input("Nhap sgl moi tuan: "))
luonggio = float(input("Nhap thù lao tren moi gio lam tieu chuan: "))
giotieuchuan=44
giovuotchuan = max(0,sogiolam - giotieuchuan)
thuclinh = giotieuchuan * luonggio + giovuotchuan*luonggio*1.5
print(f"Thực lĩnh: {thuclinh}")