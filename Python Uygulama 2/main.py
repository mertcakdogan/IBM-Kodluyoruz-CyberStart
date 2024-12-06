# 1. Noktaların Tanımlanması
points = [(1, 2), (4, 6), (7, 1), (3, 3), (5, 8)]

# 2. Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 3. Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonuçların Yazdırılması
print("Noktalar:", points)
print("Mesafeler:", distances)
print("Minimum Mesafe:", min_distance)
