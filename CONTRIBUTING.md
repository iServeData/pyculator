# Contributing

Thanks for helping. Pyculator converts Linux file permissions between numeric and symbolic form.

## Get it running

Clone the repository (the **Code** button on GitHub), then from its folder:

```sh
python3 pyculator.py                  # type help at any prompt, quit to exit
python3 pyculator_setpermissions.py   # shows a file's permissions
```

Only the Python standard library is needed.

## Making a change

- Branch from `prototype` and open the pull request against `prototype`; `main` is what gets installed.
- Never commit real tokens, passwords, keys, IP addresses, Discord IDs, domains, or community, guild,
  channel, server or player names. Use placeholders such as `Example Community`,
  `community.example.org`, `203.0.113.10` and `000000000000000000`.
  CI runs `tools/check_generic.py`, which fails on addresses, IDs and private terms.
- Lowercase filenames with underscores, no spaces.
- Add a line to `CHANGELOG.md` describing the change.

## Security problems

Please don't open a public issue; see [SECURITY.md](SECURITY.md).
