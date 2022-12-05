import glob
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

    def merge_df(self, *df):
        for i, d in enumerate(df):
            if i == 0:
                _df = d
            _df = pd.merge(_df, d, how="outer")
        return _df.sort_values("asctime", ignore_index=True)

    def log_to_df(self, log_files):
        df_list = []
        for log_file in log_files:
            df = self.read_logfile(log_file)
            df_list.append(df)
        return self.merge_df(*df_list)


if __name__ == "__main__":
    file_path = "./logs/pos_log.log"
    d1 = LogAnalysis().read_logfile(file_path)
    file_path = "./logs/count_log.log"
    d2 = LogAnalysis().read_logfile(file_path)
    file_path = "./logs/button_log.log"
    d3 = LogAnalysis().read_logfile(file_path)
    d = LogAnalysis().merge_df(d1, d2, d3)
    print(d)

    data_list = glob.glob("./logs/*.log")
    d = LogAnalysis().log_to_df(data_list)
    print(d)
