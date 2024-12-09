#!/bin/sh
export AUTH0_DOMAIN="azy-coffeeshop.au.auth0.com"
export ALGORITHMS="RS256"
export API_AUDIENCE="fsnd-image"
export DATABASE_URL="postgresql://fsndcapstonedb_user:CQXvARZ3P7qdbEkMUEGQvCzffkapuFlE@dpg-ctagb5l6l47c73bmajl0-a.singapore-postgres.render.com/fsndcapstonedb"


export FLASK_APP=flaskr
export FLASK_DEBUG=True
export FLASK_ENVIRONMENT=debug