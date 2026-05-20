# Screen_Library_Compressor

>Automation Tool To Apply A Quality Standard To Your Movie / TV Shows Library

---
## File Tree

```
Screen_Library_Compressor/
├─ config/
│  ├─ config.json
├─ db/
│  ├─ create_db.py
│  ├─ Write_to_db.py
│  ├─ read_from_db.py
├─ fs/
│  ├─ scan_fs.py
│  ├─ lockfile.py
├─ util/
│  ├─ schedule.cron
├─ log/
│  ├─ create_log.py
│  ├─ write_log.py
├─ main.py
├─ .gitignore
├─ README.md
├─ .env
```

> [!NOTE]
> The [db/create_db.py](db/create_db.py) script is for creating the DB if not exists, or drop and create as a nuke and pave </br>
> The [db/Write_to_db.py](db/Write_to_db.py) script will contain functions for writing status changes or file lists to the SQLite database </br>
> The [db/read_from_db.py](db/read_from_db.py) script will contain functions for reading records from the SQLite database </br>
> The [fs/scan_fs.py](fs/scan_fs.py) script will contain functions for scanning the file system per the library base path defined in [config/config.json](config/config.json) </br>
> The [fs/lockfile.py](fs/lockfile.py) script will contain functions for reading / writing the lockfile (as defined in [config/config.json](config/config.json)) to prevent multiple instances </br>
> Scheduling will handled by cron and [util/schedule.cron](util/schedule.cron) will contain command to create or edit the cron job </br>
> The [log/create_log.py](log/create_log.py) script will contain functions for creating the log file if not exists, nothing if exists </br>
> The [log/write_log.py](log/write_log.py) script will contain functions for writing to the log file (as defined in [config/config.json](config/config.json)) in a structured format </br>
> The [/main.py](/main.py) script will logic conrtol and will call all the other scripts </br>

> [!CAUTION]
> Secrets (if any) will be in the [/.env](/.env) file and the rest of config settings will be in [config/config.json](config/config.json) </br>

---
## Dependacies
```fish
sudo pacman -S python-dotenv
```
> [!TIP]
> Your package manager may vary.

```python
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.path.expanduser(os.getenv("SQLITE_DB"))
```
> [!NOTE]
> Example /.env content: </br>
> TMDB_API_KEY=00000000 </br>
> SQLITE_DB=~/path/to/database.db </br>

> [!CAUTION]
> Make sure the /.env file is in the .gitignore to avoid leaking secrets!

---