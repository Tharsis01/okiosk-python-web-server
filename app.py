import webbrowser

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['POST'])
def daum():
    webbrowser.open("https://okiosk678db8ca19d740dc8fe9599231a80b92141332-staging.s3.ap-northeast-2.amazonaws.com/public/test.txt")


    return redirect("https://google.com")




if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('daum'))

    #app.run(host='0.0.0.0', port=9900, debug=True)
    app.run(debug=True)
