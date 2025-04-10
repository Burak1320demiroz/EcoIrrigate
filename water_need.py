import pandas as pd
import matplotlib.pyplot as plt

şehirler = pd.read_csv("şehirler.csv")
su_ihtiyacları = pd.read_csv("su_ihtiyacları.csv")
donem = pd.read_csv("donem.csv")

şehirler.columns = şehirler.columns.str.strip()
su_ihtiyacları.columns = su_ihtiyacları.columns.str.strip()
donem.columns = donem.columns.str.strip()

def get_monthly_water_requirements_updated():
    crop_type = input("Ekilecek ürün türü ==> ").strip()
    city = input("Şehir adı ==> ").strip()
    area_hectares = float(input("Ekilen alan (hektar) ==> "))

    filtered_crop_data = su_ihtiyacları[su_ihtiyacları['EKİN TÜRÜ'] == crop_type]
    if filtered_crop_data.empty:
        print("Girdiğiniz ekin türüne uygun su ihtiyacı verisi bulunamadı.")
        return None  

    filtered_period = donem[donem['ÜRÜN'] == crop_type]
    if filtered_period.empty:
        print("Girdiğiniz ürün için dönem verisi bulunamadı.")
        return None

    try:
        valid_months = filtered_period['AYLAR'].values[0].split()
    except KeyError:
        print("'AYLAR' sütunu bulunamadı. Lütfen CSV dosyasını kontrol edin.")
        return None

    total_annual_water_requirement = 0
    months = []
    monthly_water_requirements = []

    city_weather_data = şehirler[şehirler['Şehir'] == city]
    if city_weather_data.empty:
        print(f"Girdiğiniz {city} şehri için hava durumu verisi bulunamadı.")
        return None

    for _, row in city_weather_data.iterrows():
        month = row['Ay']
        soil_type = row['Toprak Türü']
        region = row['Bölge']
        temperature = row['Sıcaklık']
        weather_condition = row['Hava Durumu']

        if month not in valid_months:
            monthly_water_requirements.append(0)
        else:
            condition = (
                (filtered_crop_data['TOPRAK TİPİ'] == soil_type) &
                (filtered_crop_data['BÖLGE'] == region) &
                (filtered_crop_data['SICAKLIK'] == temperature) &
                (filtered_crop_data['HAVA DURUMU'] == weather_condition)
            )
            water_requirement_row = filtered_crop_data[condition]

            if water_requirement_row.empty:
                print(f"{month} ayında {city} şehri için eşleşen su ihtiyacı verisi bulunamadı.")
                monthly_water_requirements.append(0)
            else:
                monthly_water_requirement = water_requirement_row['SU İHTİYACI'].values[0] * 30 
                monthly_water_requirements.append(monthly_water_requirement)
                total_annual_water_requirement += monthly_water_requirement

        months.append(month)
        print(f"{month} ayında {city} için aylık su ihtiyacı: {monthly_water_requirements[-1]:.2f} m³")

    total_annual_water_requirement_hectares = total_annual_water_requirement * area_hectares  

    print(f"Yıllık toplam su ihtiyacı ({area_hectares} hektar): {total_annual_water_requirement_hectares:.2f} m³")

    plt.figure(figsize=(10, 6))
    plt.plot(months, monthly_water_requirements, marker='o', linestyle='-', color='b')
    plt.title(f"{city} şehri için {crop_type} ürününün Aylık Su İhtiyacı ({area_hectares} Hektar)", fontsize=14)
    plt.xlabel("Ay", fontsize=12)
    plt.ylabel("Su İhtiyacı (m³)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return months, monthly_water_requirements, total_annual_water_requirement_hectares
total_water_requirement = get_monthly_water_requirements_updated()
