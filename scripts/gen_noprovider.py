#!/usr/bin/env python3
"""由 src/liqun_example.yaml 生成 src/liqun_example_noprovider.yaml。

只做两处删除，其余内容（注释、空行、缩进、行尾）逐字节保留：

1. 顶格键 ``base-provider``：即 ``base-provider: &base-provider { ... }`` 这行锚点定义，
   连同紧邻其上的注释块（当前为 ``# 机场设置锚点``）。
2. 顶格键 ``proxy-providers``：整个字段及其所有子行。

唯一例外：被删字段位于文件末尾时，其上方那行分隔空行会残留成"末尾多一个空行"，
因此输出会去掉文件尾部空行，让文件仍以最后一行内容结尾。

删除后若仍有被删锚点的引用（``*base-provider``）会直接报错，避免生成出坏配置；
源文件里本来就没有这两个键时只提示，不报错。
脚本不依赖任何第三方库，可在本地或 CI 中直接运行：``python3 scripts/gen_noprovider.py``。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE = REPO_ROOT / "src" / "liqun_example.yaml"
TARGET = SOURCE.with_name("liqun_example_noprovider.yaml")

# 需要删除的顶格键。键名同时作为锚点名，删除后会检查是否还被引用。
REMOVE_KEYS = ("base-provider", "proxy-providers")

# 顶格「键: 值」形式，键名限定为不含空白的常见字符，避免误伤注释与列表项。
TOP_LEVEL_KEY = re.compile(r"^([A-Za-z0-9_.\-]+)\s*:\s*(.*)$")


class GenerateError(RuntimeError):
    """源文件结构不符合预期时抛出，避免静默生成错误结果。"""


def is_blank(line: str) -> bool:
    return line.strip() == ""


def is_comment(line: str) -> bool:
    return line.lstrip().startswith("#")


def is_indented(line: str) -> bool:
    return line[:1] in (" ", "\t")


def attached_comment_start(lines: list[str], index: int) -> int:
    """返回紧邻 index 之上、中间无空行隔断的连续注释块起始行号。"""
    start = index
    while start > 0 and is_comment(lines[start - 1]) and not is_blank(lines[start - 1]):
        start -= 1
    return start


def block_end(lines: list[str], index: int) -> int:
    """返回顶格键 index 的块结束位置（不含）。

    规则：吃掉所有缩进行；空行只有在后面仍跟着缩进行（即块内空行）时才吃掉，
    其他情况留给后续内容，保证块外的空行原样保留。
    """
    end = index + 1
    while end < len(lines):
        line = lines[end]
        if is_indented(line) and not is_blank(line):
            end += 1
            continue
        if is_blank(line):
            lookahead = end
            while lookahead < len(lines) and is_blank(lines[lookahead]):
                lookahead += 1
            if lookahead < len(lines) and is_indented(lines[lookahead]):
                end = lookahead
                continue
        break
    return end


def generate(text: str) -> str:
    lines = text.splitlines(keepends=True)  # 保留每行原始行尾
    body = [line.rstrip("\r\n") for line in lines]
    drop = [False] * len(lines)
    removed: list[str] = []

    for index, line in enumerate(body):
        match = TOP_LEVEL_KEY.match(line)
        if not match or match.group(1) not in REMOVE_KEYS:
            continue
        key = match.group(1)
        comment_start = attached_comment_start(body, index)
        for j in range(comment_start, index):
            drop[j] = True
        end = block_end(body, index)
        for j in range(index, end):
            drop[j] = True
        removed.append(key)

    missing = [key for key in REMOVE_KEYS if key not in removed]
    if missing:
        print(
            "提示：源文件中没有这些顶格键，跳过删除："
            + ", ".join(missing)
            + f"（{SOURCE.name} 可能已改过，仅作提示）",
            file=sys.stderr,
        )

    keep = [line for line, gone in zip(lines, drop) if not gone]

    # 被删块位于文件末尾时，其上方的分隔空行会残留成"末尾多一个空行"，
    # 这里去掉文件尾部空行；最后一行内容自带的行尾原样保留。
    while keep and keep[-1].strip() == "":
        keep.pop()

    result = "".join(keep)

    for key in REMOVE_KEYS:
        if re.search(rf"\*{re.escape(key)}\b", result):
            raise GenerateError(f"删除后仍存在锚点引用 *{key}，请先处理引用再生成")

    return result


def main() -> int:
    if not SOURCE.is_file():
        print(f"错误：找不到源文件 {SOURCE}", file=sys.stderr)
        return 1

    text = SOURCE.read_text(encoding="utf-8", newline="")
    output = generate(text)

    if TARGET.is_file() and TARGET.read_text(encoding="utf-8", newline="") == output:
        print(f"{TARGET.name} 已是最新，无需写入。")
        return 0

    TARGET.write_text(output, encoding="utf-8", newline="")
    print(f"已生成 {TARGET.relative_to(REPO_ROOT)}（{len(output.splitlines())} 行）")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GenerateError as error:
        print(f"错误：{error}", file=sys.stderr)
        sys.exit(1)
