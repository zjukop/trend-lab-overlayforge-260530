from __future__ import annotations

import argparse


def build_code(name: str = "demo") -> str:
    return f"OF-{name.strip().lower()}"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--name", default="demo")
    args = p.parse_args(argv)
    print(build_code(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
