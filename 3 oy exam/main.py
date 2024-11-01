# 1. while siklining ishlash tartibini tushuntirib bering?
# 2. List ma’lumot turidagi append() va expand() metodlari orasiddagi farq nimada?
# 3. Dict ma’lumot turida dict ichidagi ma’lum bir elementni o’chirishning qanday usullari mavjud?
# 4. For orqali sonlarni teskari tartibda chiqarish uchun nima qilish kerak?
# javoblar 

#1  while ni ishlashi shunday ,biz whilega 1 berib qoysak ishluradi tohtamasdan , while  1 or true or 2==2 : bolsa ishluradi faqat truda ishlidi lekin false bolsa ishlamidi ichigayam kirib otirmidi
# 2 append bu bir nechta malumot qoshib beradoi ba rost obyektni ozgartirmaydi a expand malumotni tekislab berad va indekslarni kengaytirib berad
# 3 dict ishidagi malumotlarni ochirish uchun =pop 
# 4 for ni teskari aylanish uchun kiritilgan sondan -1 gacham aylanadi va -1 qadamdan yuradi shunda teskari aylanadi

# amaliy vazifa
# Students nomli bo’sh dict yaratilsin. While True orqali shu dictga element qo’shish, elementni chiqarish, elementni yangilash va elementni o’chirish buyruqlari bo’lsin. Ya’ni whileni ichida savol nomli o’zgaruvchi inputda son qabul qiladi.

# savol = int(input(”””

# 1. Student qo’shish
# 2. Studentlarni chiqarish
# 3. Studentni chiqarish
# 4. Studentni o’chirish

# Buyruqlardan birini tanlang: “””)

# 1- vazifa:

# Agar savol 1ga teng bo’lsa, Students nomli dictga student_id ni kalit sifatida, uning ismi, familiyasi guruh nomini o’sha kalitning qiymat(value)i sifatida qo’shilsin.

# 2-vazifa:

# Agar savol 2ga teng bo’lsa, barcha studentlar ma’lumotlari tartib bilan chiqarilsin

# 3-vazifa:

# Agar savol 3ga teng bo’lsa, student_id so’ralsin va o’sha student_id ga qiymat sifada kiritilgan studentning ismi, familiyasi va guruh printga chiqarilsin

# 3-vazifa:

# Agar savol 4ga teng bo’lsa, student_id so’ralsin va o’sha studnet_id ga qiymat sifatida kiritilgan ma’lumotlar va o’sha student_id ga teng bo’lgan kalit ham dictdan o’chirib yuborilsin

studentlar = {
    1:{"ismi":"Muhammadaziz ",
   "familiyasi":"Shokirov ",
   "guruhini nomi":"insomnia "},
    2:{"ismi":"Begzod",
   "familiyasi":"umaraliyev",
   "guruhini nomi":"insomnia"},
    3:{"ismi":"Tolib",
   "familiyasi":"Gofurov",
   "guruhini nomi":"insomnia"},
    4:{"ismi":"Dilbek",
   "familiyasi":"axrorov",
   "guruhini nomi":"insomnia"}
              }
savol = int(input("enter number \n1. Student qo’shish \n2. Studentlarni chiqarish \n3. Studentni chiqarish \n4. Studentni o’chirish \n enter number: "))
print(savol)
if savol==1:
    inp1 = int(input("nima qilmoqchisiz \n 1:ismini qoshish\n 2:familiyani qoshish\n 3:guruh nomini qoshish\n"))
    if inp1==1:
      ismilari = input("ismini qoshing: ")
      studentlar[1]["ismi"]=ismilari
      print(studentlar)
    elif inp1==2:
      familiyasi = input("familiyasini  qoshing: ")
      studentlar[1]["familiyasi"]=familiyasi
      print(studentlar)
    elif inp1==3:
      guruhi = input("familiyasini  qoshing: ")
      studentlar[1]["guruhini nomi"]=guruhi
      print(studentlar)
elif savol ==2:
   for key,value in studentlar.items():
       print(key,value)
elif savol==3:
    inp2 = int(input("qaysi studentni cgiqarmoqchisiz: \n1 \n2 \n3 \n4\n enter number: "))
    if inp2==1:
      print(studentlar[1])
    elif inp2==2:
      print(studentlar[2])
    elif inp2==3:
      print(studentlar[3])
    elif inp2==4:
      print(studentlar[4])
elif savol==4:
    inp2 = int(input("qaysi studentni o'chirmoqchisiz: \n1 student \n2 student \n3 student \n4 student"))
    if inp2==1:
      studentlar.pop(1)
      print(studentlar)
    elif inp2==2:
       studentlar.pop(2)
       print(studentlar)
    elif inp2==3:
       studentlar.pop(3)
       print(studentlar)
    elif inp2==4:
       studentlar.pop(4)
       print(studentlar)
