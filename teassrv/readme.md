# Teás feladathoz api
### ... hogy ne csak a suliban lehessen tesztelni

Elvileg megegyezik a sulis apival.

### Használata

Letöltés után létre kell hozni egy python környezetet, ahol futtatjuk. Ehhez telepítve kell legyen a python 3.11 legalább.

- Környezet létrehozása: `python -m venv teasprj`
- A teasprj mappába kell másolni a letöltött könyvtárat.
- Belépés a környezetbe: 
	- linuxon és macen: `source /teasprj/bin/activate`
	- windowson cmd-ben: `teasprj\script\activate.bat`
- Sikeres aktiválás után a prompt elején jelzi: `(teasprj)`
- Belépés a könyvtárba: `cd teasprj/teassrv`
- szükséges cuccok telepítése: `pip install -r req.txt`
- Server futtatása: 
	- Indítás (lovalhost:8000-en indul el alapértelmezés szerint): `python manage.py runserver`
	- Indítás másik ip/port-al: `python manage.py runserver ip:port`
	
Ha sikeres volt az indítás nagyjából ez jelenik meg:

	Watching for file changes with StatReloader
	Performing system checks...

	System check identified no issues (0 silenced).
	April 12, 2025 - 16:12:20
	Django version 5.1.7, using settings 'teassrv.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.

Tehát kilépni ctrl+c-vel lehet.
Deaktiválni a python környezetet: `deactivate` paranccsal lehet.

Uninstall: Töröld a teasprj könyvtárat.
