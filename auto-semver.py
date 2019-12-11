import re
import subprocess
import sys


def parse_semver_tags(raw_semver_text):
    regex_string = (
        "^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|"
        "[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-]"
        "[0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*"
        "))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*)"
        ")?$"
    )

    regex = re.compile(regex_string)


def get_remote_git_tags():
    # Git command to list remote tags, only grabbing tags and not the
    # commit hashes.
    git_tag_command = ["git", "ls-remote", "--tags", "-q"]
    awk_command = ["awk", "'{print $2}'"]

    subprocess.Popen(git_tag_command, stdout=subprocess.PIPE)
    command_process = subprocess.Popen(awk_command, stdin=subprocess.PIPE)
    command_output = command_process.stdout()

    # Checking to make sure our command succeeded. The stdout() function
    # returns None if the command fails and there is no output.
    if command_output is None:
        sys.exit("Error getting tags from remote")
    elif len(command_output) == 0:
        # There are no returned tags, writing a message to stdout and exiting.
        print("No tags found. Nothing to do.")
        sys.exit(0)

    return command_output


def auto_increment_semver_tags():
    remote_tag_text = get_remote_git_tags()
    print(remote_tag_text)


if __name__ == "__main__":
    auto_increment_semver_tags()
