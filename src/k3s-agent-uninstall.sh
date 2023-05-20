#!/bin/sh
[ "$(id -u)" -eq 0 ] || exec sudo $0

for cmd in "k3s-killall.sh" "k3s-agent"; do
  if command -v $cmd >/dev/null 2>&1; then
    $cmd
  fi
done

systemctl disable --now k3s-agent

if which systemctl >/dev/null 2>&1; then
  SYSTEMD_RELOAD=true
  systemctl daemon-reload
fi

if [ -f /etc/systemd/system/k3s-agent.service ]; then
  rm -f /etc/systemd/system/k3s-agent.service
fi

if [ -d /etc/systemd/system/k3s-agent.service.d ]; then
  rm -Rf /etc/systemd/system/k3s-agent.service.d
fi

if [ "$SYSTEMD_RELOAD" = true ]; then
  systemctl reset-failed
fi

rm -f \
  /etc/systemd/system/k3s-agent.service \
  /usr/local/bin/k3s \
  /usr/local/bin/kubectl \
  /usr/local/bin/crictl \
  /usr/local/bin/ctr \
  /var/lib/rancher/k3s \
  /var/lib/kubelet \
  /etc/cni/net.d \
  /var/lib/cni \
  /var/run/calico

echo "Uninstalled k3s"
