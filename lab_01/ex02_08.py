def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
chuoi_so_nhi_phan = input("Nhập chuỗi số nhi phân (phân tách bởi dấu phẩy): ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_nam = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]
if len(so_chia_het_cho_nam) > 0:
    ket_qua = ','.join(so_chia_het_cho_nam)
    print("Các số nhị phân chia hết cho 5 la:", ket_qua)

else:
    print("Không có sô nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")    