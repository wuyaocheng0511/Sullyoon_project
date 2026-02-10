from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # 這裡的 user_name 會傳送到 HTML 的 {{ user_name }} 位置
    return render_template('index.html', user_name="Sullyoon")

if __name__ == '__main__':
    # host='0.0.0.0' 代表監聽所有網路介面
    app.run(debug=True, host='0.0.0.0', port=5000)
