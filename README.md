# k3s RPM package for rpm-ostree based systems

This project provides a way to install [k3s](https://k3s.io/), a lightweight Kubernetes distribution, on rpm-ostree based systems like Fedora CoreOS where the traditional k3s setup script does not work.

rpm-ostree based systems use an image-based approach to the OS, combining the best features of a container (atomic updates, rollbacks) with those of a traditional Linux distribution (a familiar, mutable /etc, and fully integrated system). However, this model makes it challenging to install software that expects to be able to write to the host filesystem. The traditional k3s setup script is an example of such software.

This project solves this problem by packaging the k3s binary and its associated utility scripts into an RPM package that can be installed using rpm-ostree's package layering feature.

## Getting Started

Our GitHub Actions workflow automatically builds a new RPM package every 24 hours, ensuring that the RPM package stays up-to-date with the latest k3s release.

The built RPM package is uploaded as a GitHub Actions artifact. You can download the latest RPM package from the [Actions tab](https://github.com/pipelinedave/k3s-rpm/actions) of this repository.

## Installation

Once you've downloaded the RPM package, you can install it on your rpm-ostree based system with the following command:

```bash
sudo rpm-ostree install /path/to/your/downloaded/rpm/package.rpm
```

Replace /path/to/your/downloaded/rpm/package.rpm with the path to the downloaded RPM package. After installing the package, you'll need to reboot your system to apply the changes:

```bash
sudo systemctl reboot
```

After the reboot, k3s and its utility scripts should be installed and available on your system.
