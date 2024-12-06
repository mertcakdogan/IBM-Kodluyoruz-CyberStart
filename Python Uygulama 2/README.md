# Öklid Mesafesi Hesaplayıcı

Bu repo IBM ile Kodluyoruz: CyberStart programı için Python Uygulama 2 Minimum Öklid Mesafesinin Hesaplanması projesi için hazırlanmıştır.

Bu Python programı, verilen noktalar kümesi için Öklid mesafelerini hesaplayıp minimum mesafeyi bulur.

## Nasıl Çalışır?

1. **Noktaların Tanımlanması**: `points` adında bir liste oluşturulur ve bu listeye 2D uzaydaki noktalar temsil eden demetler (x, y) eklenir.

    ```python
    points = [(1, 2), (4, 6), (7, 1), (3, 3), (5, 8)]
    ```

2. **Öklid Mesafesi İçin Bir Fonksiyon Yazma**: `euclideanDistance` adında bir fonksiyon tanımlanır. Bu fonksiyon, iki nokta temsil eden demet alır ve bu iki nokta arasındaki Öklid mesafesini hesaplayıp döndürür.

    ```python
    def euclideanDistance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    ```

3. **Mesafelerin Hesaplanması**: Bir `for` döngüsü kullanılarak, `points` listesindeki her nokta çifti arasındaki Öklid mesafesi hesaplanır ve `distances` adındaki başka bir listede saklanır.

    ```python
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append(distance)
    ```

4. **Minimum Mesafenin Bulunması**: `distances` listesinden minimum mesafe `min()` fonksiyonu ile bulunur.

    ```python
    min_distance = min(distances)
    ```

5. **Sonuçların Yazdırılması**: Noktalar, hesaplanan mesafeler ve bulunan minimum mesafe ekrana yazdırılır.

    ```python
    print("Noktalar:", points)
    print("Mesafeler:", distances)
    print("Minimum Mesafe:", min_distance)
    ```

## Nasıl Kullanılır?

1. Python dosyasını çalıştırın.
2. Programın çıktısını inceleyin:
    - Noktalar listesi
    - Hesaplanan mesafeler listesi
    - Bulunan minimum mesafe

## Özet

Bu program, 2D uzaydaki noktalar arasındaki Öklid mesafelerini hesaplar ve minimum mesafeyi bulur. Noktaların tanımlanması, mesafe hesaplama fonksiyonunun yazılması, mesafelerin listelenmesi ve minimum mesafenin bulunması adımlarından oluşur.