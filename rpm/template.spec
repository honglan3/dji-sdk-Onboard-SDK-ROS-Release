Name:           ros-indigo-dji-sdk
Version:        0.1.9
Release:        0%{?dist}
Summary:        ROS dji_sdk package

Group:          Development/Libraries
License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-dji-sdk-lib
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dji-sdk-lib
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-std-msgs

%description
A ROS package using DJI Onboard SDK.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jun 14 2016 Norman Li <norman.li@dji.com> - 0.1.9-0
- Autogenerated by Bloom

* Sun Jun 12 2016 Norman Li <norman.li@dji.com> - 0.1.8-0
- Autogenerated by Bloom

* Thu Apr 21 2016 Norman Li <norman.li@dji.com> - 0.1.7-0
- Autogenerated by Bloom

* Wed Apr 13 2016 Norman Li <norman.li@dji.com> - 0.1.6-0
- Autogenerated by Bloom

* Thu Apr 07 2016 Norman Li <norman.li@dji.com> - 0.1.5-0
- Autogenerated by Bloom

* Sun Apr 03 2016 Norman Li <norman.li@dji.com> - 0.1.4-0
- Autogenerated by Bloom

* Wed Mar 30 2016 Norman Li <norman.li@dji.com> - 0.1.3-0
- Autogenerated by Bloom

* Wed Mar 30 2016 Norman Li <norman.li@dji.com> - 0.1.2-0
- Autogenerated by Bloom

* Tue Mar 29 2016 Norman Li <norman.li@dji.com> - 0.1.1-0
- Autogenerated by Bloom

* Fri Mar 25 2016 Norman Li <norman.li@dji.com> - 0.1.0-0
- Autogenerated by Bloom

