import logging
import os

os.makedirs("output",exist_ok=True)

logging.basicConfig(
    filename='output/execution_log.txt',
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s-%(message)s'
)
