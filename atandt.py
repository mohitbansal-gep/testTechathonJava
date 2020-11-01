import outlook
mail = outlook.Outlook()
mail.login('emailaccount@live.com','wewew dsword')
mail.inbox()
print mail.unread()
