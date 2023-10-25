from datetime import datetime
import csv

class logger():
    def __init__(self):
        pass

    def log_to_csv(self, colors, shape):
        with open('logdata.csv', 'a', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            for i in range(len(shape)):
                writer.writerow([time, colors[i], shape[i]])

        


