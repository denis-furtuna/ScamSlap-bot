# 🛡️ ScamSlap - Scutul Anti-Deepfake pentru Messenger

<p align="center">
  <b>Bodyguardul digital care îți protejează familia de fraudele realizate prin Inteligenta Artificială (Deepfakes) direct pe Facebook Messenger.</b>
</p>

---

## 📸 Demonstrația de Forță (Suport Multi-Lingv)

ScamSlap este construit inteligent: **detectează automat limba setată pe telefonul bunicului** și îi răspunde în limba lui nativă. Nu trebuie să configurezi nimic, arma se calibrează singură!

Iată ScamSlap în acțiune, interceptând și analizând media în 3 limbi diferite:

| 🇷🇴 Limba Română | 🇺🇸 Limba Engleză | 🇩🇪 Limba Germană |
| :---: | :---: | :---: |
| ![ScamSlap in Romanian](scamslap_ro.png) | ![ScamSlap in English](scamslap_en.png) | ![ScamSlap in German](scamslap_de.png) |

*(Aici apar capturile de ecran reale din Messenger)*

---
<img width="482" height="143" alt="scamslap_de" src="https://github.com/user-attachments/assets/e07837c3-0309-4e93-8fe4-02242f638599" />

## 🔥 De ce ScamSlap? (Misiunea Noastră)

Scam-urile realizate prin Deepfake (video-uri false cu personalități, apeluri cu voci clonate) sunt tot mai greu de detectat cu ochiul liber, mai ales de către persoanele în vârstă. ScamSlap oferă o **linie de apărare instantanee**. Bunicul primește un Reel dubios? Îl dă „Share” către ScamSlap și primește verdictul în 30 de secunde!

## 🚀 Arsenalul Tehnic (Ce e sub capotă?)

Am construit un sistem complex folosind tehnologii de ultimă oră pentru a asigura precizie și securitate:

* **⚡ FastAPI & Render:** Un server backend ultra-rapid, găzduit în Cloud (Render), care stă de veghe 24/7.
* **🧠 Sightengine API (GenAI Model):** Mercenarii noștri de elită în scanarea AI. Folosim modele avansate care analizează cadrele media pentru a detecta urme matematice de generare sintetică.
* **Berbecul `yt-dlp`:** Un tool de efracție digitală care sparge barierele Facebook pentru a extrage link-urile brute (`.mp4`) din Reel-uri și Share-uri, permițând analizarea lor.
* **🌐 Meta Graph API (Locale Detection):** Interogăm baza de date Meta pentru a afla limba utilizatorului în timp real.
* **🔄 `deep-translator`:** Traducem verdictul în limba utilizatorului fix înainte ca glonțul să plece, pentru un impact maxim.
* **🛡️ Arhitectură Securizată:** Toate cheile API sunt ascunse în Environment Variables pe Render, nu în cod.

## 🛠️ Cum funcționează?

1.  **Interceptare:** Bunicul trimite o poză sau un Reel către pagina de Facebook Messenger.
2.  **Triaj (Background Tasks):** Serverul FastAPI dă un răspuns instantaneu lui Facebook (`200 OK`) și trimite analiza grea în buncărul de procesare din fundal (pentru a evita duplicatele).
3.  **Spargerea Seifului:** Dacă e un Reel, `yt-dlp` extrage fișierul video brut.
4.  **Scanare Lunetistă:** Trimitem media la Sightengine cu parametri de eșantionare tactici (ex: un cadru la fiecare 5 secunde, limitat la 4 cadre) pentru a acoperi tot clipul optimizând bugetul de credite.
5.  **Traducere & Verdict:** Traducem scorul (ex: 98% AI) într-un mesaj clar în limba bunicului și îl trimitem înapoi pe Messenger.

---
<p align="center">
  Construit cu ❤️ pentru a proteja pe cei care ne-au crescut. 
</p><img width="632" height="278" alt="scamslap_ro" src="https://github.com/user-attachments/assets/08e16218-dfa9-44fc-b3c4-65a7fabea8f0" />
<img width="644" height="520" alt="scamslap_en" src="https://github.com/user-attachments/assets/561c69cc-3f24-4cda-9d9d-0a6ac6eea1dc" />
![Uploading scamslap_de.png…]()
