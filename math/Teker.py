import math
import matplotlib.pyplot as plt

class AutonomousSteeringControl:
    def __init__(self):
        # Direksiyon turu ve tekerlek açısı ilişkisi
        self.max_steering_wheel_turns = 1.4  # Direksiyonun maksimum tur sayısı
        self.max_wheel_angle = 30  # Maksimum tekerlek açısı derece cinsinden
        self.degrees_per_turn = self.max_wheel_angle / self.max_steering_wheel_turns # 1 direksiyon turu başına düşen tekerlek açısı

    def calculate_steering_angle(self, current_position, target_position, current_yaw):
        delta_x = target_position[0] - current_position[0]
        delta_y = target_position[1] - current_position[1]
        distance = (delta_x ** 2 + delta_y ** 2) ** 0.5 # Hedefe Olan Mesafeyi Hesaplama
        print(f"Başlangiç ve hedef arasi uzaklik: {distance}")
        target_angle = math.atan2(delta_y, delta_x) # Hedef yönü açısını hesapla
        print(f"Hedef Yönü Acisi: {math.degrees(target_angle)} derece")
        steering_angle = target_angle - current_yaw # Direksiyon açısını hesapla
        print(f"Direksiyon Açısı (Ham): {math.degrees(steering_angle)} derece")
        # Direksiyon açısını -180 ile 180 derece arasında normalize et
        steering_angle = (steering_angle + math.pi) % (2 * math.pi) - math.pi
        steering_angle_degrees = math.degrees(steering_angle)
        print(f"Direksiyon Açısı (Normalize): {steering_angle_degrees} derece")
        return steering_angle_degrees

    def calculate_pwm_and_wheel_angle(self, steering_angle):
        # Direksiyon açısının büyüklüğüne göre PWM değeri ve tekerlek açısı hesapla
        pwm_base = 128  # Orta nokta
        pwm_range = 127  # PWM aralığı (127 sola, 128-255 sağa)
        max_steering_angle = self.max_wheel_angle  # Maksimum tekerlek açısı derece cinsinden
        wheel_angle = min(max(steering_angle, -max_steering_angle), max_steering_angle) # Tekerlek açısını direksiyon açısına göre hesapla
        steering_wheel_turns = wheel_angle / self.degrees_per_turn # Direksiyonun kaç tur döndüğünü hesapla

        if steering_angle < 0:  # Sola dönüş
            pwm_value = pwm_base - int((abs(steering_wheel_turns) / self.max_steering_wheel_turns) * pwm_range)
            pwm_value = max(0, pwm_value)  # PWM sınırları içerisinde kalma

        elif steering_angle > 0:  # Sağa dönüş
            pwm_value = pwm_base + int((abs(steering_wheel_turns) / self.max_steering_wheel_turns) * pwm_range)
            pwm_value = min(255, pwm_value)  # PWM sınırları içerisinde kalma

        else:  # Düz gidiyorsa
            pwm_value = pwm_base  # Orta konumda, direksiyon düz
        
        print(f"Hesaplanan PWM Değeri: {pwm_value}")
        print(f"Tekerlek Açisi: {wheel_angle} derece, Direksiyon Turu: {steering_wheel_turns} tur")
        return pwm_value, wheel_angle
        
# Sınıfı başlat ve örnek bir hesaplama yap
control = AutonomousSteeringControl()
current_position = (0, 0)
target_position = (-4, 4)
current_yaw = 0

steering_angle = control.calculate_steering_angle(current_position, target_position, current_yaw)
pwm, wheel_angle = control.calculate_pwm_and_wheel_angle(steering_angle)

# Görselleştirme
plt.figure()
delta_x = target_position[0] - current_position[0]
delta_y = target_position[1] - current_position[1]

# Aracın mevcut yönünü gösteren vektör
yaw_x = math.cos(current_yaw)
yaw_y = math.sin(current_yaw)

plt.quiver(current_position[0], current_position[1], delta_x, delta_y, angles='xy', scale_units='xy', scale=1, color='r', label="Hedef Yönü") # Hedef yönünü gösteren vektör
plt.quiver(current_position[0], current_position[1], yaw_x, yaw_y, angles='xy', scale_units='xy', scale=1, color='b', label="Mevcut Yön (Yaw)") # Mevcut yön (yaw) vektörü

# Tekerlek açısını gösteren vektör
wheel_angle_rad = math.radians(wheel_angle)
wheel_x = math.cos(current_yaw + wheel_angle_rad)
wheel_y = math.sin(current_yaw + wheel_angle_rad)

plt.quiver(current_position[0], current_position[1], wheel_x, wheel_y, angles='xy', scale_units='xy', scale=1, color='g', label="Tekerlek Açısı")
plt.plot(current_position[0], current_position[1], 'bo', label="Mevcut Pozisyon")
plt.plot(target_position[0], target_position[1], 'go', label="Hedef Pozisyon")
plt.xlim(-30, 30)
plt.ylim(-30, 30)
plt.xlabel('X Koordinatı')
plt.ylabel('Y Koordinatı')
plt.title(f"Direksiyon Açısı: {steering_angle} derece, PWM: {pwm}, Tekerlek Açısı: {wheel_angle} derece")
plt.grid(True)
plt.legend()
plt.show()
