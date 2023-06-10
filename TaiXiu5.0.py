import time
import random
with open('/storage/emulated/0/Download/CodingPython/B.txt','r') as file5:
 tien_goc = int(file5.read())
 file5.close
with open('/storage/emulated/0/Download/CodingPython/Vang.txt','r') as file6:
     vang = int(file6.read())
     file6.close
a = 0
while True:
 with open('/storage/emulated/0/Download/CodingPython/B.txt','w+') as file5:
     file5.write(str(tien_goc))
     file5.close
 g = 0
 while g < 50:
   g = g + 1
   print(" ")
 print("""     Tài Xỉu 5.0
 code by : Đức Chính 

""")
 print("bạn còn : "+ str(tien_goc)+" đồng trong tài khoản")
 print("bạn còn : "+ str(vang)+" vàng trong tài khoản")
 print("""1: Tài Xỉu Tiền
2: Tài Xỉu Vàng
3: Nạp tiền
4: Đổi tiền""")
 lua_chon = int(input("lựa chọn : "))
#Game
 if lua_chon == 1:
  l = 0
  while l < 5:
   with open('/storage/emulated/0/Download/CodingPython/B.txt','w+') as file5:
     file5.write(str(tien_goc))
     file5.close
   a1 = 0
   while a1 < 50:
    a1 += 1
    print(" ")
   print("số tiền của bạn còn : "+str(tien_goc)+" đồng")
   print("số vàng của bạn còn : "+str(vang)+" vàng")
   print("mức cược")
   print("""1 : 50k Tài    7 : 500k Tài
2 : 50k Xỉu    8 : 500k Xỉu
3 : 100k Tài   9 : 1000k Tài
4 : 100k Xỉu   10 : 1000K Xỉu
5 : 200k Tài
6 : 200k Xỉu""")
   muc_cuoc = int(input("nhập mức cược : "))
   az = 0
   tong_diem = 0
   while az < 3:
    az += 1
    cz = random.randint(1,6)
    tong_diem += cz
    time.sleep(0.4)
    print("Xúc Xắc "+str(az)+" : "+str(cz)) 
   print("tổng số điểm : "+str(tong_diem))
   if tong_diem <= 10:
      chon1 = -1
   if tong_diem > 10:
      chon1 = 1
   if muc_cuoc == 1:
      tien_cuoc = 50000
      chon = 1
   if muc_cuoc == 2:
      tien_cuoc = 50000
      chon = -1
   if muc_cuoc == 3:
      tien_cuoc = 100000
      chon = 1
   if muc_cuoc == 4:
      tien_cuoc = 100000
      chon = -1
   if muc_cuoc == 5:
      tien_cuoc = 200000
      chon = 1
   if muc_cuoc == 6:
      tien_cuoc = 200000
      chon = -1
   if muc_cuoc == 7:
      tien_cuoc = 500000
      chon = 1
   if muc_cuoc == 8:
      tien_cuoc = 500000
      chon = -1
   if muc_cuoc == 9:
      tien_cuoc = 1000000
      chon = 1
   if muc_cuoc == 10:
      tien_cuoc = 1000000
      chon = -1
   if chon1 == chon:
    if chon1 == 1:
       tien_goc = tien_goc + tien_cuoc
       time.sleep(0.2)
       print("Tài")
       print("Chúc Mừng Bạn Đã Thắng : "+str(tien_cuoc))
       print("Tổng số tiền của bạn là : "+str(tien_goc))
    if chon1 == -1:
       tien_goc = tien_goc + tien_cuoc
       print("Xỉu")
       print("Chúc Mừng Bạn Đã Thắng : "+str(tien_cuoc))
       print("Tổng số tiền của bạn là : "+str(tien_goc))
   if chon != chon1:
    if chon1 == 1:
       tien_goc = tien_goc - tien_cuoc
       time.sleep(0.2)
       print("Tài")
       print("Bạn Đã Mất : "+str(tien_cuoc))
       print("Tổng số tiền của bạn là : "+str(tien_goc))
    if chon1 == -1:
       tien_goc = tien_goc - tien_cuoc
       print("Xỉu")
       print("Bạn Đã Mất : "+str(tien_cuoc))
       print("Tổng số tiền của bạn là : "+str(tien_goc))
   with open('/storage/emulated/0/Download/CodingPython/B.txt','w+') as file5:
     file5.write(str(tien_goc))
     file5.close
   print("""1 : Có
2 : Không""")
   tiep_tuc = int(input("Tiếp Tục : "))
   if tiep_tuc == 1:
     l = 2
     b = 0
     while b < 50:
       b = b + 1
       print(" ")
   if tiep_tuc == 2:
     l = 6
