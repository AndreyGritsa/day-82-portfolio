from flask import Flask, render_template, request, flash, url_for, redirect
import os
import datetime
import smtplib
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET")
# Bootstrap(app)

MY_EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASS")


@app.route("/", methods=["GET", "POST"])
def index():
    year = datetime.datetime.now().year
    if request.method == "POST":
        print("Message")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="gricaenko.95a@gmail.com",
                msg=f"Subject:{request.form['name']} work!\n\n{request.form['text']}\n{request.form['phone']}"
            )
        flash("Message has been sent. I'll contact you ASAP. Have a good time out there :)")
        return redirect(url_for("index") + "#contact-me")

    return render_template("index.html", year=year)

if __name__ == "__main__":
    app.run(debug=True)