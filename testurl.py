from flask import url_for

print(url_for('index'))
##报错
#Attempted to generate a URL without the application context being pushed. This has to be executed when application context is available.