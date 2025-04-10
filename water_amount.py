total_water_requirement = total_water_requirement[2]

def compare_water_requirements(toplam_su, total_water_requirement):

    if toplam_su > total_water_requirement:
        message = f"Depodaki su yeterli. (Depodaki su: {toplam_su:.2f} m³, Gerekli su: {total_water_requirement:.2f} m³)"
    elif toplam_su < total_water_requirement:
        message = f"Depodaki su yetersiz. (Depodaki su: {toplam_su:.2f} m³, Gerekli su: {total_water_requirement:.2f} m³)"
    else:
        message = f"Depodaki su, gereken miktar ile eşit. (Depodaki su: {toplam_su:.2f} m³, Gerekli su: {total_water_requirement:.2f} m³)"

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(['Depodaki Su', 'Gerekli Su'], [toplam_su, total_water_requirement], color=['blue', 'red'])
    ax.set_title(f"Su İhtiyacı Karşılaştırması: {message}", fontsize=14)
    ax.set_ylabel("Su Miktarı (m³)", fontsize=12)
    ax.set_ylim(0, max(toplam_su, total_water_requirement) * 1.2)   
    plt.tight_layout()
    plt.show()

    return message

result = compare_water_requirements(toplam_su, total_water_requirement)
print(result)
