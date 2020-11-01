import outlook
mail = outlook.Outlook()
mail.login('emailaccount@live.com','youoijweoi dsword')
mail.inbox()
print mail.unread()
