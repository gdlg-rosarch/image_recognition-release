Name:           ros-kinetic-image-recognition-rqt
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS image_recognition_rqt package

Group:          Development/Libraries
License:        TODO
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-image-recognition-msgs
Requires:       ros-kinetic-image-recognition-util
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rqt-gui
Requires:       ros-kinetic-rqt-gui-py
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-image-recognition-msgs
BuildRequires:  ros-kinetic-image-recognition-util
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-rqt-gui
BuildRequires:  ros-kinetic-rqt-gui-py

%description
The image_recognition_rqt package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Feb 07 2017 Rein Appeldoorn <reinzor@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Tue Feb 07 2017 Rein Appeldoorn <reinzor@gmail.com> - 0.0.2-2
- Autogenerated by Bloom

* Tue Jan 17 2017 Rein Appeldoorn <reinzor@gmail.com> - 0.0.2-1
- Autogenerated by Bloom

* Tue Jan 17 2017 Rein Appeldoorn <reinzor@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

