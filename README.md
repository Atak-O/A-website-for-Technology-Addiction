# #Teknoloji Bagimliligindan Kurtul

Bu proje, teknoloji bagimliligi konusunda farkindalik olusturmak icin hazirlanmis basit bir Flask web sitesidir. Site, kullanicilara teknoloji bagimliliginin ne oldugunu, gunluk hayata etkilerini ve farkli turlerini anlatir.

Proje hem bilgilendirici hem de etkilesimli olacak sekilde tasarlanmistir. Kullanici ana sayfada konu hakkinda bilgi okuyabilir, rastgele bir gercek gorebilir, rastgele bir resim acabilir ve kisa bilmecelerle sayfayi daha eglenceli sekilde kullanabilir.

## Projenin Amaci

Teknoloji gunluk hayatin onemli bir parcasi olsa da asiri ve kontrolsuz kullanim bazi sorunlara yol acabilir. Bu web sitesi, teknoloji bagimliligi hakkinda temel bilgiler vererek kullanicilarin bu konuda dusunmesini saglamayi amaclar.

## Sitede Neler Var?

Ana sayfada teknoloji bagimliliginin tanimi, etkileri ve farkli turleri yer alir. Kullanici buradan farkli bolumleri okuyarak sosyal medya, akilli telefon, oyun ve internet alisverisi gibi konular hakkinda bilgi edinebilir.

Sitede ayrica uc etkilesimli sayfa bulunur:

- Rastgele bilgi sayfasi, teknoloji kullanimiyla ilgili farkli bilgiler gosterir.
- Rastgele resim sayfasi, her acildiginda farkli bir resim gosterir.
- Bilmece sayfasi, kullaniciya kisa bir bilmece ve cevabini sunar.

Bu ozellikler sayesinde site sadece bilgi veren bir sayfa olmaktan cikar ve kullanicinin farkli sayfalari denemesini saglar.

## Kullanilan Teknolojiler

Bu proje Python programlama dili ve Flask web framework'u kullanilarak gelistirilmistir. Sayfa icerigi HTML ile hazirlanmis, gorunum ise CSS ile duzenlenmistir.

## Kurulum

Projeyi calistirmak icin bilgisayarinizda Python ve Flask kurulu olmalidir.

Pipenv kullaniyorsaniz:

```bash
pipenv install
pipenv shell
python main.py
```

Pipenv kullanmiyorsaniz:

```bash
pip install flask
python main.py
```

## Kullanim

Uygulamayi baslattiktan sonra tarayicida su adrese giderek ana sayfayi acabilirsiniz:

```text
http://127.0.0.1:5000/
```

Sayfalar:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/bilgiler`
- `http://127.0.0.1:5000/resim`
- `http://127.0.0.1:5000/bilmece`

## Sonuc

Bu web sitesi, teknoloji bagimliligi hakkinda temel bilgiler sunan ve basit etkilesimli ozelliklerle desteklenen bir Flask projesidir. Proje, web sayfalarina yeni route ekleme, HTML sayfasi hazirlama ve CSS ile stil verme konularini uygulamak icin hazirlanmistir.
