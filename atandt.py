import outlook
mail = outlook.Outlook()
mail.login('emailaccount@live.com','okokokok dsword')
mail.inbox()
print mail.unread()
