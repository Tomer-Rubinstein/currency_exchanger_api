from flask import Flask, render_template, request
from api import Currency
from datetime import timedelta, datetime
import requests

app = Flask(__name__)

months = {
    "1": "Jan",
    "2": "Feb",
    "3": "Mar",
    "4": "Apr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Aug",
    "9": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}

@app.route("/")
def homepage():
    return render_template("homepage.html", value="")

@app.route("/send", methods=['GET', 'POST'])
def send():
    if request.method == "POST":
        prev_state = request.form["date"].split("-")
        fdate = request.form["date"]
        c_code = request.form["c_code"]

        for _ in range(2):
            fdate = fdate.replace("-", "")

        USD = Currency(c_code, fdate)
        res = USD.get_value(USD.get_currency())

        if res == None or res == "" or res == " ":
            for _ in range(3):
                if res == None or res == "" or res == " ":
                    # Subtract Date By 1
                    m_num = str(int(prev_state[1]))
                    m = months[m_num]
                    full_date = f"{m} {prev_state[-1]} {prev_state[0]}"
                    c = datetime.strptime(full_date, "%b %d %Y")
                    d = str(c - timedelta(days=_))
                    print(f"{_}: {d}")

                    for x in range(2):
                        d = d.replace("-", "")

                    d = d[:8]

                    # Get Value, if None: run again.
                    USD = Currency(c_code, d)
                    res = USD.get_value(USD.get_currency())
                    
                    # check if need to render yet again
                else:
                    return render_template("homepage.html", value=res + "₪", new_date=f"({str(c - timedelta(days=_))[:10]}) YYYY-MM-DD")

        return render_template("homepage.html", value=res)
    return render_template("homepage.html", value=res)



@app.route("/showCodes")
def showCodes():
    # https://www.boi.org.il/currency.xml scrape data from here.
    codes = [
        "​01",
        "02​",
        "31",
        "27​",
        "18",
        "06",
        "12​",
        "28​",
        "17​",
        "03​",
        "05​",
        "69​",
        "70​",
        "79",
    ]
    names = []
    state = []
    r = requests.get("https://www.boi.org.il/currency.xml")
    raw_data = r.text.split()
    for line in raw_data:
        if "</NAME>" in line:
            line = line.replace("<NAME>", "")
            line = line.replace("</NAME>", "")
            names.append(line)
        if "</COUNTRY>" in line:
            line = line.replace("<COUNTRY>", "")
            line = line.replace("</COUNTRY>", "")
            state.append(line)
    return render_template("showCodes.html", names=names, state=state, codes=codes, length=len(names))

if __name__ == "__main__":
    app.run(debug=True)
