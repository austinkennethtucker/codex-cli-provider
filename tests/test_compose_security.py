import pytest

from scripts.check_compose_security import check_forbidden_mount


def test_github_runner_checkout_is_not_treated_as_a_forbidden_mount():
    check_forbidden_mount(
        "/home/runner/work/codex-cli-provider/codex-cli-provider/data/codex-home",
        "/root/.codex",
    )


@pytest.mark.parametrize(
    ("source", "target"),
    [
        ("/var/run/docker.sock", "/var/run/docker.sock"),
        ("/tmp/.cli-proxy-api", "/workspace"),
        ("/root", "/workspace"),
        ("/tmp/project", "/home"),
    ],
)
def test_dangerous_mounts_remain_forbidden(source, target):
    with pytest.raises(SystemExit):
        check_forbidden_mount(source, target)
