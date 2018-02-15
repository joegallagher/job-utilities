from quickbooks import QuickBooks
from quickbooks import Oauth1SessionManager

QUICKBOOKS_CLIENT_KEY = "qyprdqJ3nHgL6rAMmgCNZjUpHxgYOU"
QUICKBOOKS_CLIENT_SECRET = "bKlLnGrmcMyZlqdPvx11CrDjgKlWvfhuXUuaxngO"
access_token = "qyprdnb9eDMKtGEDsjUwCni8UXAuJPJaKkwxfdQyqCWfrHXz"
access_token_secret = "R6hWhVtISKkJaozWwdltjaTpiUJo7QDq5LsGHn3O"
realm_id = "824478045"



session_manager = Oauth1SessionManager(
	sandbox=False,
    consumer_key=QUICKBOOKS_CLIENT_KEY,
    consumer_secret=QUICKBOOKS_CLIENT_SECRET,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

client = QuickBooks(
    sandbox=False,
    session_manager=session_manager,
    company_id=realm_id
)