import openpyxl

# Excel dosyasını aç
workbook = openpyxl.load_workbook('deneme.xlsx')

# İlgili çalışma sayfasını seç (Varsayılan olarak ilk sayfa seçilir)
sheet = workbook.active

# B2 hücresine veri yaz
sheet['B2'] = 5

# Excel dosyasını kaydet
workbook.save('deneme.xlsx')
