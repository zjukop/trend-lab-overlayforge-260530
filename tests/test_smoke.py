from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from overlayforge.main import build_code, main


def test_smoke(capsys):
    assert build_code("Foo") == "OF-foo"
    assert main(["--name", "Bar"]) == 0
    assert capsys.readouterr().out.strip() == "OF-bar"
