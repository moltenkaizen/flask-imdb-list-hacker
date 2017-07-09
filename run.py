from flask import Flask, render_template
import csv

app = Flask(__name__)


@app.route("/")
def template_test():
    results = []
    with open('indies.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            with open('movietitles.txt', 'r') as inF:
                for line in inF:
                    title = line.split('(')[0].lower()
                    if row['Title'].lower() in title:
                        row['IMDb_rating'] = row['IMDb Rating']
                        results.append(row)
                        # print('Title: ', row['Title'], 'IMDB Rating: ', row['IMDb Rating'], 'Year: ', row['Year'])
    return render_template('template.html', my_string="Wheeeee!", results=results)


if __name__ == '__main__':
    app.run(debug=True)
