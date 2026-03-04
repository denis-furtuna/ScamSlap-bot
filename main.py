import os
import requests
import yt_dlp
from deep_translator import GoogleTranslator
from fastapi import FastAPI, Request, BackgroundTasks, Response

app = FastAPI()

# --- ARSENALUL TĂU SECRET (Securizat în Cloud!) ---
PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN')
SIGHTENGINE_USER = os.environ.get('SIGHTENGINE_USER')
SIGHTENGINE_SECRET = os.environ.get('SIGHTENGINE_SECRET')
VERIFY_TOKEN = os.environ.get('SCAM_SLAP_SECRET')


# -----------------------------

def trimite_mesaj_facebook(sender_id, text_mesaj):
    # 1. SPIONAJ: Spargem ușa la Meta și aflăm limba telefonului!
    url_spion = f"https://graph.facebook.com/{sender_id}?fields=locale&access_token={PAGE_ACCESS_TOKEN}"
    try:
        date_spion = requests.get(url_spion).json()
        limba_tinta = date_spion.get('locale', 'ro_RO').split('_')[0]
    except Exception as e:
        print(f"⚠️ Spionajul a eșuat. Mergem pe default (Română).")
        limba_tinta = 'ro'

    # 2. TRADUCERE TACTICĂ: Dacă nu e român, traducem glonțul pe zbor!
    if limba_tinta != 'ro':
        print(f"🕵️‍♂️ Inamic străin detectat (Limba: {limba_tinta}). Traducem mesajul...")
        try:
            text_mesaj = GoogleTranslator(source='ro', target=limba_tinta).translate(text_mesaj)
            print(f"🔄 Glonț tradus: {text_mesaj}")
        except Exception as e:
            print(f"💥 Traducătorul s-a blocat: {e}")

    # 3. FOC! Tragem pachetul către inamic
    url = f"https://graph.facebook.com/v19.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    pachet = {
        "recipient": {"id": sender_id},
        "message": {"text": text_mesaj}
    }
    requests.post(url, json=pachet)


def extrage_link_brut(url_share):
    print(f"⏳ Punem berbecul pe poarta: {url_share}")
    optiuni = {
        'quiet': True,
        'format': 'best',
    }
    try:
        with yt_dlp.YoutubeDL(optiuni) as ydl:
            date_extrase = ydl.extract_info(url_share, download=False)
            link_brut = date_extrase.get('url', None)
            return link_brut
    except Exception as e:
        print(f"💥 Buncărul a rezistat. Eroare: {e}")
        return None


def analizeaza_poza(url_poza):
    api_url = 'https://api.sightengine.com/1.0/check.json'
    parametri = {
        'models': 'genai',
        'api_user': SIGHTENGINE_USER,
        'api_secret': SIGHTENGINE_SECRET,
        'url': url_poza
    }

    try:
        raspuns = requests.get(api_url, params=parametri)
        date = raspuns.json()
        scor_fake = date['type']['ai_generated'] * 100

        if scor_fake > 75:
            return f"🚨 DEEPFAKE DETECTAT! Această poză este falsă. Șansa de AI este {scor_fake:.2f}%. Nu distribui!"
        else:
            return f"✅ Poza este CURATĂ! Șansa de AI este doar {scor_fake:.2f}%. Totul este în regulă."
    except Exception as e:
        return "⚠️ Eroare tactică la scanare. Nu mi-am dat seama ce e cu poza asta."


def analizeaza_video(url_video):
    print("⏳ Trimit videoclipul la divizia de Deepfake...")
    api_url = 'https://api.sightengine.com/1.0/video/check-sync.json'
    parametri = {
        'models': 'genai',
        'api_user': SIGHTENGINE_USER,
        'api_secret': SIGHTENGINE_SECRET,
        'stream_url': url_video,
        'limit': 4  # 🛑 Oprește-te după 4 gloanțe trase
    }

    try:
        raspuns = requests.get(api_url, params=parametri)
        date = raspuns.json()

        print("\n--- CE A ZIS MERCENARUL SIGHTENGINE ---")
        print(date)
        print("---------------------------------------\n")

        if 'data' in date and 'frames' in date['data']:
            scor_maxim_fake = 0
            for cadru in date['data']['frames']:
                if 'type' in cadru and 'ai_generated' in cadru['type']:
                    scor_curent = cadru['type']['ai_generated'] * 100
                    if scor_curent > scor_maxim_fake:
                        scor_maxim_fake = scor_curent

            if scor_maxim_fake > 75:
                return f"🚨 DEEPFAKE DETECTAT! Am scanat videoclipul. Șansa de AI este de {scor_maxim_fake:.2f}%. E o capcană!"
            else:
                return f"✅ Videoclip CURAT! Șansa de AI este maxim {scor_maxim_fake:.2f}%. Pare complet real!"
        else:
            motiv_eroare = date.get('error', {}).get('message', 'Zuckerberg a blocat accesul mercenarului.')
            return f"⚠️ Buncărul de analiză a refuzat clipul! Motiv: {motiv_eroare}"

    except Exception as e:
        print(f"💥 Eroare letală la video: {e}")
        return "⚠️ Arma s-a blocat total la scanarea videoclipului!"


