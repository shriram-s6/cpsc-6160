import csv


# Write scores to a CSV file
def write_score(player_name, score):
    with open('assets/scores.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([player_name, score])


# Read scores from a CSV file
def read_scores():
    scores = []
    with open('assets/scores.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            scores.append({'spaceship_name': row[0], 'score': int(row[1])})
    return scores
