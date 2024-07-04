from flask import Flask, request, render_template
from analyze import analyze_review

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    review = request.form['review']
    sentiment = analyze_review(review)
    return render_template('index.html', review=review, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
