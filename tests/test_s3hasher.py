
from click.testing import CliRunner

from s3hasher.cli import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0

import subprocess
def test_module():
    rc = subprocess.check_call(['python','-ms3hasher'])
    assert rc == 0
