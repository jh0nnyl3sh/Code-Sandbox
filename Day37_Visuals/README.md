
# 🐺 Project Cerberus: The Data Storyteller (Visual Intelligence)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Data](https://img.shields.io/badge/Data-Matplotlib-orange)
![Architecture](https://img.shields.io/badge/Architecture-Data_Viz-success)

**Project Cerberus - Faz 2 (Veri Analizi ve Görsel İstihbarat)**

Bu modül, ham veri yığınlarını (Excel/JSON) saniyeler içinde karar alıcıların (Yöneticiler, Komisyonlar, SOC Analistleri) anlayabileceği yüksek çözünürlüklü görsel grafiklere dönüştüren otonom bir raporlama motorudur.

## 📊 Operasyon Detayı

Script, geçmiş projelerde simüle edilen "Dosya Tevzi Sistemi" verilerini alır, `Pandas` ile işler ve `Matplotlib` kullanarak kurumsal standartlarda bir "Bar Chart" (Çubuk Grafiği) inşa eder. 

### 🛠️ Teknik Nitelikler (Architecture)
* **Otomasyon Odaklı Çıktı:** Grafikler ekranda manuel olarak açılıp sistemi bekletmez (`plt.show()` kullanılmaz). Arka planda sessizce yüksek çözünürlüklü (`dpi=300`) PNG dosyaları olarak sisteme kaydedilir (`plt.savefig()`).
* **Kurumsal Tasarım:** Hex renk kodları, eksen isimlendirmeleri (labels) ve grid (ızgara) sistemleri ile yönetici sunumlarına (C-Level) hazır, temiz ve profesyonel bir arayüz.
* **OPSEC (Güvenlik):** Üretilen görsel raporlar ve medya dosyaları (`*.png`, `*.jpg`, `*.pdf`) `.gitignore` kalkanı ile versiyon kontrol sisteminden (GitHub) izole edilmiştir.

## 📦 Kurulum ve Çalıştırma

**1. Gereksinimleri Yükleyin:**
```bash
pip install pandas matplotlib
2. Operasyonu Başlatın:

Bash
python visualizer.py
Engineered by Jhonny Lesh 🤠
