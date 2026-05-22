from flask import Flask,render_template
import random
random_images = [
    'https://picsum.photos/seed/teknoloji/600/350',
    'https://picsum.photos/seed/doga/600/350',
    'https://picsum.photos/seed/uzay/600/350',
    'https://picsum.photos/seed/hayvan/600/350'
]
riddles = [
    {'question': 'Ekranı vardır, tuşu vardır; doğru kullanırsan bilgi sunar. Cevabı nedir?', 'answer': 'Bilgisayar'},
    {'question': 'Cebinde durur, dünyaya bağlar; fazla bakarsan zamanını alır. Cevabı nedir?', 'answer': 'Telefon'},
    {'question': 'Ne eli vardır ne ayağı, ama herkesi birbirine baglar. Cevabı nedir?', 'answer': 'Internet'}
]
app = Flask(__name__)
interestingfacts = ['2019 da yapılan bir araştırmaya göre, insanların %60 ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.','Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.','2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50 den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.']
@app.route("/bilgiler")
def hello_world():
    return f'<p>{random.choice(interestingfacts)}</p>'
@app.route("/resim")
def rastgele_resim():
    image_url = random.choice(random_images)
    return f'''
        <h1>Rastgele bir resim</h1>
        <img src="{image_url}" alt="Rastgele resim" style="max-width: 600px; width: 100%; border-radius: 12px;">
        <p><a href="/">Ana sayfaya dön</a></p>
    '''
@app.route("/bilmece")
def bilmece():
    selected_riddle = random.choice(riddles)
    return f'''
        <h1>Bir bilmece</h1>
        <p><strong>Soru:</strong> {selected_riddle["question"]}</p>
        <p><strong>Cevap:</strong> {selected_riddle["answer"]}</p>
        <p><a href="/">Ana sayfaya dön</a></p>
    '''
@app.route("/")
def anasayfa():
    return render_template("index.html")
app.run(debug=True)
