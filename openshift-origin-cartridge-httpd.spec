%global cartridgedir %{_libexecdir}/openshift/cartridges/httpd

Summary:       Apache Httpd cartridge for V2 Cartridge SDK
Name:          openshift-origin-cartridge-httpd
Version:       1.0.0
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           https://www.openshift.com
Source0:       https://github.com/misho-kr/openshift-cartridge-httpd/archive/master.zip
Requires:      facter
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
BuildArch:     noarch

%description
Provides a simple cartridge for use in the V2 Cartridge SDK. It runs Apache httpd
server that can serve static content, and with suitable changes to the configuration
file it will run CGI scripts, support SSI and more.

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Sat Nov 2 2013 Misho Krastev <misho.kr+github@gmail.com> 1.0.0-1
- Initial files checking
