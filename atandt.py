import outlook
mail = outlook.Outlook()
mail.login('emailaccount@live.com','yourpasmyokokPasswordsword')
mail.inbox()
print mail.unread()
