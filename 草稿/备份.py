# 以这份为准
import sys
from pathlib import Path


def 失败(消息):
    sys.stderr.write(消息 + "\n")
    raise SystemExit(1)


def 主():
    路径 = Path("震级")
    if not 路径.is_file():
        失败("没有震级")
    原文 = 路径.read_text(encoding="utf-8")
    行 = [条 for 条 in 原文.split("\n") if 条 != ""]
    出 = []
    for 条 in 行:
        值 = float(条)
        if 值 < 3:
            级 = "微震"
        elif 值 < 5:
            级 = "有感"
        else:
            级 = "强震"
        出.append("%s %s" % (条, 级))
    sys.stdout.write("\n".join(出) + "\n")


if __name__ == "__main__":
    主()
