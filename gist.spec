%define name	gist
%define version 3.1.0
%define release 1

Summary:	Command line gister
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
License:	MIT
Group:		Development/Other
Url:		https://github.com/defunkt/gist/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	ruby
BuildRequires:	ruby-RubyGems
Provides:	rubygem(%{name})

%description
Creates Gists (pastes) on gist.github.com from standard input or
arbitrary files. Can link to your GitHub account, create private
gists, and enable syntax highlighting.

%prep
%setup -q

%install
%__rm -rf %{buildroot}
gem install --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

%__install -m 755 -d %{buildroot}%{_mandir}
mv %{buildroot}%{ruby_gemdir}/bin %{buildroot}%{_prefix}
rm -f %{buildroot}%{ruby_gemdir}/gems/%{name}-%{version}/man/*ron
rm -f %{buildroot}%{ruby_gemdir}/gems/%{name}-%{version}/man/*html
mv %{buildroot}%{ruby_gemdir}/gems/%{name}-%{version}/man %{buildroot}%{_mandir}/man1

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{name}-%{version}
%_bindir/gist
%_mandir/man1/gist.*
%attr(755,root,root) %{ruby_gemdir}/cache/%{name}-%{version}.gem
%{ruby_gemdir}/specifications/%{name}-%{version}.gemspec
%{ruby_gemdir}/gems/%{name}-%{version}

