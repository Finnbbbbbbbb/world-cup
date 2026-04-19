from flask import Flask, render_template
import pandas as pd

app=Flask(__name__)

@app.route("/")
def main():
    df=pd.read_csv("static/csv/WorldCupMatches.csv")
    print(df)
    return render_template("index.html",table=df.to_html(classes="table table=-striped",index=False))


if __name__=="__main__":
    app.run(debug=True)