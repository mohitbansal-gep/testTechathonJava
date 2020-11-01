import outlook
mail = outlook.Outlook()
mail.login('emailaccount@live.com','youoijweoiqwklkjlkdsword')
mail.inbox()
print mail.unread()
