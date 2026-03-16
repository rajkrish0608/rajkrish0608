#!/usr/bin/env python3
"""
Auto-update Tech Stack Data from GitHub API
Runs via GitHub Actions to keep techstack-data.json fresh.
"""

import json
import os
import urllib.request
import urllib.error

GITHUB_USERNAME = "rajkrish0608"
GITHUB_TOKEN    = os.environ.get("GITHUB_TOKEN", "")

# Manual tech stack with project mappings — this is the ground truth.
# Languages/frameworks detected via API AUGMENT this list.
TECH_MANIFEST = {
    # ── AI / ML ──────────────────────────────────────────────────────────────
    "Python":       {"domain": "AI / ML",  "r": 62, "detect": ["Python"],     "projects": ["SellSenseAI", "IoT Inventory Optimizer", "Engineering Skills Radar"]},
    "TensorFlow":   {"domain": "AI / ML",  "r": 54, "detect": [],             "projects": ["Swasth-AI", "Medical image analysis pipeline"]},
    "OpenCV":       {"domain": "AI / ML",  "r": 46, "detect": [],             "projects": ["Swasth-AI", "Agri-Guard", "Visual detection"]},
    "scikit-learn": {"domain": "AI / ML",  "r": 45, "detect": [],             "projects": ["SellSenseAI", "Engineering Skills Radar"]},
    "XGBoost":      {"domain": "AI / ML",  "r": 40, "detect": [],             "projects": ["SellSenseAI", "Classification models"]},
    "HuggingFace":  {"domain": "AI / ML",  "r": 44, "detect": [],             "projects": ["Swasth-AI", "Legal-Clarity-AI", "NLP pipelines"]},
    "Flask":        {"domain": "AI / ML",  "r": 38, "detect": [],             "projects": ["SellSenseAI", "Agri-Guard", "AI REST APIs"]},
    # ── Security / Systems ───────────────────────────────────────────────────
    "Linux":        {"domain": "Security", "r": 52, "detect": [],             "projects": ["ZenithOS", "Raspberry Pi rover", "Server hardening"]},
    "Cybersecurity":{"domain": "Security", "r": 58, "detect": [],             "projects": ["ZenithOS", "Penetration testing", "Network security"]},
    "IoT / ESP32":  {"domain": "Security", "r": 50, "detect": [],             "projects": ["IoT Inventory Optimizer", "Health Monitor"]},
    "C++":          {"domain": "Security", "r": 44, "detect": ["C++"],        "projects": ["ZenithOS", "Robotics rover", "Embedded systems"]},
    "Rust":         {"domain": "Security", "r": 46, "detect": ["Rust"],       "projects": ["ZenithOS kernel"]},
    # ── Web / Mobile ─────────────────────────────────────────────────────────
    "TypeScript":   {"domain": "Web",      "r": 62, "detect": ["TypeScript"], "projects": ["DataSaathi", "WorkProof", "HireFlow", "ClipForge", "BillSentry-Health"]},
    "React":        {"domain": "Web",      "r": 50, "detect": [],             "projects": ["Final Portfolio", "KINETIKA website", "HireFlow"]},
    "Next.js":      {"domain": "Web",      "r": 48, "detect": [],             "projects": ["CivicGPT", "Legal-Clarity-AI", "LinkRaft"]},
    "Node.js":      {"domain": "Web",      "r": 46, "detect": [],             "projects": ["CivicGPT", "HireFlow", "msme-digital-backbone"]},
    "MongoDB":      {"domain": "Web",      "r": 42, "detect": [],             "projects": ["HireFlow", "CivicGPT", "LinkRaft"]},
    "Flutter":      {"domain": "Web",      "r": 54, "detect": ["Dart"],       "projects": ["Offline Survival Companion", "Rent-Ledger"]},
    "JavaScript":   {"domain": "Web",      "r": 44, "detect": ["JavaScript"], "projects": ["My Portfolio", "Govt-Notice-Checker", "algo-nirman"]},
    "HTML / CSS":   {"domain": "Web",      "r": 40, "detect": ["HTML", "CSS"],"projects": ["Agri-Guard", "Vedic Asharam site"]},
    "Socket.io":    {"domain": "Web",      "r": 38, "detect": [],             "projects": ["Real-time apps", "CivicGPT live features"]},
    # ── Tools / Infra ─────────────────────────────────────────────────────────
    "Git / GitHub": {"domain": "Tools",    "r": 48, "detect": [],             "projects": ["All 49+ repositories"]},
    "Docker":       {"domain": "Tools",    "r": 42, "detect": [],             "projects": ["DataSaathi", "Backend deployments"]},
    "Vercel":       {"domain": "Tools",    "r": 40, "detect": [],             "projects": ["Final Portfolio", "CivicGPT", "HireFlow"]},
    "Algorand":     {"domain": "Tools",    "r": 46, "detect": [],             "projects": ["DataSaathi — DPDP Act platform"]},
    "Solidity":     {"domain": "Tools",    "r": 40, "detect": ["Solidity"],   "projects": ["WorkProof", "DataSaathi smart contracts"]},
    "Figma":        {"domain": "Tools",    "r": 38, "detect": [],             "projects": ["KINETIKA design", "UI prototypes"]},
    "Java":         {"domain": "Tools",    "r": 36, "detect": ["Java"],       "projects": ["GFG-160-Days-Challenge", "DSA practice"]},
}


