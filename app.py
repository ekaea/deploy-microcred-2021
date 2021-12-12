from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model_nb.pkl', 'rb')
model = pickle.load(model_file)


@app.route('/')
def index():
    return render_template('main.html', categori_pred='')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the indeks of air quality
    '''
    pm10, so2, co, o3, no2, max, critical = [x for x in request.form.values()]

    data = []

    data.append(int(pm10))
    data.append(int(so2))
    data.append(int(co))
    data.append(int(o3))
    data.append(int(no2))
    data.append(int(max))
    data.append(int(critical))

    pred_result = model.predict([data])

    pred_result = ' '.join(map(str, pred_result))
    result = ""
    if (pred_result == "0.0"):
        result = "Tidak Baik"
    elif (pred_result == "1.0"):
        result = "Baik"
    else:
        result = "Sedang"

    return render_template('main.html', categori_pred=result, pm10=pm10, so2=so2, co=co, o3=o3, no2=no2, max=max, critical=critical)


if __name__ == '__main__':
    app.run(debug=True)
