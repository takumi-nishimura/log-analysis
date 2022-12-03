import json
import pandas as pd


class LogAnalysis:
    def __init__(self):
        pass

    def read_logfile(self, path: str):
        with open(path) as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                line = json.loads(line)
                if i == 0:
                    df = pd.DataFrame(columns=list(line.keys()))
                df = pd.concat(
                    [
                        df,
                        pd.DataFrame([list(line.values())], columns=list(line.keys())),
                    ],
                    ignore_index=True,
                )
        return df


if __name__ == "__main__":
    file_path = "./logs/pos_log.log"
    d = LogAnalysis().read_logfile(file_path)
    print(d)
