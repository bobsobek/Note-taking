wfrom flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    title = ''
    notes = ''
    titles =''
          
    with open("title.txt") as file:
        lines = file.readlines()
    titles = []
    for line in lines:
        parts = line.split("\n")
        titles.append({
            "id": parts[0]
             })
    return render_template('index.html', title=title, notes=notes, titles=titles)

@app.route("/form1", methods=["POST"])
def handle_form1():
    data1 = {}
    for key in request.form:
        data1[key] = request.form.getlist(key)
    title = data1['title'][0]
    notes = data1['notes'][0]
    with open('notes.txt', 'a') as file:
        notes = notes.replace("\n",' ')
        file.write(notes +'\n')
        file.close()
    with open('title.txt', 'a') as file:
        file.write(title +'\n')
        file.close()
    with open("title.txt") as file:
        lines = file.readlines()
    titles = []
    for line in lines:
        parts = line.split('\n')
        titles.append({
            "id": parts[0]
             })
    return render_template('index.html', title=title, notes=notes,titles=titles)

@app.route("/form2", methods=["POST"])
def handle_form2():
  passage = "Notes not found"
  titlel =[]
  notesl =[]
  data2 = {}
  for key in request.form:
    data2[key] = request.form.getlist(key)
  check = data2['check'][0]
  
  with open("title.txt") as file:
        lines = file.readlines()   
  titlel = []
  for line in lines:
        line = line.replace("\n",'')
        titlel.append(line)
  file.close()
  with open("notes.txt") as file:
        lines = file.readlines()   
  
  notesl = []
  for line in lines:
        line = line.replace("\n",'')
        notesl.append(line)
  file.close()

  if titlel.count(check) > 0:
    index = titlel.index(check)
    passage = notesl[index]
  
  
  with open("title.txt") as file:
        lines = file.readlines()   
  titles = []
  for line in lines:
        parts = line.split("\n")
        titles.append({
            "id": parts[0]
             })
  file.close()
  return render_template("index.html", check = check, titles=titles,titlel=titlel, notesl=notesl, passage=passage)




app.run(host='0.0.0.0', port=81)
