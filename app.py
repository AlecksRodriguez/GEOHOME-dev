...

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False  # Token nunca expira
#app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False  # timedelta(minutes=3) # Token Expira en 3 minutos
app.config["JWT_SECRET_KEY"] = "Ge0HomeIsThePlaceWhereFantasyMeetsReality"
app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)

users = {} # Lista de usuarios - JWT

...
