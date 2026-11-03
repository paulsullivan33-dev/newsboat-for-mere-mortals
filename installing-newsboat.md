# Installing Newsboat

Outcome: Newsboat and Podboat on your
machine, and a version command that proves
they run. This chapter has two roads: the
short one most people take, and the one
the lab was forced onto — which is also
the one you will need if your system turns
out to be missing the package.

## The short road: your distribution's package

Newsboat is packaged by most Linux
distributions and the BSDs, and the
project's own advice is to take the
package where one exists. One command is
usually the whole job:

```bash
sudo apt install newsboat
```

(Debian and older Ubuntu releases carry
it; so do Fedora, Arch, openSUSE, and
Homebrew on macOS.) Podboat arrives in the
same package. Prove it:

```text
$ newsboat --version
Newsboat 2.34.1 - https://newsboat.org/
```

## The gap: when there is no package

The lab's machine ran Ubuntu 24.04, and
there the short road ends at a fence:

```text
$ apt-cache policy newsboat
newsboat:
  Installed: (none)
  Candidate: (none)
```

No candidate at all — not an old version,
nothing. (The package was dropped from
that release; it happens to tools whose
build requirements move faster than a
frozen distribution.) The lab did not take
that on trust from one command: it also
searched the release's raw package index
and found exactly one mention of the word,
as a suggestion inside an unrelated
package. When the package is genuinely
absent, the project's documented route is
the source build below. FreeBSD, or a
distribution that still packages Newsboat,
never makes you take it.

## The build road: the release tarball

Newsboat is written in C++ with a Rust
library inside, so the build needs both
toolchains plus a row of development
libraries. The project's README lists
them; on a Debian-family system the set
the lab installed was:

```bash
sudo apt install g++ make pkg-config cargo rustc \
  libsqlite3-dev libcurl4-openssl-dev libxml2-dev \
  libstfl-dev libjson-c-dev libncurses-dev gettext
```

Then the official release tarball — from
the project's own site, not a mirror:

```bash
curl -sLO https://newsboat.org/releases/2.34.1/newsboat-2.34.1.tar.xz
sha256sum newsboat-2.34.1.tar.xz
# 11edb1399339ea6dac348a7ed4baa1b5a799ed899c478ea777496bc143df708a
tar -xf newsboat-2.34.1.tar.xz
cd newsboat-2.34.1
make -j2 newsboat podboat
sudo make install     # or run ./newsboat in place, as the lab did
```

On the lab's two-core machine the compile
took about six and a half minutes. The
check is the same version command as
above; a full `-vv` adds the library
versions Newsboat was built against
(SQLite, libcurl, libxml2), which is the
output to quote if you ever report a bug.

## Which release? A toolchain ceiling, honestly

The lab built **2.34.1**, not the newest
release, and the reason is worth stating
because you may meet it too. Each release
states a minimum Rust version (2.34.1 asks
for Rust 1.70). The newest releases have
moved to Rust's 2024 edition, which needs
a much newer compiler than the lab
machine's distribution provides (its cargo
is 1.75). So the rule is: build the newest
release your toolchain satisfies. The
lab verified both ends of that claim —
the 2.34.1 requirement in its README, and
`edition = "2024"` in the current
release's manifest — and everything in
the following chapters is 2.34.1's
behaviour, which differs from the newest
only in details the project lists in its
changelog.

Check: `newsboat --version` answers, and
`podboat --version` answers with the same
number. Next chapter puts feeds in front
of them.
