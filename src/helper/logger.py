import logging
from os import getcwd, listdir, mkdir
from os.path import join

# TODO: write a basic logger
# -------------------- .log folder --------------------
log_dir = "logs"
if not log_dir in listdir(getcwd()):
    try:
        mkdir(log_dir)
    except OSError as e:
        print(e)

# -------------------- main root_logger --------------------
root_logger = logging.getLogger()

# Set the log level
root_logger.setLevel(logging.DEBUG)

# Create a file handler for the main root_logger
handler = logging.FileHandler(join(log_dir, 'app.log'))

# Set the format for the logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the root_logger
root_logger.addHandler(handler)
