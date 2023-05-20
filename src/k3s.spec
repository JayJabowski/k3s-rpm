Name: k3s
Version: 0.0.1
Release: 1%{?dist}
Summary: Lightweight Kubernetes

License: Apache-2.0
URL: https://k3s.io/

Source0: ./k3s
Source1: ./k3s-uninstall.sh
Source2: ./k3s-agent-uninstall.sh
Source3: ./k3s-killall.sh
Source4: ./k3s.bash-completion

BuildArch: x86_64

%description
k3s is a highly available, certified Kubernetes distribution designed
for production workloads in unattended, resource-constrained, remote
locations or inside IoT appliances.

%prep

%install
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/etc/bash_completion.d
cp %{SOURCE0} %{buildroot}/usr/local/bin/k3s
cp %{SOURCE1} %{buildroot}/usr/local/bin/k3s-uninstall.sh
cp %{SOURCE1} %{buildroot}/usr/local/bin/k3s-agent-uninstall.sh
cp %{SOURCE3} %{buildroot}/usr/local/bin/k3s-killall.sh
cp %{SOURCE4} %{buildroot}/etc/bash_completion.d/k3s
chmod +x %{buildroot}/usr/local/bin/k3s
chmod +x %{buildroot}/usr/local/bin/k3s-uninstall.sh

%files
/usr/local/bin/k3s
/usr/local/bin/k3s-uninstall.sh
/etc/bash_completion.d/k3s

%changelog
