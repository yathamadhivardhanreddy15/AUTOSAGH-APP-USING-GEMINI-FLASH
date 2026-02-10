import os
from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""

    if request.method == 'POST':
        image = request.files['image']

        if image:
            img = Image.open(image)

            prompt = "Describe this image in detail."

            response = model.generate_content([prompt, img])
            response_text = response.text

    return render_template('index.html', response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
