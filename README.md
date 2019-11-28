# Description

Centreon deprecated many plugins and some people asked for `check_centreon_ping` command back.

This repository include code extracted from `centreon-web-2.8.30.tar.gz`, slightly modified to be able to run standalone as well as Debian and RPM packaging for easier deployment.

# Build package

For Debian package:

```
dpkg-buildpackage
```

For RPM package:

```
rpmbuild -ba check-centreon-ping.spec \
  --define "_sourcedir $PWD" \
  --define "_commit_date $(git log -1 --format=%cd --date=short |sed 's!-!!g')" \
  --define "_commit_hash $(git rev-parse --short HEAD)"
```
