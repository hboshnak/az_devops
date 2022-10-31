from click.testing import CliRunner
from main import main

def test_main():
    runner = CliRunner()
    result = runner.invoke(main, ["--name", "Mani", "--color", "black"])
    assert "Mani" in result.output