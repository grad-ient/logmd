from pathlib import Path
import markdown

class LogSite:
    def __init__(self, log_path='log.md', output_dir='_site'):
        self.log_path = Path(log_path)
        self.output_dir = Path(output_dir)
        self.md = markdown.Markdown(extensions=['fenced_code', 'tables'])
        
    def generate(self):
        """Convert log.md to a simple HTML site"""
        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Read log.md
        content = self.log_path.read_text()
        
        # Convert to HTML
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>logmd</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            max-width: 650px;
            margin: 2rem auto;
            padding: 0 1rem;
            color: #2c3e50;
            background: #fafafa;
        }}
        pre, code {{
            background: #f0f0f0;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-size: 85%;
        }}
        pre code {{
            padding: 1em;
            display: block;
            overflow-x: auto;
        }}
        .task-list {{
            list-style-type: none;
            padding-left: 0;
        }}
        .task-list-item {{
            margin: 0.5em 0;
            display: flex;
            align-items: center;
        }}
        .task-list-item input {{
            margin-right: 0.5em;
        }}
        h1 {{ 
            font-size: 1.5em;
            margin-top: 2em;
            color: #34495e;
        }}
    </style>
</head>
<body>
    {self.md.convert(content)}
    <script>
        document.querySelectorAll('li').forEach(function(li) {{
            var text = li.textContent;
            if (text.startsWith('[ ]') || text.startsWith('[x]')) {{
                var checked = text.startsWith('[x]');
                var checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.checked = checked;
                checkbox.disabled = true;
                li.innerHTML = li.innerHTML.replace(/\\[[ x]\\]/, '');
                li.insertBefore(checkbox, li.firstChild);
                li.classList.add('task-list-item');
                if (li.parentElement) li.parentElement.classList.add('task-list');
            }}
        }});
    </script>
</body>
</html>
"""
        
        # Write output
        output_file = self.output_dir / 'index.html'
        output_file.write_text(html)
        print(f"Generated {output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", default="log.md", help="Path to log.md")
    args = parser.parse_args()
    
    # Generate site
    site = LogSite(args.log)
    site.generate()
