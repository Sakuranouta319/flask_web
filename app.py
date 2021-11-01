from flask import Flask, render_template #載入 Flask
app=Flask(__name__) #建立 Application 物件

#建立網站首頁的回應方式
@app.route('/')
def index():  #用來回應網站首頁的函式
    paragraphs = {
        '系級: 資管二乙',
        '姓名: 林貞智',
        '學號: C109118245'
    }
    return render_template('index.html', title = '自我介紹', data=paragraphs) #回傳網站的內容

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

#啟動網站伺服器
#app.run(debug=True)
