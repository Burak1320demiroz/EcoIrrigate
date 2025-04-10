import pandas as pd
import matplotlib.pyplot as plt

def su_toplama_hesapla(yagis_mm, alan_m2, verimlilik=0.8):
    yagis_m = yagis_mm / 1000  
    toplanan_su_m3 = yagis_m * alan_m2
    kullanilabilir_su_m3 = toplanan_su_m3 * verimlilik
    return kullanilabilir_su_m3

def bursa_yagis_verisini_al():
    df = pd.read_csv('yagıs_oranları_mm.csv')
    df.columns = df.columns.str.strip()  
    return df

bursa_yagis_df = bursa_yagis_verisini_al()

def su_toplama_hesapla_ve_toplam_su_hesapla(sehir, alan_boyutu):
    toplam_su = 0  
    aylik_su = [] 
    aylik_aylar = []  

    if sehir == "Bursa":
        print(f"{sehir} için aylık yağış miktarları: ")

        for index, row in bursa_yagis_df.iterrows():
            ay = row['Ay']
            yagis_miktari = row['Yağış (mm)']
            birikmis_su = su_toplama_hesapla(yagis_miktari, alan_boyutu)
            toplam_su += birikmis_su  

            aylik_su.append(birikmis_su)
            aylik_aylar.append(ay)

            print(f"{ay}: {birikmis_su:.2f} m³")

        print(f"\nToplam birikmiş su miktarı: {toplam_su:.2f} m³")
    else:
        print("Bu şehir veritabanımızda bulunmamaktadır.")

    return aylik_aylar, aylik_su, toplam_su


sehir = input("Lütfen şehri girin: ")
alan_boyutu = float(input("Lütfen su toplama alanının büyüklüğünü (m² cinsinden) girin: "))
aylik_aylar, aylik_su, toplam_su = su_toplama_hesapla_ve_toplam_su_hesapla(sehir, alan_boyutu)

plt.figure(figsize=(10, 6))
plt.bar(aylik_aylar, aylik_su, color='blue', alpha=0.7, label='Aylık Su Miktarı (m³)')
plt.plot(aylik_aylar, [sum(aylik_su[:i+1]) for i in range(len(aylik_su))], color='red', marker='o', label='Toplam Birikmiş Su (m³)')
plt.title(f"{sehir} İçin Aylık Su Toplama ve Toplam Su Miktarı", fontsize=14)
plt.xlabel("Aylar", fontsize=12)
plt.ylabel("Su Miktarı (m³)", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
