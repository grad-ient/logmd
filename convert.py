from pathlib import Path
import markdown

class LogSite:
    def __init__(self, log_path='log.md', output_dir='_site'):
        self.log_path = Path(log_path)
        self.output_dir = Path(output_dir)
        self.md = markdown.Markdown(extensions=['fenced_code', 'tables', 'task_lists'])


    def generate(self):
        """convert log.md to a simple HTML site"""
        self.output_dir.mkdir(parents=True, exist_ok=True)

        content = self.log_path.read_text()

        html = f"""

        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>logmd</titleu>

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
                    input[type="checkbox"] {{
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
            </body>
        </html>
        """


        outfile = self.output_dir / 'index.html'
        outfile.write_text(html)
        print(f'Generated {outfile}')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", default='log.md', help="Path to log.md")
    args = parser.parse_args()

    site = LogSite(log_path=args.log)
    site.generate()

