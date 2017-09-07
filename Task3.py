from flask import Flask,render_template, request

app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
def hello_world():
    return render_template('uploadfile.html')
@app.route('/admin',methods=['GET', 'POST'])
def hello_world1():
    return render_template('uploadfile.html')

import os

UPLOAD_FOLDER = 'C:\Users\SyedFawad\PycharmProjects\Task'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt'])
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
        with open(f.filename) as fd:
            lines1 = fd.readlines()
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
        #-------------------merging
        x=len(newlist2)
        y=len(newlist3)
        merged_list = []
        loop = 0
        for i in range(0, x):
            for j in range(0, y):
                if i != j:
                    # if newlist2[i]==newlist2[j]:
                    # print i,j,"[",newlist2[i],newlist3[j],"]","[",newlist2[j],newlist3[i],"]"
                    # loop=loop+1
                    # `count.insert(i,loop)
                    # count.append(+1)
                    # merged_list.insert(loop,newlist2[i],newlist3[i])
                    # loop=loop+1
                    if newlist3[i] == newlist3[j]:
                        print i, j, "[", newlist2[i], newlist3[j], "][", newlist2[j], newlist3[i], "]"
                        f = "[" + newlist2[i] + "," + newlist3[j] + "][" + newlist2[j] + "," + newlist3[i] + "]"
                        merged_list.append(f)
                    if newlist2[i] == newlist2[j]:
                        if newlist3[i] != newlist3[j]:
                            print "i=", i, " j=", j
                            f = "[" + newlist2[i] + "," + newlist3[j] + "][" + newlist2[j] + "," + newlist3[i] + "]"
                            merged_list.append(f)

        #------------------
        length=len(merged_list)

        print "p= ",p
        print "counter2 =",counter2


        return render_template('tableresult3.html',counter2=counter2,lines=newlist2,lines1=newlist3,count1=count1,merged_list=merged_list,length=length)
@app.route('/tableresult2',methods=['GET', 'POST'])
def tableresult2():
    return render_template('tableresult3.html', counter2=counter2,lines=lines)


if __name__ == "__main__":
    app.run(host='127.0.0.1')
