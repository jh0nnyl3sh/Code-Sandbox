# 🐺 GÜN 43: Nesne Yönelimli (OOP) Siber İstihbarat Botu

Bu proje, Python'da Prosedürel Programlama (sadece `def` kullanımı) seviyesinden, **Nesne Yönelimli Programlama (OOP - Class/Object)** seviyesine geçiş yaptığımız 43. Gün operasyonudur. 

Sıradan bir ağ tarayıcı script'i, hafızası ve durumu (state) olan otonom bir "Siber Ajan" sınıfına (`ReconBot`) dönüştürülmüştür.

### 🎯 Projenin Amacı
Siber güvenlik araçları (Recon araçları) geliştirirken, aynı anda birden fazla hedefi taradığımızda verilerin (açık port listelerinin) birbirine karışmasını engellemek. Sınıf (Class) mimarisi sayesinde her hedefe özel, birbirinden tamamen izole "Klon Ajanlar" üretilmiştir.

### 🧠 Mimari Özellikler (Neler Öğrendik?)
* **`Class` (Fabrika Kalıbı):** Ajanların nasıl davranacağını belirleyen temel `ReconBot` şablonu çizildi.
* **`__init__` (İnşaatçı/Constructor):** Ajanın yaratıldığı an hedefini beynine kazıması sağlandı.
* **`self` (Kapsülleme/Encapsulation):** Her ajanın bulduğu açık portları dışarıdaki global bir listeye değil, sadece kendi cebine (`self.acik_portlar`) kaydetmesi sağlandı. Bu sayede nesneler arası veri izolasyonu (Memory Isolation) başarıldı.
* **Otonom Raporlama:** Ajanların dışarıdan parametre almadan, kendi iç hafızalarındaki veriyi kullanarak operasyon raporu sunması sağlandı.

### 🛠️ Kullanım

Projeyi çalıştırmak için terminalden şu komutu girin:
```bash
python recon_bot.py


💻 Beklenen Çıktı Örneği
Sistem, üretilen nesne (object) sayısı kadar hedefi bağımsız olarak tarar ve birbirine karışmayan raporlar sunar:

📊 scanme.nmap.org İÇİN İSTİHBARAT RAPORU
=============================================
[!] Sızma İçin Potansiyel Kapılar : [22]

📊 testphp.vulnweb.com İÇİN İSTİHBARAT RAPORU
=============================================
[!] Sızma İçin Potansiyel Kapılar : [80]