%define build_version 99.99.99.9999

Name:           libinvm-cli
Version:        %{build_version}
Release:        1%{?dist}
Summary:        Framework for Intel Storage CLI Binaries
License:        BSD
Group:          Development/Libraries
URL:            https://01.org/intel-nvm-cli-library
Source:         https://github.com/01org/intelnvmclilibrary/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:libinvm-i18n
BuildRequires:libinvm-i18n-devel

%description
Framework libraries for the Intel Storage CLI binaries

%package -n %{name}-devel
Summary:        Development files for %{name}
License:        BSD
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-devel
The %{name}-devel package contains header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
make BUILDNUM=%{build_version} RELEASE=1 CFLAGS_EXTERNAL="%{?cflag}"

%install
make install RELEASE=1 RPM_ROOT=%{buildroot} LIB_DIR=%{_libdir} INCLUDE_DIR=%{_includedir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%{_libdir}/libinvm-cli.so.*
%license LICENSE

%files -n %{name}-devel
%doc README.md
%{_libdir}/libinvm-cli.so
%{_includedir}/libinvm-cli
%license LICENSE

%changelog
* Thu Dec 24 2015 Nicholas Moulin <nicholas.w.moulin@intel.com> - 1.0.0.1094-1
- Initial rpm release