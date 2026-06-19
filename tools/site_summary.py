import json
from datetime import datetime

SITE_DATA = {
    "title": "爱游戏门户",
    "url": "https://portalcn-aiyouxi.com.cn",
    "keywords": ["爱游戏", "游戏门户", "游戏资讯", "游戏社区"],
    "description": "一个专注于游戏内容聚合与玩家交流的综合性门户平台。",
    "sections": [
        {"name": "首页推荐", "tags": ["热门", "推荐", "新游"]},
        {"name": "攻略中心", "tags": ["攻略", "技巧", "心得"]},
        {"name": "游戏评测", "tags": ["评测", "评分", "深度"]},
        {"name": "社区讨论", "tags": ["社区", "玩家", "讨论"]}
    ],
    "status": "active",
    "created": "2024-09-15",
    "last_updated": "2025-03-20"
}


def format_tags(tags):
    return " | ".join(sorted(set(tags)))


def build_summary(data):
    lines = []
    lines.append("=" * 50)
    lines.append(f"站点摘要 - {data['title']}")
    lines.append("=" * 50)
    lines.append(f"URL: {data['url']}")
    lines.append(f"关键词: {', '.join(data['keywords'])}")
    lines.append(f"说明: {data['description']}")
    lines.append(f"状态: {data['status']}")
    lines.append(f"创建日期: {data['created']}")
    lines.append(f"最近更新: {data['last_updated']}")
    lines.append(f"板块数量: {len(data['sections'])}")
    lines.append("-" * 50)
    for section in data["sections"]:
        tag_str = format_tags(section["tags"])
        lines.append(f"  · {section['name']:<12} 标签: {tag_str}")
    lines.append("-" * 50)
    return "\n".join(lines)


def export_as_json(data):
    export = {
        "site": data["title"],
        "url": data["url"],
        "keywords": data["keywords"],
        "description": data["description"],
        "status": data["status"],
        "section_count": len(data["sections"]),
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return json.dumps(export, ensure_ascii=False, indent=2)


def main():
    summary = build_summary(SITE_DATA)
    print(summary)
    print()
    print("--- JSON 导出 ---")
    print(export_as_json(SITE_DATA))
    print()
    print(f"摘要生成完成（{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}）")


if __name__ == "__main__":
    main()