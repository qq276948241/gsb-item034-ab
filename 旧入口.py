import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "散页"))
from 界限 import 分级

def 主():
    原文 = Path("震级").read_text(encoding="utf-8")
    行 = [条 for 条 in 原文.split("\n") if 条 != ""]
    出 = []
    for 条 in 行:
        出.append("%s %s" % (条, 分级(float(条))))
    sys.stdout.write("\n".join(出) + "\n")

if __name__ == "__main__":
    主()
