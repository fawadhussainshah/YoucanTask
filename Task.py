from flask import Flask,render_template,request, jsonify, redirect, Response
import csv

app = Flask(__name__)

error=None
@app.route('/',methods=['GET', 'POST'] )
def hello_world():
    #text_file = open("sample_data.txt", "r")
   # lines = text_file.read().split(',')
    #lines = text_file.read().split('\n')
   # print lines
   # print len(lines) - 1
   # totat_records=len(lines)-1
    #text_file.close()
   # return render_template('tableresult2.html')
    return render_template('login3.html', error=error)

import os
import csv
UPLOAD_FOLDER = 'C:\Users\SyedFawad\Desktop'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['csv'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
@app.route('/uploader', methods=['GET','POST'])
def upload_file():
    error=None
    #my_method = request.json['method']
    if request.method == 'POST' and 'file' in request.files:
        f = request.files['file']
       # f.save(secure_filename(f.filename))
        if f and allowed_file(f.filename):
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
            global p
            p=UPLOAD_FOLDER+"/"+f.filename
            checking_format_csv=check_format(f.filename, 2)
            print "format is =", checking_format_csv
            if checking_format_csv==False:
                error='File uploaded is not in correct order'
                return render_template('uploadfile.html', error=error)
            print "p= ",p
            q_id1=[]
            questions1=[]
            answerofteacher1=[]
            score1=[]
            global counter2
            counter2=0
            global score
            with open(p) as f:
                reader = csv.reader(f)
                for row in reader:
                    #q_id1.append(row[0])
                    #while counter2<5:
                    if counter2==0:
                            #questions1.append(row[0])
                        questions1=row[0]
                        score=row[1]
                        man=score
                    else:
                        answerofteacher1.append(row[0])
                        #score1.append(float(row[3]))
                   # if counter2==51:
                    #    break
                    counter2=counter2+1
            print "counter2 =",counter2
            print "score = ",score
            print questions1
            print answerofteacher1
            exam_name="MIDTERM1"
            global avg
            avg=0
            sum1=0
            for i in range(0,counter2-1):
                g=answerofteacher1[i]
                print "calculating score = ",i+1
                f=Semantic_Similarity.Calculate_Similarity(questions1, g, score, 3)#m=3
                sum1=sum1+f
                obtained_marks.append(f)

            global max
            max=0
            max=maximum(obtained_marks)
            max=float(max)
            max = format(round(max, 2))
            global min
            min=0
            min=minimum(obtained_marks)
            min=float(min)
            min = format(round(min, 2))
            #obtained_marks = Semantic_Similarity.Evaluate_Paper(questions1, answerofteacher1, p, 2)
            print "+++++++++++", obtained_marks
            global scores2
            scores2=0
            answerscores3=obtained_marks
            for i in range(0,counter2-1):
                scores2=scores2+obtained_marks[i]
            scores2 = format(round(scores2, 2))
            print "scores2 = ",scores2
            global answerscores2
            answerscores2=[]
            global m
            m=(counter2-1)*int(score)
            print "m = ",m
            for i in range(0,counter2-1):
                x=obtained_marks[i]
                x=format(round(x,2))
                answerscores2.append(x)
                answerscores3.append(x)
            l=counter2-1


            avg=sum1/l
            avg=format(round(avg,2))
            global anothercounter
            anothercounter=[]
            for i in range(0,counter2):
                h=i+1
                anothercounter.append(h)
            print "avg=",avg
            global checker
            checker=1
            return render_template('tableresult2.html',counter2=counter2,scores2=scores2,answerscores2=answerscores2,answerscores3=answerscores3,score=score,m=m,avg=avg,min=min,max=max,anothercounter=anothercounter)
        error='The file is not in csv format. Please upload a file in csv format'
        return render_template('uploadfile.html',error=error)

def minimum(list):
    min = list[0]
    for elm in list[1:]:
        if elm < min:
            min = elm
    return min


def maximum(list):
    max = list[0]
    for elm in list[1:]:
        if elm > max:
            max = elm
    return max


def check_format(filename, total_columns):
    column_that_should_not_exist = total_columns

    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        i = 0
        Format = False
        for row in reader:
            try:
                row[column_that_should_not_exist]
                Format = False
                return Format
            except:
                Format = True
        return Format
if __name__ == '__main__':
    app.run()
