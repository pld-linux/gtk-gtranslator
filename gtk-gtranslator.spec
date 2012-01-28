# TODO
# - hardcoded to translate: langpair=en%7Czh-CN&text=
# - does not seem to work
Summary:	Translate sentences in clipboard using translate.google.com
Name:		gtk-gtranslator
Version:	0.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	%{name}-2.tar.bz2
# Source0-md5:	d128263eb17cc2ce283b41695f31b80f
URL:		https://code.google.com/p/gtk-gtranslator/
BuildRequires:	GConf2-devel
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Translate sentences in clipboard using translate.google.com.

%prep
%setup -q -n %{name}

%build
# NOTE: not autoconf generated configure
./configure \
	--prefix=%{_prefix}
%{__make} gtranslator gconf-keybinding \
	CC="%{__cc} %{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p gtranslator gconf-keybinding $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtranslator
%attr(755,root,root) %{_bindir}/gconf-keybinding
