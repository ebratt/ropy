from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'ropy'
settings.subtitle = 'a community of opportunity'
settings.author = 'Eric Bratt'
settings.author_email = 'eric_bratt@yahoo.com'
settings.keywords = 'web2py, python, crm, platform, ipaas, paas, daas'
settings.description = 'ropy is a web2py-powered application that helps people work smarter.'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '5ca8a3a9-7699-441d-a552-cdd7c6a181b6'
settings.email_server = 'logging'
settings.email_sender = 'admin@ropy.com'
settings.email_login = None
settings.login_method = 'local'
settings.login_config = None
settings.plugins = []
