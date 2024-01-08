# Bot

To launch bot, you need to create a virtual environment and run it.

## To do this, use the following commands:

```bash
python -m venv venv
```
### Windows:
```bash
venv\Scripts\activate.bat
```
### Linux
```bash
venv/Scripts/activate
```
Then install the necessary libraries. (Use python 3.11)
```bash 
pip install -r requirements.txt
```
In the "config" folder, create a .env file and write there:
```python 
BOT_TOKEN="token_your_telegam_bot"
ADMIN_IDS="telegram_id manager(or admin), who will receive messages with orders"
```
Start bot this command:
```bash 
python bot.py 
```
