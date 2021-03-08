def half_text_file(path):
    # reduce the size of text file into half
	with open(path, "r") as f:
		keywords = f.readlines()
	print(len(keywords))
	print(keywords)
	start = len(keywords)//2
	stop = len(keywords)
	keywords = keywords[start:stop]
	print(len(keywords))
	print(keywords)
	with open(path, "w") as g:
		for key in keywords:
			g.write("%s" % key)

# half_text_file('keywords/test.txt')


def check_file(key):
	key = key + '\n'
	with open("test.txt", "r") as f:
		keywords = f.readlines()
		if key in keywords:
			# print('Present')
			return True
		else:
			with open("test.txt", "a") as g:
				g.write("%s" % key)
				# print('Not present')
				return False

# status = check_file(None)
# if status is True:
# 	print('Present')
# else:
# 	print('Not present')


def log_fun(log_path=None):
	from datetime import date
	from pathlib import Path
	import logging
    # log_path = 'logs/'
    today = date.today()
    if log_path is None:
        log_file = Path(str(today) + '.log')
    else:
        log_file = Path(log_path + str(today) + '.log')
    logging.basicConfig(filename=log_file, filemode='a', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    return logging

logger = log_fun('logs/')
logger.info("Platform name: %s, Post response: %s, Payload: %s", 'var1', 'var2', 'var3')


def setup_logger(name, filename):
    logger = logging.getLogger(name)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.ERROR)
    handler = TimedRotatingFileHandler(filename, when="midnight", interval=1)
    handler.suffix = "%Y%m%d"
    formatter = logging.Formatter("%(asctime)s | %(message)s", "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger('', '')


def lang_translator(text):
	from google_trans_new import google_translator  
	translator = google_translator()  
	translate_text = translator.translate(text, lang_src='en')  
	detect = translator.detect(text)
	print(translate_text)
	print(detect)

lang_translator("Mitä sinä teet")