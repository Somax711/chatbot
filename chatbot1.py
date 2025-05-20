from flask import Flask, render_template, request, jsonify
import os
app = Flask(__name__)

# Ruta a template
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')  # Interfaz de usuario

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")  
    if not user_input:
        return jsonify({"error": "No se proporcionó un mensaje"}), 400
    # Respuestas
    responses = {
    "hola": "¡Bienvenido! ¿Cómo puedo asistirte hoy?",
    "Buenas": "¡Bienvenido! ¿Cómo puedo asistirte hoy?",
    "horario": "Nuestro horario de atención es de lunes a viernes, de 9:00 a 18:00.",
    "ubicación": "Estamos ubicados en el centro de la ciudad. ¿Necesitas la dirección exacta?",
    "envío": "Realizamos envíos a todo el país. ¿Dónde te gustaría recibir tu pedido?",
    "descuento": "Actualmente ofrecemos descuentos en varios productos. ¡Consulta nuestra página para más detalles!",
    "productos": "Ofrecemos una variedad de productos. ¿Qué tipo estás buscando?",
    "seguimiento": "Para rastrear tu pedido, por favor ingresa tu número de seguimiento en nuestro sitio web.",
    "faq": "Puedes consultar nuestras preguntas frecuentes en la sección 'Ayuda' de nuestro sitio.",
    "reclamo": "Si necesitas presentar un reclamo, contáctanos a reclamos@empresa.com.",
    "actualización": "Las actualizaciones de nuestros servicios se publican en nuestro blog. ¿Te interesa recibir notificaciones?",
    "agradecimiento": "Gracias por confiar en nosotros. ¿Hay algo más en lo que pueda ayudarte?"
     }

    # Buscar una respuesta predefinida
    chatbot_response = responses.get(user_input.lower(), "Lo siento, no entiendo tu consulta. ¿Puedes reformularla?")
    return jsonify({"response": chatbot_response})

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)
