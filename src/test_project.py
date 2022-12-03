import time

import libs.loggle as loggle
from libs.loggle import logger

if __name__ == "__main__":
    loggle.set_file_handler(
        filename="./logs/pos_log.log",
        fileLogLevel=loggle.INFO,
        mode="w",
        filt="robot_pos",
    )
    loggle.set_file_handler(
        filename="./logs/count_log.log",
        fileLogLevel=loggle.INFO,
        mode="w",
        filt="count",
    )

    count = 0

    while True:
        try:
            if count == 0:
                logger.info("start")

            count += 1

            logger.warning({"message": "robot_pos", "x": 111, "y": 222, "z": 333})

            if count % 3 == 0:
                logger.info({"message": "count", "cnt": count})

            if count % 5 == 0:
                logger.info(count)

            time.sleep(0.1)
        except:
            logger.warning("finish")
            break
