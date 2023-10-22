from datetime import datetime
import csv

class logger():
    def __init__(self):
        self.time  = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def log_to_csv(self, colors, shape):
        with open('logdata.csv', 'a', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            writer.writerow([time, colors, shape])

        


