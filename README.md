# AI Research Assistant 🤖

Yapay zeka destekli araştırma asistanı. Web araması ve Wikipedia entegrasyonu ile kullanıcı sorularına kapsamlı yanıtlar üretir.

## Özellikler ✨

- 🔍 **Web Araması**: DuckDuckGo ile güncel bilgilere erişim
- 📚 **Wikipedia Entegrasyonu**: Detaylı ansiklopedik bilgiler
- 🤖 **AI Özetleme**: Google Gemini 2.5 Flash ile akıllı yanıt üretimi
- 💾 **Kayıt Sistemi**: Araştırma sonuçlarını dosyaya kaydetme
- 🎯 **Odaklanmış Yanıtlar**: Kısa ve öz, madde işaretli açıklamalar

## Kurulum 📦

### Gereksinimler

- Python 3.13+ (önerilir - Python 3.9 ile uyumluluk sorunları yaşanabilir)
- Google Gemini API anahtarı ([buradan alabilirsiniz](https://makersuite.google.com/app/apikey))

### Adımlar

1. **Projeyi klonlayın**
```bash
git clone https://github.com/ibb-git-demo/ai-research-assistant.git
cd ai-research-assistant
```

2. **Sanal ortam oluşturun** (önerilir)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Bağımlılıkları yükleyin**
```bash
pip install -r requirements.txt
```

4. **API anahtarını yapılandırın**

`.env` dosyasını düzenleyin ve Gemini API anahtarınızı ekleyin:
```env
GEMINI_API_KEY="your-api-key-here"
```

## Kullanım 🚀

Uygulamayı başlatın:
```bash
python main.py
```

### Örnek Kullanım

```
🤖 AI Research Assistant
Type 'quit' to exit

What can I help you research? Python programlama dili nedir?

🔍 Searching the web...
📚 Checking Wikipedia...
🤖 Generating summary...

✨ Summary:
• Python, 1991 yılında Guido van Rossum tarafından geliştirilen yüksek seviyeli bir programlama dilidir
• Okunabilir sözdizimi ve dinamik tip sistemine sahiptir
• Web geliştirme, veri analizi, yapay zeka gibi birçok alanda kullanılır
...
```

Çıkmak için `quit`, `exit` veya `q` yazın.

## Proje Yapısı 📁

```
.
├── main.py              # Ana uygulama dosyası
├── tools.py             # Araç tanımlamaları (arama, wiki, kayıt)
├── requirements.txt     # Python bağımlılıkları
├── .env                 # API anahtarı yapılandırması
└── research_output.txt  # Araştırma sonuçları (otomatik oluşturulur)
```

## Araçlar 🛠️

### `search_tool`
DuckDuckGo üzerinden web araması yapar (5 sonuç)

### `wiki_tool`
Wikipedia'dan bilgi alır (2 makale, maksimum 1000 karakter)

### `save_tool`
Araştırma sonuçlarını zaman damgalı olarak dosyaya kaydeder

## Yapılandırma ⚙️

### LLM Modeli Değiştirme

`main.py` dosyasında model ismini değiştirebilirsiniz:
```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # veya "gemini-pro"
    google_api_key=api_key
)
```

### Arama Sonuç Sayısı

`tools.py` dosyasında `max_results` parametresini ayarlayın:
```python
search_wrapper = DuckDuckGoSearchAPIWrapper(max_results=5)
```

## Notlar 📝

- Yanıtlar maksimum 300 kelime ile sınırlandırılmıştır
- Sadece arama sonuçlarındaki bilgiler kullanılır, modelin genel bilgisi değil
- Internet bağlantısı gereklidir

## Sorun Giderme 🔧

**Python 3.9 uyumluluk sorunu:**
```bash
# Python 3.13 veya üstü kullanın
python --version  # 3.13 veya üstü olmalı
```

**DuckDuckGo kurulu değil hatası:**
```bash
pip install duckduckgo-search
```

**API anahtarı hatası:**
- `.env` dosyasının doğru konumda olduğundan emin olun
- API anahtarının geçerli olduğunu kontrol edin

**Bağımlılık hataları:**
```bash
pip install --upgrade -r requirements.txt
```

## Lisans 📄

MIT License

## Katkıda Bulunma 🤝

Pull request'ler memnuniyetle karşılanır. Büyük değişiklikler için lütfen önce bir issue açarak neyi değiştirmek istediğinizi tartışın.

---

**Not**: Bu proje eğitim amaçlıdır. Üretim ortamında kullanmadan önce hata yönetimi ve güvenlik önlemlerini güçlendirin.