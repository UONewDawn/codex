# New Dawn Codex

The comprehensive wiki and knowledge base for New Dawn, an Ultima Online server.

**Live Site:** [https://codex.uonewdawn.com](https://codex.uonewdawn.com)

## Contributing to the Codex

This repository contains the source for the New Dawn Codex, built with [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. We welcome contributions from the community!

When you submit changes via pull request, they will be automatically deployed to the live site once merged to the `main` branch.

### Quick Edit on GitHub

**Don't want to set up a local environment?** You can contribute directly through GitHub's web interface:

1. **Navigate to the file** you want to edit in the [repository](https://github.com/UONewDawn/Codex)
2. **Click the pencil icon** (✏️) in the top-right corner of the file view
3. **Make your changes** in the GitHub editor
4. **Preview your changes** using the "Preview" tab
5. **Propose changes** by filling out the commit message at the bottom
6. **Create a pull request** - GitHub will automatically fork the repo and create a PR for you

This is perfect for fixing typos, updating content, or making small improvements without needing to install anything locally!

## Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Setup

1. **Fork and clone the repository:**

```bash
git clone https://github.com/UONewDawn/Codex.git
cd Codex
```

2. **Create a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the development server:**

```bash
mkdocs serve
```

5. **Open your browser to [http://localhost:8000](http://localhost:8000)**

The site will automatically reload when you make changes to the documentation!

## Content Structure

Try to contain you changes within the existing structure. If you're unsure, please reach out.

## Making Changes

### Adding New Pages

1. Create a new `.md` file in the appropriate directory under `docs/`
2. Add the page to the navigation in `mkdocs.yml`
3. Write your content using Markdown
4. Test locally with `mkdocs serve`

### Editing Existing Pages

1. Find the `.md` file in the `docs/` directory
2. Make your changes
3. Save and preview in your browser (auto-reloads)
4. Verify everything looks correct

## Markdown Features

The site supports extended Markdown with special features:

### Basic Syntax

```markdown
# Main Heading
## Sub Heading

**Bold** and *italic* text
[Link text](url)

- Bullet lists
1. Numbered lists
```

### Callout Boxes

```markdown
!!! note "Title"
    Important information here

!!! tip "Pro Tip"
    Helpful advice

!!! warning "Watch Out"
    Warning message

!!! danger "Critical"
    Important warning
```

### Grid Cards (Home Page Style)

```markdown
<div class="grid cards" markdown>

-   :material-icon:{ .lg .middle } __Title__

    ---

    Description text

    [:octicons-arrow-right-24: Link](url)

</div>
```

### Tables

```markdown
| Column 1 | Column 2 |
|----------|----------|
| Data     | Data     |
```

## Contributing Workflow

1. **Fork the repository** on GitHub
2. **Create a branch** for your changes: `git checkout -b my-new-content`
3. **Make your edits** in the `docs/` directory
4. **Test locally** with `mkdocs serve`
5. **Commit your changes**: `git commit -am 'Add new guide'`
6. **Push to your fork**: `git push origin my-new-content`
7. **Submit a pull request** on GitHub

Your changes will be reviewed and, once approved, automatically deployed to the live site!

## Troubleshooting

### Module not found

- Run `pip install -r requirements.txt`
- Check that you're in the virtual environment

### Configuration error

- Check `mkdocs.yml` for syntax errors
- Ensure all paths in navigation exist

### Broken links

- Use relative paths: `../page.md` not `/page.md`
- Verify linked files exist

### Development Server Issues

#### Port already in use

- Stop any other instances of `mkdocs serve`
- Or use a different port: `mkdocs serve -a localhost:8001`

#### Changes not showing

- Hard refresh your browser (Ctrl+Shift+R or Cmd+Shift+R)
- Check for syntax errors in your Markdown

## Resources

- 📖 [MkDocs Documentation](https://www.mkdocs.org/)
- 🎨 [Material Theme Docs](https://squidfunk.github.io/mkdocs-material/)
- 💬 [Join our Discord](https://discord.gg/uonewdawn)
- 🐛 [Report Issues](https://github.com/UONewDawn/Codex/issues)

## Technology Stack

- **[MkDocs](https://www.mkdocs.org/)** - Static site generator
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** - Theme
- **[Python Markdown Extensions](https://facelessuser.github.io/pymdown-extensions/)** - Enhanced Markdown features

## ⚖️ License & Legal

This documentation is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** License. 

- **Attribution:** You must give appropriate credit if you use this content.
- **ShareAlike:** If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

**Disclaimer:** *Ultima Online™ is a trademark of Electronic Arts Inc. This project is a fan-made resource and is not affiliated with Electronic Arts or Broadsword.*

---

Built for the New Dawn community
