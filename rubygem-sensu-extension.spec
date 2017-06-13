# Generated from sensu-extension-1.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-extension

Name:           rubygem-%{gem_name}
Version:        1.5.1
Release:        1%{?dist}
Summary:        The Sensu extension library
Group:          Development/Languages
License:        MIT
URL:            https://github.com/sensu/sensu-extension
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        https://github.com/sensu/%{gem_name}/archive/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(eventmachine)

Requires:       rubygem(eventmachine)

BuildArch:     noarch
%if 0%{?rhel}
Provides:      rubygem(%{gem_name}) = %{version}
%endif

%description
The Sensu extension library.


%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

install -d -p %{_builddir}%{gem_instdir}
tar -xvzf %{SOURCE1} -C %{_builddir}/%{gem_name}-%{version}/%{gem_instdir} --strip-components=1 %{gem_name}-%{version}/spec

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml}


# Run the test suite
%check
pushd .%{gem_instdir}
sed -i /codeclimate-test-reporter/d spec/helpers.rb
sed -i /CodeClimate::TestReporter.start/d spec/helpers.rb
rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md

%files doc
%doc %{gem_docdir}
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Mon Dec 19 2016 Martin Mágr <mmagr@redhat.com> - 1.5.1-1
- Updated to upstream version 1.5.1

* Thu May 05 2016 Martin Mágr <mmagr@redhat.com> - 1.5.0-1
- Updated to upstream version 1.5.0

* Thu Feb 25 2016 Martin Mágr <mmagr@redhat.com> - 1.3.0-1
- Updated to upstream version 1.3.0

* Tue Jan 27 2015 Graeme Gillies <ggillies@redhat.com> - 1.1.2-1
- Initial package
