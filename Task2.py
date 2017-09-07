from flask import Flask,render_template, request

app = Flask(__name__)
app.secret_key='fawad'
@app.route('/',methods=['GET', 'POST'])
def hello_world():
    return render_template('uploadfile.html')
@app.route('/admin',methods=['GET', 'POST'])
def hello_world1():
    return render_template('uploadfile.html')

import os

UPLOAD_FOLDER = 'C:\Users\SyedFawad\Desktop\m'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['csv','txt'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
counter2=0
p='fawad'
anothercounter=[]
lines=[]
@app.route('/uploader', methods=['GET','POST'])
def upload_file():
    f = request.files['file']
    if f and allowed_file(f.filename):
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        global p
        p=UPLOAD_FOLDER+"/"+f.filename
        ###############################
        text_file = open(f.filename, "r")
        global lines
        lines = text_file.read().split(',')
        #lines = text_file.read().split('\n')
        print lines
        print len(lines) - 1
        text_file.close()
        global counter2
        counter2=len(lines)-1
        #################################
        #=================
        with open("sample_data.txt") as f:
            lines1 = f.readlines()
        newlist = []
        for word in lines1:
            word = word.split(",")
            newlist.extend(word)
        newlist2=[]
        newlist3=[]
        count1=[]
        for i in range(0,counter2*2):
            if i%2==0:
                newlist2.insert(i,newlist[i])
            else:
                newlist3.insert(i,newlist[i])
            count1.append(i+1)
        #=============
        print "p= ",p
        print "counter2 =",counter2


        return render_template('tableresult2.html',counter2=counter2,lines=newlist2,lines1=newlist3,count1=count1)
       # error='The file is not in csv format. Please upload a file in csv format'
        #return render_template('uploadfile.html',error=error)
@app.route('/tableresult2',methods=['GET', 'POST'])
def tableresult2():
    return render_template('tableresult2.html', counter2=counter2,lines=lines)


if __name__ == "__main__":
    app.run(host='127.0.0.1')
