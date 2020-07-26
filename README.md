# SocialAuthDjango

Creating social auth with GitHub, Google, Twitter and API authentication.

## Installing

Install requirements

```sh
pip install -r requirements.txt
```

Install all repository dependencies

```sh
yarn install
```

## Configuring

Create a `.env` file and fill it with the respective information present in `.env.example`

```env
SECRET_KEY = random_string
GOOGLE_CLIENT_ID = OAuth_client_id
GOOGLE_CLIENT_SECRET = OAuth_client_secret
```

## Building CSS

Build main css using postcss

```sh
yarn run build:css
```

Build main css using npx

```sh
yarn run dev:css
```

Build tailwind in specific app

```sh
yarn run authentication:css
```
