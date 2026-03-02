# 🛑 ScamSlap Bot

**Your Grandpa's Digital Bodyguard Against AI Scams and Deepfakes on Facebook Messenger.**

ScamSlap is an automated, cloud-hosted cybersecurity bot designed to protect vulnerable users (like the elderly) from modern internet scams, AI-generated images, and deepfake videos. You simply forward a suspicious image or Facebook Reel to the bot, and it neutralizes the threat by analyzing the media and replying with a clear verdict in the user's native language.

---

## 🎯 The Mission
Internet scams have evolved. Phishing links are now accompanied by highly realistic AI-generated faces, and fake celebrity endorsements are powered by deepfake video Reels. ScamSlap acts as a frontline defense system that sits directly inside Facebook Messenger, requiring zero technical knowledge from the end-user. 

## ⚙️ Core Features

* 📸 **Image AI Detection:** Scans images directly sent from the camera roll to detect AI anomalies.
* 🎥 **Deepfake Video Slicing:** Extracts Facebook Reels, breaks them down frame-by-frame, and calculates the probability of AI generation.
* 🪓 **CDN Wall Bypassing:** Uses `yt-dlp` to smash through Facebook's share links and extract the raw `.mp4` or `.jpg` files without requiring the user to take manual screenshots.
* 🌍 **Tactical Auto-Translation:** Spies on the user's Facebook locale settings via the Graph API and translates the warning messages on the fly, replying in the exact language the user speaks.
* ☁️ **Cloud-Native & Serverless:** Deployed 24/7 on Render, hooked directly to Meta's Webhooks.

## 🛠️ Arsenal (Tech Stack)

* **Python 3**
* **FastAPI / Uvicorn** (Handling the Meta Webhook pipeline)
* **yt-dlp** (Extracting raw media from Facebook share links)
* **Sightengine API** (AI and Deepfake detection models)
* **Deep-Translator** (Google Translate API for real-time localization)
* **Meta Graph API** (Sending messages and extracting user locale)

## 🚀 How It Works (The Pipeline)

1. **Intercept:** The user sends a photo or shares a Reel to the ScamSlap Messenger page.
2. **Extract:** The Python backend receives the webhook payload. If it's a restricted link, `yt-dlp` acts as a battering ram to extract the raw media URL.
3. **Analyze:** The raw media is sent to Sightengine's servers. Videos are analyzed frame-by-frame.
4. **Translate & Fire:** The bot queries Meta for the sender's language, translates the verdict, and shoots the final warning back to the user's chat.

---
*Built with grit, Python, and zero tolerance for internet scammers.* 💥
