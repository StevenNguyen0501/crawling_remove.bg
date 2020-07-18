import pandas as pd

email = {'Account_name': ['tinnvt@bap.jp'],
         'Password': ['StevenNguyenUSA5196']
         }

df = pd.DataFrame(email, columns=['Account_name', 'Password'])

df.to_csv('./email_accounts.csv', index=False, header=True)

print(df)
