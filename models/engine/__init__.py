from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Create an instance of FileStorage or DBStorage
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