def gh_get(path):
    url = f"https://api.github.com/{path}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "techstack-updater",
    })
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} for {url}")
        return None


def fetch_all_repos():
    repos, page = [], 1
    while True:
        data = gh_get(f"users/{GITHUB_USERNAME}/repos?per_page=100&page={page}&type=public")
        if not data:
            break
        repos.extend(data)
        if len(data) < 100:
            break
        page += 1
    return repos


def fetch_repo_languages(repo_name):
    data = gh_get(f"repos/{GITHUB_USERNAME}/{repo_name}/languages")
    return data or {}


def get_language_bytes():
    """Aggregate total bytes per language across all repos."""
    print(f"Fetching repos for {GITHUB_USERNAME}...")
    repos = fetch_all_repos()
    print(f"  Found {len(repos)} public repos")

    lang_bytes = {}
    for repo in repos:
        if repo.get("fork"):
            continue
        langs = fetch_repo_languages(repo["name"])
        for lang, count in langs.items():
            lang_bytes[lang] = lang_bytes.get(lang, 0) + count

    return lang_bytes


def build_techstack(lang_bytes):
    """Merge detected languages with manifest, compute radius from bytes."""
    total = sum(lang_bytes.values()) or 1
    stack = {}

    # Start from manifest
    for name, info in TECH_MANIFEST.items():
        entry = {
            "name":     name,
            "domain":   info["domain"],
            "r":        info["r"],
            "projects": info["projects"],
            "bytes":    0,
        }

        # Sum bytes for any detected language keys
        for detect_key in info.get("detect", []):
            entry["bytes"] += lang_bytes.get(detect_key, 0)

        stack[name] = entry

    # Adjust radius for detected languages based on actual byte share
    detected_names = {k for v in TECH_MANIFEST.values() for k in v.get("detect", [])}
    for name, entry in stack.items():
        if entry["bytes"] > 0:
            pct = entry["bytes"] / total
            base = TECH_MANIFEST[name]["r"]
            # Blend: 70% base + 30% dynamic (capped at +15/-10)
            dynamic = min(80, max(30, 35 + pct * 500))
            entry["r"] = round(base * 0.7 + dynamic * 0.3)

    # Add any completely new languages not in manifest
    for lang, b in lang_bytes.items():
        if lang in detected_names:
            continue
        if b / total < 0.005:      # < 0.5% — skip noise
            continue
        if lang not in [v for info in TECH_MANIFEST.values() for v in info.get("detect", [])]:
            stack[lang] = {
                "name":     lang,
                "domain":   "Web",
                "r":        max(30, min(50, round(30 + (b/total)*300))),
                "projects": ["Detected in repositories"],
                "bytes":    b,
            }

    return list(stack.values())


def write_json(tech_list, lang_bytes):
    out = {
        "updated":      __import__("datetime").datetime.utcnow().isoformat() + "Z",
        "username":     GITHUB_USERNAME,
        "lang_bytes":   {k: v for k, v in sorted(lang_bytes.items(), key=lambda x: -x[1])[:20]},
        "tech_stack":   tech_list,
    }
    with open("techstack-data.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote techstack-data.json with {len(tech_list)} entries")


if __name__ == "__main__":
    if not GITHUB_TOKEN:
        print("WARNING: No GITHUB_TOKEN — rate limits will apply")
    lang_bytes = get_language_bytes()
    tech_list  = build_techstack(lang_bytes)
    write_json(tech_list, lang_bytes)
    print("Done.")
