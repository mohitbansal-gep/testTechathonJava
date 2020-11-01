import outlook
mail = outlook.Outlook()
mail.login('emailaccount@live.com','ioqweiouoqwie dsword')
mail.inbox()
print mail.unread()
