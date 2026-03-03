# 🛡️ ScamSlap - The Anti-Deepfake Shield for Messenger

<p align="center">
  <b>A digital bodyguard designed to protect your family from AI-generated frauds (Deepfakes) directly on Facebook Messenger.</b>
</p>

---

## 📸 Multilingual Force Demonstration

ScamSlap is built with intelligence: **it automatically detects the language set on the user's phone** and responds in their native tongue. No configuration needed—the weapon calibrates itself!

Here is ScamSlap in action, intercepting and analyzing media in 3 different languages:

| 🇷🇴 Romanian | 🇺🇸 English | 🇩🇪 German |
| :---: | :---: | :---: |
| ![ScamSlap in Romanian](scamslap_ro.png) | ![ScamSlap in English](scamslap_en.png) | ![ScamSlap in German](scamslap_de.png) |

*(Real Messenger screenshots showing the analysis process)*

---

## 🔥 Why ScamSlap? (Our Mission)

Deepfake scams (fake videos of celebrities, cloned voices, AI-generated images) are becoming increasingly difficult to detect with the naked eye, especially for the elderly. ScamSlap provides an **instant line of defense**. 

Did Grandpa receive a suspicious Reel? He just "Shares" it with ScamSlap and gets a verdict in 30 seconds. It's that simple.

## 🚀 Technical Arsenal (Under the Hood)

This system integrates cutting-edge technologies to ensure precision, speed, and security:

* **⚡ FastAPI & Render:** An ultra-fast Python backend hosted in the Cloud (Render), standing guard 24/7.
* **🧠 Sightengine API (GenAI Model):** Our elite mercenaries for AI scanning. We use advanced models that analyze media frames for mathematical traces of synthetic generation.
* **YT-DLP Battering Ram:** A digital breach tool that bypasses Facebook's walls to extract raw video links (`.mp4`) from Reels and Shares for deep analysis.
* **🌐 Meta Graph API (Locale Detection):** We query the Meta database to identify the user's language in real-time.
* **🔄 `deep-translator`:** We translate the verdict into the user's language right before the "bullet" is fired, ensuring maximum impact.
* **🛡️ Secure Architecture:** All API keys are hidden in Environment Variables on Render—never hardcoded, never exposed.

## 🛠️ How It Works

1.  **Interception:** The user sends a photo or a Reel to the ScamSlap Facebook Page.
2.  **Triage (Background Tasks):** The FastAPI server sends an immediate response to Facebook (`200 OK`) and pushes the heavy lifting to a background worker (to prevent duplicate messages).
3.  **Breaching the Vault:** If it's a Reel, `yt-dlp` extracts the direct video file.
4.  **Sniper Scanning:** We send the media to Sightengine with tactical sampling parameters (e.g., one frame every 5 seconds, capped at 4 frames) to cover the whole clip while optimizing API credits.
5.  **Translation & Verdict:** We translate the AI probability score (e.g., 98% AI) into a clear message in the user's language and send it back to Messenger.

---
<p align="center">
  Built with ❤️ to protect those who raised us.
</p><img width="632" height="278" alt="scamslap_ro" src="https://github.com/user-attachments/assets/cf5ce4fc-78fe-4fb8-b9e7-f50418b61048" />
<img width="644" height="520" alt="scamslap_en" src="https://github.com/user-attachments/assets/be1c8434-aa77-4772-bb46-b05ce4dfd695" />
<img width="482" height="143" alt="scamslap_de" src="https://github.com/user-attachments/assets/d7f96ca2-87bb-4c6d-82a6-102614194bd4" />
