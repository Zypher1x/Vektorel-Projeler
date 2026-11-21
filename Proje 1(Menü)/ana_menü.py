print("╔════════════════════════════════╗")
print("║            ANA MENU            ║")
print("╠════════════════════════════════╣")
print("║   1-Oyunlar                    ║")
print("║   2-Çizimler                   ║")
print("║   3-Hesplamalar                ║")
print("║   4-Sosyal Medya               ║")
print("║   5-Çıkış                      ║")
print("╚════════════════════════════════╝")
seçim = input('Seçiminizi Giriniz:')
 
if seçim == '1':
    print('Oyunlar Menüsü Açılıyor...')
    import oyunlar

elif seçim == '2':
    print('Çizimler Menüsü Açılıyor...')
    import çizimler

elif seçim == '3':
    print('Hesaplamalar Menüsü Açılıyor...')
    import hesaplamalar

elif seçim == '5':
    print('Sosyal Medya Menüsü Açılıyor...')
    import sosyal_medya

elif seçim == '6':
    print('Çıkış Yapılıyor...')

else:
    print('Geçerli Bir Seçim Giriniz!')