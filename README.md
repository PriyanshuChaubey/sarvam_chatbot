# 🪔 Indian Language Chatbot — Powered by Sarvam AI

**A conversational AI chatbot built specifically for India — supporting 13 Indian languages with real-time auto language detection, conversation memory, and a professional web interface.**

---

## 🌟 About The Project

India has over 1.4 billion people speaking hundreds of languages — yet most AI chatbots only work in English. This project solves that problem.

This chatbot is built using **Sarvam AI** — India's own sovereign AI platform — and supports **13 major Indian languages** including Hindi, Tamil, Telugu, Malayalam, Kannada, Bengali, Marathi, Gujarati, Punjabi, and more. The bot automatically detects which language the user is typing in and responds in that exact same language — no configuration needed.

Whether a user types in pure Hindi, Tamil, Kannada, or even casual Hinglish like *"Bhai kya scene hai?"*, the chatbot understands and responds naturally in the same language and tone.

---

## ✨ Key Features

**🔍 Automatic Language Detection**
The chatbot uses Sarvam AI's language identification API to detect the language of every message in real time. It returns BCP-47 codes like `hi-IN` for Hindi and `ta-IN` for Tamil, and immediately adjusts its reply language. No dropdowns, no settings, no friction for the user.

**🧠 Conversation Memory**
Unlike simple one-shot chatbots, this bot remembers the entire conversation. It maintains a rolling history of the last 20 messages and sends them with every API call, giving the model full context. If you tell the bot your name at the start, it will remember it throughout the entire conversation.

**🔒 Force Language Mode**
The sidebar includes buttons for all 13 supported languages. Clicking any language locks the bot's responses to that language — even if the user types in English. The lock can be toggled on and off at any time.

**🌐 Hinglish Support**
Many Indians communicate in a mix of Hindi and English known as Hinglish. The language detection model correctly identifies Hinglish as Hindi, ensuring the bot responds naturally rather than switching to English.

**🎨 Indian Themed Professional UI**
The entire interface is designed with an Indian identity — using the tricolor palette of saffron, white, and green. The hero banner, chat bubbles, dividers, and sidebar all carry this theme, making it feel distinctly Indian and professional.

---

## 🛠️ Tech Stack

| Technology | Role in Project |
|---|---|
| **Python 3.10+** | Core backend language used throughout the project |
| **Sarvam AI API** | Powers the LLM (sarvam-m model), language detection, and translation |
| **Streamlit** | Used to build the entire web-based chat interface |
| **python-dotenv** | Manages environment variables and keeps the API key secure |
| **uv** | Fast modern Python package manager used instead of pip |

---

## 🌐 Supported Languages

Hindi · Tamil · Telugu · Malayalam · Kannada · Bengali · Marathi · Gujarati · Punjabi · Odia · Assamese · Urdu · English

---

## 🔑 Sarvam AI Free Credits

Sarvam AI gives every new user **₹1,000 free credits on signup**. These credits work across all APIs — LLM chat, language detection, and translation — and they never expire. For a development and learning project like this, the free credits are more than sufficient to build, test, and demo the chatbot comfortably.

---

## 👨‍💻 Author

**Priyanshu**
3rd Year B.Tech Student passionate about AI, NLP, and building real-world products for India.

---

## 🙏 Acknowledgements

- [**Sarvam AI**](https://sarvam.ai) for building India's own sovereign AI platform and making it accessible to developers with generous free credits
- [**Streamlit**](https://streamlit.io) for making it possible to build beautiful web apps entirely in Python
- 
---

<div align="center">
Made with ❤️ for भारत &nbsp;🇮🇳&nbsp; • &nbsp;भारत की अपनी AI
</div>
