
from config import DOWNLOAD_PATH
from videx_bot import VidexBot

def main():
    bot = VidexBot(DOWNLOAD_PATH)
    bot.open_page()
    bot.fill_text("antragsteller.familienname", "Emam")
    # weitere Felder...
    bot.quit()

if name == "main":
    main()