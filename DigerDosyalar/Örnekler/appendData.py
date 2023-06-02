def virgul_ekleyen_fonksiyon(deger, dosya_yolu):
    try:
        with open(dosya_yolu, 'a') as dosya:
            dosya.write(str(deger) + ',')
        print("Değer başarıyla dosyaya eklendi.")
    except IOError:
        print("Dosya bulunamadı veya açılamadı.")

# Örnek kullanım:
# virgul_ekleyen_fonksiyon(42, 'basinc.txt')
