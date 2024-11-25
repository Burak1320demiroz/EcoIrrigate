Samsung Innovation Campus eğitimine katılarak aldığım eğitim sonu süzenlenen hackathon projemi sizinle paylaşmaktan mutluluk duyarım. 

kullandıgım datasetler:
yagıs_oranları_mm.csv : türkiyedeki 81 ilin 12 aylık m^2 başına düşen yağmur bilgisi var mm cinsinden. data setini kendim hazırladım ve kullandığım kaynak  :  https://www.mgm.gov.tr/
su_ihtiyacları.csv : ekin türlerinin yetiştirildiği ortama göre gerekli su ihtiyacını belirlediğimiz dataset. data seti türkçeye cevirip türkiyeye uygun hale getirdim orjinal dataset  :  https://www.kaggle.com/datasets/prateekkkumar/crop-water-requirement
donem.csv : belirlenen ekim türlerinin ekilme ve hasat dönemlerini önerilen dataset. kendi hazırladığım bi dataset hazırlarken kullandığım kaynak  :
şehirler.csv : türkiye şehirlerin hava durumu, sıcaklık, toprak nemi, bulunduğu bölge gibi bilgileri iceren dataset. kendim hazırladığım bir dataset ve kullandığım kaynak  :  https://www.mgm.gov.tr/ , https://data.tuik.gov.tr/Kategori/GetKategori?p=tarim-111

yazdıgım kodlar:
water_tank.py : şehir bilgisi ve yagmur hasadı yapıcagımız alan (m^2) cinsinden girerek yıllık biriken suyu öğreniyoruz.
water_need.py : ekin türünü, ekilicek hektar ve şehir bilgisini girdi oralara verdiğimiz ; 12 aylık ve yıllık gerken su miktarını cıktı olarak aldığımız kısım.
water_amount.py : yıllık gereken su ile yıllık biriken suyu karşılaştırdığımız kısım 
