import os
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()
client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])

# first chat call
response = client.chat.completions(
    model="sarvam-105b",
    messages=[
        {"role": "user", "content": "नमस्ते! आप कैसे हैं?"}
    ]
)

# Tamil
tamil = client.chat.completions(
    model="sarvam-105b",
    messages=[{"role": "user", "content": "வணக்கம்! நீங்கள் எப்படி இருக்கிறீர்கள்?"}]
)
print(tamil.choices[0].message.content)

# Malayalam
mal = client.chat.completions(
    model="sarvam-105b",
    messages=[{"role": "user", "content": "നമസ്കാരം! സുഖം ആണോ?"}]
)
print(mal.choices[0].message.content)

conversation_history = []
system_prompt = {
    "role": "system",
    "content": """आप एक helpful AI assistant हैं जो भारतीय भाषाओं में बात कर सकते हैं।
जो भाषा user बोले, उसी भाषा में जवाब दें।
छोटे और clear जवाब दें।"""
}
# read the reply
reply = response.choices[0].message.content
print(reply)

MAX_HISTORY = 20  # last 20 messages = 10 turns

# def chat(user_message: str) -> str:
#     # Add user message to history
#     conversation_history.append({
#         "role": "user",
#         "content": user_message
#     })

#     # Call the API - note: no .create(), just .completions()
#     response = client.chat.completions(
#         model="sarvam-105b",
#         messages=[system_prompt] + conversation_history[-MAX_HISTORY:]
#     )

#     reply = response.choices[0].message.content

#     # Save reply to history
#     conversation_history.append({
#         "role": "assistant",
#         "content": reply
#     })

#     return reply

# print(chat("मेरा नाम प्रियांशु है"))
# print(chat("मैं उत्तर प्रदेश से हूँ"))
# print(chat("मेरे बारे में क्या पता है तुम्हें?"))


# Language detection function
def detect_language(text: str) -> str:
    """Returns the BCP-47 language code of the input text."""
    response = client.text.identify_language(input=text)
    return response.language_code

print(detect_language("नमस्ते कैसे हो"))   # → hi-IN
print(detect_language("வணக்கம்"))           # → ta-IN
print(detect_language("Hello how are you")) # → en-IN
print(detect_language("Kal office jaana hai")) # → hi-IN (Hinglish!)

LANGUAGE_NAMES = {
    "hi-IN": "Hindi", "ta-IN": "Tamil", "te-IN": "Telugu",
    "ml-IN": "Malayalam", "kn-IN": "Kannada", "bn-IN": "Bengali",
    "mr-IN": "Marathi", "gu-IN": "Gujarati", "pa-IN": "Punjabi",
    "od-IN": "Odia", "as-IN": "Assamese", "ur-IN": "Urdu",
    "en-IN": "English"
}

def chat(user_message: str) -> str:
    # Detect this message's language
    lang_code = detect_language(user_message)
    lang_name = LANGUAGE_NAMES.get(lang_code, "Hindi")

    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Tell the model exactly which language to use
    dynamic_system = {
        "role": "system",
        "content": f"""You are a helpful assistant.
The user is writing in {lang_name}. Always respond in {lang_name}.
Be conversational, warm, and concise."""
    }

    response = client.chat.completions(
        model="sarvam-105b",
        messages=[dynamic_system] + conversation_history[-20:]
    )

    reply = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": reply})
    return reply, lang_code

def translate_text(
    text: str,
    target_language: str,
    source_language: str = "auto"  # use "auto" only with model mayura:v1
) -> str:
    response = client.text.translate(
        input=text,
        source_language_code=source_language,
        target_language_code=target_language,
        model="mayura:v1"
    )
    return response.translated_text

# Hindi to Tamil
print(translate_text("आज मौसम बहुत अच्छा है", target_language="ta-IN"))

# English to Malayalam
print(translate_text("What is your name?", target_language="ml-IN"))

# Auto-detect source
print(translate_text("Naan Chennai-la irukken", target_language="en-IN"))


# Formal mode
client.text.translate(
    input="Your payment is pending",
    source_language_code="en-IN",
    target_language_code="hi-IN",
    model="mayura:v1",
    mode="formal"
    # → आपका भुगतान लंबित है
)

# Modern colloquial mode
client.text.translate(
    input="Your payment is pending",
    source_language_code="en-IN",
    target_language_code="hi-IN",
    model="mayura:v1",
    mode="modern-colloquial"
    # → आपका payment pending है
)