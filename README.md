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
│  ├─ write_to_db.py
│  ├─ read_from_db.py
│  ├─ slc.db
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
```

> [!NOTE]
> The [db/create_db.py](db/create_db.py) script is for creating the DB if not exists, or drop and create as a nuke and pave </br>
> The [db/write_to_db.py](db/write_to_db.py) script will contain functions for writing status changes or file lists to the SQLite database </br>
> The [db/read_from_db.py](db/read_from_db.py) script will contain functions for reading records from the SQLite database </br>
> The [db/slc.db](db/slc.db) will contain the SQLite database but in PROD will exist in `~/.local/share/Screen_Library_Compressor` </br>
> The [fs/scan_fs.py](fs/scan_fs.py) script will contain functions for scanning the file system per the library base path defined in [config/config.json](config/config.json) </br>
> The [fs/lockfile.py](fs/lockfile.py) script will contain functions for reading / writing the lockfile (as defined in [config/config.json](config/config.json)) </br>
> Scheduling will handled by cron and [util/schedule.cron](util/schedule.cron) will contain command to create or edit the cron job </br>
> The [log/create_log.py](log/create_log.py) script will contain functions for creating the log file if not exists, nothing if exists </br>
> The [log/write_log.py](log/write_log.py) script will contain functions for writing to the log file (as defined in [config/config.json](config/config.json)) in a structured format </br>
> The [/main.py](/main.py) script will logic conrtol and will call all the other scripts </br>

---
