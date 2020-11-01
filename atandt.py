import outlook
mail = outlook.Outlook()
mail.login('emailaccount@live.com','you dsword')
mail.inbox()
print mail.unread()
