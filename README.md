# log-analysis

## loggle
python-json-logger config sample
### Usage
- stream
```python
from libs.loggle import logger
logger.info("log")
```
- file
```python
import libs.loggle as loggle
from libs.loggle import logger
loggle.set_file_handler(
    filename="./logs/test_log.log",
    fileLogLevel=loggle.INFO,
    mode="w",
    filt="test",
)
loggle.info("message":"test", "cnt":999)
```
