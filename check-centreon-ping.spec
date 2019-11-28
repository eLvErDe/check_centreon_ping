Name:       check-centreon-ping
Version:    0.0.%{_commit_date}.%{_commit_hash}
Release:    1
Summary:    Legacy Centreon monitoring check_centreon_ping command
License:    GPLv2
Requires:   perl
Requires:   nagios-plugins-perl
Requires:   iputils

%description
Extracted from Centreon Web 2/8.30 archive and modified to run
standalone.

%install
mkdir -p %{buildroot}%{_libdir}/nagios/plugins
sed 's!@NAGIOS_PLUGINS@!%{_libdir}/nagios/plugins!' %{_sourcedir}/check_centreon_ping > %{buildroot}%{_libdir}/nagios/plugins/check_centreon_ping
chmod 0755 %{buildroot}%{_libdir}/nagios/plugins/check_centreon_ping

%files
%{_libdir}/nagios/plugins/check_centreon_ping
