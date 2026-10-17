*This project has been created as part of the 42 curriculum by myohann-.*

# Born2beroot

## Description
**Born2beroot** is a project about Virtual Machine part of the 42 curriculum.

**'GOAL'**: -Experiments and Learn the installation, seting up and utilisation of the Virtual Machine by setting up a linux server inside a virtual machine by following strict rules and with no graphical interface.

The project covers: virtualization, disk patitioning with LVM encription, user and group management, firewall configuration, SSH hardening, sudo policies, password policies, and automated monitoring scripts.

In this project, the use of VirtualBox (or UTM if VirtualBox is not available) is mandatory. So we Simply submit a signature.txt file to the root of the repository and paste the signature of your machine's virtual disk into it.

---

## Project Description

### Operating System Choice: Debian

I chose **Debian** over Rocky Linux for the following reasons:

| | Debian | Rocky Linux |
|---|---|---|
| **Difficulty** | Recommended for beginners | More complex setup |
| **Package manager** | APT (apt, aptitude) | DNF |
| **Security module** | AppArmor | SELinux |
| **Firewall** | UFW | firewalld |
| **Community** | Very large, lots of documentation | Smaller, enterprise-focused |

**Advantages of Debian:** Stable, well-documented, huge community, easy to learn.
**Disadvantages of Debian:** Packages can be slightly older than other distros.

---

### AppArmor vs SELinux

| | AppArmor | SELinux |
|---|---|---|
| **Used on** | Debian, Ubuntu | Rocky, RHEL, Fedora |
| **Approach** | Path-based profiles | Label-based (type enforcement) |
| **Complexity** | Easier to configure | More complex but more powerful |
| **Default mode** | Enforce or Complain | Enforcing or Permissive |

Both implement **MAC (Mandatory Access Control)**. AppArmor was chosen because it integrates naturally with Debian and is easier to manage.

---

### UFW vs firewalld

| | UFW | firewalld |
|---|---|---|
| **Used on** | Debian, Ubuntu | Rocky, RHEL, Fedora |
| **Complexity** | Simple, beginner-friendly | More complex, zone-based |
| **Backend** | iptables / nftables | nftables |
| **Dynamic rules** | No (requires reload) | Yes (without interrupting connections) |

---

### VirtualBox vs UTM

| | VirtualBox | UTM |
|---|---|---|
| **Platform** | Windows, Linux, macOS (Intel) | macOS (Apple Silicon M1/M2) |
| **Price** | Free | Free |
| **Performance** | Good on x86 | Good on Apple Silicon |

### Main Design Choices

#### Partitioning

The disk is partitioned using **LVM (Logical Volume Manager)** on top of **LUKS encryption (Linux Unified Key Setup)**. This setup follows the bonus partition scheme required by the subject.

**Why LVM?**
LVM adds a flexible abstraction layer between physical disks and the filesystem. Volumes can be resized, added, or snapshotted without repartitioning the disk.

**Why LUKS encryption?**
LUKS encrypts the entire volume group so that data on the disk cannot be read without the passphrase, even if the physical disk is stolen.

**Partition structure (bonus scheme):**

| Mount point | Type | Size | Purpose |
|---|---|---|---|
| `/boot` | Primary (unencrypted) | 500 MB | Bootloader and kernel — must remain unencrypted |
| `sda5_crypt` | LUKS encrypted | rest of disk | Container for all LVM volumes |
| `/` | LVM logical volume | 10 GB | Root filesystem |
| `/swap` | LVM logical volume | 2.3 GB | Swap space |
| `/home` | LVM logical volume | 5 GB | User data |
| `/var` | LVM logical volume | 3 GB | Variable data (logs, packages) |
| `/srv` | LVM logical volume | 3 GB | Service data (web, FTP) |
| `/tmp` | LVM logical volume | 3 GB | Temporary files |
| `/var/log` | LVM logical volume | 4 GB | System logs isolated for security |

**Why separate `/var/log`?**
Isolating logs prevents a log flood from filling up `/` and crashing the system.

**Why separate `/home`?**
Isolating user data allows reinstalling the OS without losing user files.

---

## Instructions

### Virtual Machine signature
The VM signature change when the VM parent system is lanch instead of a clone.
command to show the signature(in your ):
```bash
sha1sum Born2beroot.vdi
```
after a some minutes it show:
```text
```

### AppArmor
```bash
# Check AppArmor status
systemctl status apparmor

# Check loaded profiles
/usr/sbin/aa-status

# Verify AppArmor starts at boot
systemctl is-enabled apparmor
```

### SSH Configuration
```bash
# Check SSH service status
systemctl status ssh

# Check SSH config: port and root login
grep Port /etc/ssh/sshd_config
grep PermitRootLogin /etc/ssh/sshd_config
```

### UFW Firewall
```bash
# Check UFW status and rules
sudo /usr/sbin/ufw status

# Check UFW verbose (default policy)
sudo /usr/sbin/ufw status verbose

# Check UFW starts at boot
systemctl is-enabled ufw
```

### users and Group
```bash
# Check groups of myohann-
groups myohann-

# Check members of sudo group
getent group sudo

# Check members of user42 group
getent group user42

# Full user info
id myohann-
```
### Password Policies
```bash
# Check password expiry rules for nfitahin
sudo chage -l nfitahin

# Check password expiry rules for root
sudo chage -l root
```

### Sudo Configuration
```bash
# Check sudo is installed
which sudo
sudo --version

# Check sudoers config file
sudo cat /etc/sudoers

# Verify sudoers syntax is correct
sudo visudo -c

# Check sudo log folder exists
ls -la /var/log/sudo/

# Read sudo logs
sudo cat /var/log/sudo/sudo.log

# Run a command with sudo then verify it appears in logs
sudo apt update
sudo cat /var/log/sudo/sudo.log
```

### Hostname and Partitions
```bash
# Check current hostname
hostname
hostnamectl
cat /etc/hostname
```

### Monitoring script
```bash
# Show the script content
cat /usr/local/bin/monitoring.sh

# Run the script manually
/usr/local/bin/monitoring.sh

# Check script permissions
ls -la /usr/local/bin/monitoring.sh

# Check cron configuration
sudo crontab -l
```

## Ressources
- [Debian Official Documentation](https://www.debian.org/doc/)
- [AppArmor Wiki Debian](https://wiki.debian.org/AppArmor)
- [UFW Manual](https://manpages.debian.org/buster/ufw/ufw.8.en.html)
- [LVM Guide - ArchWiki](https://wiki.archlinux.org/title/LVM)
- [LUKS/dm-crypt - ArchWiki](https://wiki.archlinux.org/title/Dm-crypt)
- [WordPress Documentation](https://wordpress.org/documentation/)
- [Fail2ban Documentation](https://www.fail2ban.org/wiki/index.php/Main_Page)
- [SSH Hardening Guide](https://www.ssh.com/academy/ssh/config)
- [Cron Documentation](https://manpages.debian.org/buster/cron/crontab.5.en.html)
- [MariaDB Documentation](https://mariadb.com/kb/en/documentation/)

### AI Usage
Claude (by Anthropic) was used as a learning assistant during this project for:
- **Understanding concepts**: AppArmor, LVM, UFW, SSH, cron, sudo policies, Fail2ban
- **Debugging**: identifying and fixing errors in configuration files and the monitoring script
- **Verification**: checking that commands produce the expected results
- **Explanations**: understanding what each command does and why it is needed

AI was used as a guide and explainer. Each command was executed, tested, and understood before moving on.


partition primaire et logique explique
MBR GPT
