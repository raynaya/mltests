from flask import Flask
from logging.handlers import TimedRotatingFileHandler
import logging.handlers

app = Flask(__name__)
app.config.from_object('config')
logger = logging.getLogger('agentlogger')
logger.setLevel(logging.getLevelName(app.config.get("LOG_LEVEL", "INFO")))
formatter = logging.Formatter(u"[%(asctime)s] [%(levelname)s] [%(module)s:%(funcName)s:%(lineno)s] %(message)s")
handler = TimedRotatingFileHandler(app.config.get("LOG_FILE_PATH"), when="midnight", encoding="utf-8", interval=1,
                                   backupCount=app.config.get('LOG_MAX_HISTORY', 7))
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("ml is starting ")

from ml_models import main
