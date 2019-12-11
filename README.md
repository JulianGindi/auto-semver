# Auto Increment Semver

A portable python script that auto increments a semver tag for you based on remote git tags.

## Usage

Running from within a git directory.

`python auto_semver.py`

Specifying a specific remote.

`python auto_semver.py --remote git@github.com:JulianGindi/auto-increment-semver.git`

Auto-incrementing a minor version

`python auto_semver.py --highest-value minor`
