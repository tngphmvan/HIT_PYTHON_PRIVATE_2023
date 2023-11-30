import math as math


def doc_toa_do(file_input):
    # Mở tệp input.txt
    with open(file_input, "r") as f:
        # Lấy toàn bộ nội dung của tệp
        data = f.read()
        # Phân tách dữ liệu thành 2 phần, phần đầu là tên điểm A, phần sau là tọa độ của điểm B
        data_split = data.split(" ")
        # Lấy tọa độ x của điểm A
        x_a = float(data_split[1])
        # Lấy tọa độ y của điểm A
        y_a = float(data_split[2])
        # Lấy tọa độ x của điểm B
        x_b = float(data_split[4])
        # Lấy tọa độ y của điểm B
        y_b = float(data_split[5])
    return x_a, y_a, x_b, y_b


# Hàm tính khoảng cách giữa 2 điểm


def tinh_khoang_cach(x1, y1, x2, y2):
    # Tính khoảng cách theo công thức Pythogoras
    khoang_cach = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # Làm tròn đến số thập phân thứ 2
    khoang_cach = round(khoang_cach, 2)
    return khoang_cach

# Hàm ghi kết quả ra tệp output.txt


def ghi_ket_qua(file_output, x_a, y_a, x_b, y_b, khoang_cach):
    # Mở tệp output.txt
    with open(file_output, "w") as f:
        # Ghi tọa độ điểm A
        f.write("A(%.2f, %.2f)\n" % (x_a, y_a))
        # Ghi tọa độ điểm B
        f.write("B(%.2f, %.2f)\n" % (x_b, y_b))
        # Ghi khoảng cách AB
        f.write("AB = %.2f\n" % khoang_cach)


# Chạy chương trình
if __name__ == "__main__":
    # Tọa độ 2 điểm
    x_a, y_a, x_b, y_b = doc_toa_do("input.txt")
    # Khoảng cách AB
    khoang_cach = tinh_khoang_cach(x_a, y_a, x_b, y_b)
    # Ghi kết quả ra tệp output.txt
    ghi_ket_qua("output.txt", x_a, y_a, x_b, y_b, khoang_cach)
