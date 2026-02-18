from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mutate', methods=['POST'])
def mutate():
    data = request.json
    cmd = data.get('command', '').lower()
    
    # Default State: Liquid Mercury
    dna = {
        "color": "#444444",
        "speed": 1.0,
        "distortion": 0.2,
        "mode": "stable"
    }
    
    # Mutation Logic (The Shock Factors)
    if "plasma" in cmd:
        dna.update({"color": "#ff0055", "speed": 5.0, "distortion": 1.5, "mode": "hyper-drive"})
    elif "gold" in cmd:
        dna.update({"color": "#ffd700", "speed": 0.5, "distortion": 0.1, "mode": "solid-gold"})
    elif "void" in cmd:
        dna.update({"color": "#000000", "speed": 0.1, "distortion": 8.0, "mode": "singularity"})
    elif "matrix" in cmd:
        dna.update({"color": "#00ff41", "speed": 3.0, "distortion": 0.8, "mode": "digital-grid"})
    elif "nebula" in cmd:
        dna.update({"color": "#8a2be2", "speed": 2.0, "distortion": 2.0, "mode": "deep-space"})
        
    return jsonify(dna)

if __name__ == '__main__':
    app.run(debug=True)