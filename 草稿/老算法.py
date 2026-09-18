import sys
from pathlib import Path


def 失败(消息):
    sys.stderr.write(消息 + "\n")
    raise SystemExit(1)


def 读数(文本):
    if 文本.count(".") > 1:
        return None
    if "." in 文本:
        整, 小 = 文本.split(".")
        if len(小) != 1 or not 小.isdigit():
            return None
        尾 = int(小)
    else:
        整 = 文本
        尾 = 0
    if not 整.isdigit():
        return None
    if len(整) > 1 and 整[0] == "0":
        return None
    if len(整) > 2:
        return None
    值 = int(整) + 尾 / 10.0
    if 值 > 10:
        return None
    return 值


def 分级(值):
    if 值 < 3:
        return "微震"
    if 值 < 4.5:
        return "有感"
    return "强震"


def 主():
    路径 = Path("震级")
    if not 路径.is_file():
        失败("找不到震级")
    原文 = 路径.read_text(encoding="utf-8")
    if 原文 == "":
        失败("震级不对")
    行 = 原文.split("\n")
    if 行 and 行[-1] == "":
        行.pop()
    if not 行:
        失败("震级不对")
    出 = []
    for 条 in 行:
        值 = 读数(条)
        if 值 is None:
            失败("震级不对")
        出.append("%s %s" % (条, 分级(值)))
    sys.stdout.write("\n".join(出) + "\n")


if __name__ == "__main__":
    主()
