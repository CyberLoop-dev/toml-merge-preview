<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:0f766e&height=170&section=header&text=toml%20merge%20preview&fontSize=36&fontColor=ffffff&animation=twinkling" alt="Animated wave header"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2800&pause=900&color=14B8A6&center=true&vCenter=true&width=760&lines=toml%20merge%20preview%20%7C%20inspect%2C%20understand%2C%20improve" alt="Animated title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/toml-merge-preview?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/toml-merge-preview?style=for-the-badge" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/toml-merge-preview?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/toml-merge-preview?style=for-the-badge" alt="Last commit"/></p>
<p align="center"><img src="assets/mark.svg" alt="toml-merge-preview project mark" width="520"/></p>

## 🧭 Overview

`toml-merge-preview` combines multiple TOML files from lowest to highest precedence. Nested tables merge recursively, while later scalar values and arrays replace earlier values. It prints JSON and an optional conflict trace without modifying input files.

## ✨ Features

- 🧱 Merges nested TOML tables recursively
- ⬆️ Applies files in supplied order; later files take precedence
- 🧾 Explains overwritten values with dotted key paths and source filenames
- 🔒 Never edits the source configuration files
- 📤 Emits the merged result as JSON for inspection or piping

## 🧪 Demo

Run `python main.py sample/base.toml sample/local.toml --trace`. The final JSON shows the local port override while retaining the base logging table. No hosted demo is published.

## 🚀 Quick Start

```bash
python main.py sample/base.toml sample/local.toml --trace
python main.py defaults.toml staging.toml overrides.toml
python -m unittest discover -s tests
```
Requires Python 3.11 or newer. No third-party packages are needed.

## 🧰 Tech Stack

- **Stack:** Python 3.11+ (tomllib; standard library only)
- **Approach:** small, local-first tooling with clear output

## 🗂️ Folder Structure

```text
toml-merge-preview/
├── assets/mark.svg
├── sample/base.toml
├── sample/local.toml
├── tests/test_main.py
├── main.py
├── pyproject.toml
├── .gitignore
├── LICENSE
└── README.md
```

## 🛣️ Roadmap

- Add optional dotted-path allow and deny lists
- Add a compact Markdown conflict report

## 🤝 Contributing

Issues and focused pull requests are welcome. Explain the use case, keep changes small, and add tests for behavior changes. Run the project using the Quick Start instructions before submitting.

## 📄 License

Released under the [MIT License](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:0f172a&height=120&section=footer&animation=twinkling" alt="Animated wave footer"/></p>
