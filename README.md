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
│  ├─ PLACE_HOLDER.ext
├─ log/
│  ├─ create_log.py
│  ├─ write_log.py
│  ├─ rotate_log.py
├─ main.py
├─ .gitignore
├─ README.md
├─ .env
```

> [!NOTE]
> Secrets (if any) will be in the [/.env](/.env) file and the rest of config settings will be in [config/config.json](config/config.json) </br>
> The [db/create_db.py](db/create_db.py) script is for creating the DB if not exists, or drop and create as a nuke and pave </br>

---
## Notes



> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.



## 0. Dev Set Up
```fish
sudo pacman -S python-dotenv python-requests
sudo pacman -S python-pyqt6
```

/.env # file for secrets
TMDB_API_KEY=ae5ec04cf1d3e2aaf73bf57df908bad3
SQLITE_DB=~/.local/share/reellibman/reellibman.db

import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.path.expanduser(os.getenv("SQLITE_DB"))