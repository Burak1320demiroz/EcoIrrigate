

# EcoIrrigate 🌱  
Samsung Innovation Campus eğitimi kapsamında düzenlenen hackathon için geliştirdiğim projeyi paylaşmaktan mutluluk duyuyorum. Bu proje, tarımsal sulama süreçlerini optimize etmek ve doğal kaynakları daha verimli kullanmak amacıyla tasarlanmıştır.

## Kullanılan Datasetler 📊

### 1. **yağış_oranları_mm.csv**
   - **Açıklama**: Türkiye'deki 81 ilin 12 aylık m² başına düşen yağmur miktarını (mm cinsinden) içerir. 
   - **Not**: Bu veri setini kendim hazırladım.

### 2. **su_ihtiyacları.csv**
   - **Açıklama**: Ekin türlerinin yetiştirildiği ortama göre gerekli su ihtiyacını belirler. Veriyi Türkçeye çevirerek Türkiye'ye uygun hale getirdim.
   - **Orijinal Dataset**: [Kaggle - Crop Water Requirement](https://www.kaggle.com/datasets/prateekkkumar/crop-water-requirement)

### 3. **dönem.csv**
   - **Açıklama**: Belirli ekin türlerinin ekim ve hasat dönemlerini içerir. Bu veri setini tamamen kendim hazırladım.

### 4. **şehirler.csv**
   - **Açıklama**: Türkiye'nin şehir bazında hava durumu, sıcaklık, toprak nemi ve bulunduğu bölge gibi bilgilerini içerir.
   - - **Not**: Bu veri setini kendim hazırladım.


## Yazılan Kodlar 💻

### 1. **water_tank.py**
   - **Açıklama**: 
     Şehir bilgisi ve yağmur hasadı yapılacak alanı (m² cinsinden) girerek, yıllık biriken su miktarını hesaplar.

### 2. **water_need.py**
   - **Açıklama**: 
     Ekin türünü, ekilecek hektar miktarını ve şehir bilgisini girdikten sonra; 12 aylık ve yıllık gerekli su miktarını çıktı olarak verir.

### 3. **water_amount.py**
   - **Açıklama**: 
     Yıllık biriken su miktarı ile yıllık ekin türüne bağlı gerekli su miktarını karşılaştırır ve durumu raporlar.


     ## Sunum 📑
### Samsung Innovation Campus hackathon projemi detaylı olarak anlattığım sunuma buradan ulaşabilirsiniz:

###👉 EcoIrrigate Sunumu: Proje ile ilgili tüm detaylar ve görseller için EcoIrrigate.pptx dosyasını inceleyebilirsiniz.


## Kaynaklar 📚
1. [Meteoroloji Genel Müdürlüğü (MGM)](https://www.mgm.gov.tr/)  
2. [Türkiye İstatistik Kurumu (TÜİK)](https://data.tuik.gov.tr/Kategori/GetKategori?p=tarim-111)  
3. [Kaggle - Crop Water Requirement](https://www.kaggle.com/datasets/prateekkkumar/crop-water-requirement)
