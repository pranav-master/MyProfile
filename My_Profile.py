from flask import Flask , render_template, request , redirect
import csv


app = Flask(__name__)

@app.route("/")
def Home():
    return render_template('index.html')

@app.route("/<Page>")
def Page(Page):
    return render_template(Page)

def write_to_csv(data):
    with open('My_Profile/test.csv', mode='a', newline='') as csvfile:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([email,subject,message])


@app.route('/thankYou', methods=['POST', 'GET'])
def thankYou():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("thankYou.html")
    else:
        return "Something went wrong:("
    # the code below is executed if the request method
    # was GET or the credentials were invalid
