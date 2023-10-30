from datetime import datetime
import csv


class Logger:
    """Logs found shapes and colors with current timestamp

    Attributes:
        file_name: Path name for the logfile. Defaults to "logdata.csv".
        
    """
    def __init__(self, path_name="logdata.csv"):
        self.path_name = path_name

    def log_to_csv(self, colors, shapes):
        """Writes shapes and colors into csv

        Args:
            colors: Array containing all new found colors
            shape: Array containing all new found shapes
        """
        with open(self.path_name, "a", newline="", encoding="UTF8") as f:
            writer = csv.writer(f)
            time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            for i, shape in enumerate(shapes):
                writer.writerow([time, colors[i], shape])
