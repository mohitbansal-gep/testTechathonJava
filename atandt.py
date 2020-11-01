import outlook
mail = outlook.Outlook()
mail.login('emailaccount@live.com','yourpasmy Passwordsword')
mail.inbox()
print mail.unread()