#Tài Xỉu Vàng
 if lua_chon == 2:
  v = 0
  while v < 5:
   a1 = 0
   with open('/storage/emulated/0/Download/CodingPython/Vang.txt','r') as file6:
      vang = int(file6.read())
   while a1 < 50:
    file6.close
    a1 += 1
    print(" ")
   print("""Tài Xỉu Vàng
""")
   print("bạn hiện có : "+str(vang)+" vàng")
   print(" ")
   muc_vang = int(input("mời bạn nhập số vàng : "))
   print("""1: Tài
2: Xỉu


""")
   chon1 = int(input("Mời bạn chọn cầu : "))
   if chon1 == 1:
    cau = 1
   if chon1 == 2:
    cau = -1
   if muc_vang <= vang:
    vang = vang - muc_vang
    az = 0
    tong_diem = 0
    while az < 3:
     az += 1
     cz = random.randint(1,6)
     tong_diem += cz
     time.sleep(0.4)
     print("Xúc Xắc "+str(az)+" : "+str(cz)) 
    print("tổng số điểm : "+str(tong_diem))
    if tong_diem > 10:
     cau2 = 1
     print("""
    Tài
     """)
    if tong_diem <= 10:
     cau2 = -1
     print("""
    Xỉu
    """)
    if cau == cau2:
     print("Chúc mừng bạn đã thắng : "+str(muc_vang)+" vàng")
     vang += muc_vang+muc_vang
     print("bạn hiện có : "+str(vang)+" vàng")
     with open('/storage/emulated/0/Download/CodingPython/Vang.txt','w+') as file6:
      file6.write(str(vang))
      file6.close
    if cau != cau2:
      print("Chúc Bạn May Mắn Lần Sau")
      print("bạn hiện có : "+str(vang)+" vàng")
      with open('/storage/emulated/0/Download/CodingPython/Vang.txt','w+') as file6:
       file6.write(str(vang))
       file6.close
    print("""1: Tiếp Tục
2: Thoát""")
    lua_chon = int(input("nhập lựa chọn : "))
    if lua_chon == 1:
     v = 1
    if lua_chon == 2:
     v = 6
   else:
    print("""
    
    
    bạn không đủ số vàng""")
    time.sleep(5)
#Nạp Thẻ
 if lua_chon == 3:
  print("""     Nạp Thẻ
1: 50k
2: 100k
3: 200k
4: 500k""")
  nap_the = int(input("chọn mức nạp : "))
  k = 0
  if nap_the == 1:
   tien_goc = tien_goc + 50000
   while k < 50:
    k = k + 1
    print(" ")
   print("""nạp thẻ thành công
tài khoản bạn hiện có : """+ str(tien_goc))
   print("""


""")
  if nap_the == 2:
   tien_goc = tien_goc + 100000
   while k < 50:
    k = k + 1
    print(" ")
   print("""nạp thẻ thành công
tài khoản bạn hiện có : """+ str(tien_goc))
   print("""


""")
  if nap_the == 3:
   tien_goc = tien_goc + 200000
   while k < 50:
    k = k + 1
    print(" ")
   print("""nạp thẻ thành công
tài khoản bạn hiện có : """+ str(tien_goc))
   print("""


""")
  if nap_the == 4:
   tien_goc = tien_goc + 500000
   while k < 50:
    k = k + 1
    print(" ")
   print("""nạp thẻ thành công
tài khoản bạn hiện có : """+ str(tien_goc))
   print("""


""")
#Đổi tiền
 if lua_chon == 4:
   a = 0
   while a < 50:
    a = a + 1
    print(" ")
   with open('/storage/emulated/0/Download/CodingPython/Vang.txt','r') as file6:
     vang = int(file6.read())
     file6.close
   print("bạn hiện có : "+ str(tien_goc)+" đồng")
   print("bạn hiện có : "+ str(vang)+" vàng")
   print("ĐỔI TIỀN")
   print("""1 : đổi tiền ra vàng
2 : đổi vàng ra tiền""")
   doi_tien = int(input("mời bạn chọn : "))
   if doi_tien == 1:
    print("1 vàng = 1000000 đồng")
    tien_doi = int(input("nhập số vàng cần đổi : "))
    if tien_doi <= tien_goc:
     if tien_doi >= 1000000:
      vang = int(vang + (tien_doi/1000000))
      tien_goc = tien_goc - tien_doi
     else:
      print("""
    
    số tiền nhập không hợp lệ""")
      time.sleep(5)
    else:
     print("""
    
    
    bạn đã nhập quá số tiền bạn hiện có
    yêu cầu nạp thêm tiền vào tài khoản""")
     time.sleep(5)
    with open('/storage/emulated/0/Download/CodingPython/B.txt','w+') as file5:
     file5.write(str(tien_goc))
     file5.close
    with open('/storage/emulated/0/Download/CodingPython/Vang.txt','w+') as file6:
     file6.write(str(vang))
     file6.close
   if doi_tien == 2:
    print("1 vàng = 1000000 đồng")
    vang_doi = int(input("nhập số vàng cần đổi : "))
    if vang_doi <= vang:
     if vang_doi >= 1:
      tien_goc = int(tien_goc + (vang_doi*1000000))
      vang = vang - vang_doi
     else:
      print("""
    
    số tiền nhập không hợp lệ""")
      time.sleep(5)
    else:
     print("""
    
    
    bạn đã nhập quá số vàng bạn hiện có
    yêu cầu đổi thêm vàng """)
     time.sleep(5)
    with open('/storage/emulated/0/Download/CodingPython/B.txt','w+') as file5:
     file5.write(str(tien_goc))
     file5.close
    with open('/storage/emulated/0/Download/CodingPython/Vang.txt','w+') as file6:
     file6.write(str(vang))
     file6.close
     
   