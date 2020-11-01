import outlook
mail = outlook.Outlook()
mail.login('emailaccount@live.com','jhwkehfweyiweu')
mail.inbox()
print mail.unread()
