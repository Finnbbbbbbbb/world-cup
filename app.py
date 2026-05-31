from flask import Flask, render_template
import pandas as pd

app=Flask(__name__)

@app.route("/")
def main():
    df=pd.read_csv("static/csv/WorldCupMatches.csv")
    data_list=df.to_dict(orient="records")
    columns=df.columns.tolist()
   
    return render_template("index.html",table_data=data_list,columns=columns)


if __name__=="__main__":
    app.run(debug=True)