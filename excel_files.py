import csv

with open("week23.csv" , 'w') as f:
    pen = csv.writer(f)
    header = ["Name", "Cell phone", "City"]
    pen.writerow(header)
    pen.writerow(["francine", "438 379 8245", "Montreal"])
f.close
