from flask import Flask, render_template, request, redirect
import csv
import email_sender as email

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt', mode='a') as database:
        database.write(f'\n{email},{subject},{message}')
        
def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message'].replace('\r\n', ' ').replace('\n', ' ')
    with open('database.csv', mode='a', newline='') as database2:
        csv_writer = csv.writer(database2, 
                                delimiter=',', 
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # return 'form submitted hooray!'
    if request.method == 'POST':
        from_email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        data = request.form.to_dict()
        #print(message, data)
        write_to_csv(data)
        email.send_email(from_email, subject, message)
        return redirect('/thankyou.html')       
        #return thank_you(message)
    else:
        return 'something went wrong, please try again'

@app.route('/thankyou')
def thank_you(message):
    return render_template('thankyou.html', message=message)


# @app.route("/works.html")
# def works_page():
#     return render_template('works.html')

# @app.route("/work.html")
# def work_template():
#     return render_template('work.html')

# @app.route("/about.html")
# def about_page():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact_page():
#     return render_template('contact.html')

# @app.route("/components.html")
# def components():
#     return render_template('components.html')

