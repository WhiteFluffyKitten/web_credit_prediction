import flask
import pickle
import pandas as pd
import sklearn
print('The scikit-learn version is {}.'.format(sklearn.__version__))

app = flask.Flask(__name__)


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # обрабатываем POST
    if flask.request.method == 'POST':
        res = ''
        fea_1 = flask.request.form.get('fea_1')
        fea_2 = flask.request.form.get('fea_2')
        fea_4 = flask.request.form.get('fea_4')
        fea_10 = flask.request.form.get('fea_10')
        fea_11 = flask.request.form.get('fea_11')

        d = {'fea_1': [int(fea_1)], 'fea_2': [float(fea_2)], 'fea_4': [float(fea_4)], 'fea_10': [int(fea_10)],
             'fea_11': [float(fea_11)]}
        print(d)
        df = pd.DataFrame(data=d)
        print(df.dtypes)

        rf = pickle.load(open('Pickle_RF_Model.pkl', 'rb'))

        res = rf.predict(df)
        if res == 0:
            res = 'Low Credit Risk'
        else:
            res = 'High Credit Risk'

        return '''
                  <h1>Prediction result is: {}</h1>'''.format(res)

    # обрабатываем GET (создание полей ввода и кнопки submit)
    return '''
           <form method="POST">
               <div><label> fea_1: <input type="text" name="fea_1"></label></div>
               <div><label> fea_2: <input type="text" name="fea_2"></label></div>
               <div><label> fea_4: <input type="text" name="fea_4"></label></div>
               <div><label> fea_10: <input type="text" name="fea_10"></label></div>
               <div><label> fea_11: <input type="text" name="fea_11"></label></div>
               <input type="submit" value="Submit">
           </form>'''

#запускаем
app.run()
