from flask import Flask, request, jsonify
import random

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    user_msg = request.json.get("message").lower()

    response = ""

    # ===== GREETING =====
    if any(word in user_msg for word in ["hello", "hi", "hey"]):
        response = random.choice([
            "Hey there! 🎨 How can I help you explore art today?",
            "Hi! Looking for something beautiful?",
            "Hello! Tell me your mood and I’ll suggest art ✨"
        ])

    # ===== MOODS =====
    elif any(word in user_msg for word in ["sad", "low", "depressed"]):
        response = "I’ll show you some emotional artworks 💙"

    elif any(word in user_msg for word in ["happy", "bright"]):
        response = "Here are some vibrant artworks 🌈"
        

    elif "calm" in user_msg:
        response = "Let’s explore peaceful artworks 🌿"
        

    elif "dark" in user_msg:
        response = "Showing deep & dark themed art 🌑"
        

    elif "energetic" in user_msg:
        response = "Let’s see something dynamic ⚡"
        

    # ===== TYPES =====
    elif "nature" in user_msg:
        response = "Nature art includes landscapes, forests, oceans 🌿"

    elif "portrait" in user_msg:
        response = "Portraits capture human emotion 👤"

    elif "landscape" in user_msg:
        response = "Landscapes show natural beauty 🏞️"

    # ===== STYLE =====
    elif "abstract" in user_msg:
        response = "Abstract art focuses on emotion and shapes 🎭"

    elif "modern" in user_msg:
        response = "Modern art explores new ideas ✨"

    elif "realistic" in user_msg:
        response = "Realistic art shows life as it is 🖼️"

    # ===== HUMAN BEHAVIOR =====
    elif "confused" in user_msg:
        response = "No worries 😄 Try starting with a mood!"

    elif "bored" in user_msg:
        response = "Let’s fix that 😎 Want something relaxing or intense?"

    elif "surprise me" in user_msg:
        response = "Try abstract art — always unexpected 🔥"

    elif "i dont know" in user_msg:
        response = "That’s okay 🙂 Relaxing or exciting?"

    # ===== SYSTEM =====
    elif "what can you do" in user_msg:
        response = "I suggest art based on mood, style, and preferences 🎨"

    elif "who are you" in user_msg:
        response = "I’m your AI Art Assistant 🤖 I help you explore and understand art!"

    elif "bye" in user_msg:
        response = "Goodbye! Come back for inspiration 🎨"

    elif "thank" in user_msg:
        response = "You're welcome! 😊 Enjoy exploring art 🎨"

    elif "how to use" in user_msg:
        response = "Browse gallery, explore styles, or upload your own art. I’m here if you need help 😊"

    elif "buy" in user_msg:
        response = "Looking to buy art? Explore the gallery and pick what connects with you 💸"

    elif "upload" in user_msg:
        response = "You can upload your artwork from the artist dashboard 🎨"

    elif "which one is better" in user_msg:
        response = "Hard to say — it depends on your taste. Do you prefer calm or bold styles?"

    # ===== FALLBACK =====
    else:
        response = random.choice([
            "Tell me your mood 😊",
            "Try 'calm', 'dark', or 'happy' 🎨",
            "What kind of art do you like?"
        ])

    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
