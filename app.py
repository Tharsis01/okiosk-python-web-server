import webbrowser
import main

from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def create():
    print(request.is_json)
    params = request.get_json()
    print(params['order'])
    order = params['order']

    a = main.nlp(order)
    return jsonify({"answer": a})
    #1
    # 자연어처리

    # 주문되는 qr코드인 order.png 를 s3에 업로드
    # 이 이미지를 키오스크에 찍으면 자동주문

    #return redirect("https://google.com")

    #2
    # 자연어처리

    # 메뉴코드 폰으로 쏴줌

    # 폰에서 메뉴 코드를 qr코드로 만든다

    # 키오스크에서 그 코드에 매칭되는 메뉴 주문되게끔

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('create'))

    #app.run(host='0.0.0.0', port=9900, debug=True)
    app.run(debug=True)
