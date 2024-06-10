from secrets import token_urlsafe
import webbrowser
from urllib.parse import quote

code_challenge = token_urlsafe(64)

client_id = "ae341fa460e94391ad160378983d6d40"
redirect_uri = "http://localhost:8080/callback"

scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing streaming playlist-read-private user-read-playback-position user-library-read"
auth_url = f"""https://accounts.spotify.com/authorize?
response_type=code
&client_id={client_id}
&scope={quote(scopes)}
&code_challenge_method=S256
&code_challenge={code_challenge}
&redirect_uri={quote(redirect_uri).replace("/", "%2F")}
""".replace("\n", "")

webbrowser.open_new_tab(auth_url)