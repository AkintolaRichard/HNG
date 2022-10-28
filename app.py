from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hng():
    return jsonify({
            'slackUsername': 'laolu',
            'backend': True,
            'age': 23,
            'bio': 'My name is Richard Olaoluwa Akintola, a Full Stack Developer',
        })

if __name__ == '__main__':
    app.run()