# =====================================================================
# 🛠️ NOUA UNITATE DE PROCESARE ÎN FUNDAL (MUNCITORUL)
# =====================================================================
def proceseaza_mesaj_greu(date):
    print("\n🚨 --- MUNCITORUL A PRELUAT PACHETUL ÎN BUNCĂR --- 🚨")
    try:
        for entry in date.get("entry", []):
            for mesaj in entry.get("messaging", []):
                sender_id = mesaj["sender"]["id"]

                if "message" in mesaj and "attachments" in mesaj["message"]:
                    for attach in mesaj["message"]["attachments"]:
                        tip_atasament = attach["type"]

                        if tip_atasament == "image":
                            url_poza = attach["payload"]["url"]
                            print(f"Țintă vizuală detectată: {url_poza}")
                            trimite_mesaj_facebook(sender_id, "🕵️‍♂️ Scanez poza pentru falsuri... Așteaptă!")
                            rezultat_scanare = analizeaza_poza(url_poza)
                            trimite_mesaj_facebook(sender_id, rezultat_scanare)

                        elif tip_atasament in ["reel", "share", "video"]:
                            url_share = attach["payload"]["url"]
                            print(f"Link complex detectat: {url_share}")
                            trimite_mesaj_facebook(sender_id,
                                                   "🚧 Am detectat un link protejat de Facebook! Scot berbecul de asalt să sparg seiful...")
                            link_curat = extrage_link_brut(url_share)

                            if link_curat:
                                print(f"VICTORIE! Link-ul brut este: {link_curat}")
                                if ".mp4" in link_curat or tip_atasament in ["reel", "video"]:
                                    trimite_mesaj_facebook(sender_id,
                                                           "🎥 Am spart seiful și am extras videoclipul! Îl trimit la laboratorul de Deepfake (poate dura câteva zeci de secunde, ai răbdare)...")
                                    rezultat_scanare = analizeaza_video(link_curat)
                                    trimite_mesaj_facebook(sender_id, rezultat_scanare)
                                else:
                                    trimite_mesaj_facebook(sender_id,
                                                           "📸 Am smuls poza ascunsă din postare! O trimit direct la scanare...")
                                    rezultat_scanare = analizeaza_poza(link_curat)
                                    trimite_mesaj_facebook(sender_id, rezultat_scanare)
                            else:
                                trimite_mesaj_facebook(sender_id,
                                                       "💀 Misiune eșuată. Zidul a fost prea gros pentru berbecul meu. Încearcă să îi faci o captură de ecran!")
    except Exception as e:
        print(f"💥 Eroare gravă în buncărul de procesare: {e}")


# =====================================================================
# 📡 RADARUL PRINCIPAL (WEBHOOK-UL BLINDAT)
# =====================================================================
@app.get("/webhook")
def verifica_webhook(request: Request):
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    if token == VERIFY_TOKEN:
        return int(challenge)
    return "Marș de aici!"


@app.post("/webhook")
async def primeste_mesaj(request: Request, background_tasks: BackgroundTasks):
    date = await request.json()

    # Dacă mesajul vine de la o pagină (nu e spam)
    if date.get("object") == "page":
        # 1. Trimitem misiunea grea către "Muncitor" în fundal
        background_tasks.add_task(proceseaza_mesaj_greu, date)

        # 2. Îi închidem ușa lui Zuckerberg instantaneu ca să nu trimită duplicate!
        return Response(content="EVENT_RECEIVED", media_type="text/plain", status_code=200)

    # Dacă e un pachet ciudat, îl respingem scurt
    return Response(content="NOT_A_PAGE_EVENT", status_code=404)
