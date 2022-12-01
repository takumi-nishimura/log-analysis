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
            count += 1

            message = {"message": {"robot_pos": {"x": 1111, "y": 2222}}}
            logger.info(message)

            if count % 3 == 0:
                logger.info({"message": {"count": count}})

            time.sleep(0.1)
        except:
            logger.warning("finish")
            break
