[![Python package](https://github.com/0djentd/token-auth-cli/actions/workflows/python-package.yml/badge.svg)](https://github.com/0djentd/token-auth-cli/actions/workflows/python-package.yml)
[![Pylint](https://github.com/0djentd/token-auth-cli/actions/workflows/pylint.yml/badge.svg)](https://github.com/0djentd/token-auth-cli/actions/workflows/pylint.yml)
# token-auth-cli
## Description
Simple tool for testing token authentication during development.

## Installation
```
pip install token-auth-cli
```

## How to use
```
token-auth-cli --help
```
```
Usage: token-auth-cli [OPTIONS] COMMAND [ARGS]...

  token-auth-cli

  Simple tool for testing token authentication during development.

Options:
  --verbose / --no-verbose    Show additional information
  --debug / --no-debug        Show debug information
  --confirm-settings BOOLEAN  Confirm settings before trying to get token.
  --show-settings BOOLEAN     Show settings before trying to get token.
  --api TEXT                  API url.
  --api-get-token TEXT        API url to use when trying to get token.
  --api-get TEXT              API url to check if token valid.
  --config FILE               Config file.
  --store BOOLEAN             Store users/tokens.
  --help                      Show this message and exit.

Commands:
  init     Create config file and users/tokens storage.
  list     List stored users/tokens.
  login    Get token and store it.
  relogin  Try to use stored token for authentication.
  remove   Remove stored user/token.
```
