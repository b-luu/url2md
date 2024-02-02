#! /usr/bin/env python3
"""
Small utility script to
convert the HTML available
at the given URL
to Markdown format.

Usage: convert_to_markdown.py URL > result.md
"""

import click
import requests

def html_to_markdown(html_text):
    import html2text  # dynamic (runtime) import to try to remain compatible with GPL-3.0 licensing policies...
    converter = html2text.HTML2Text()
    converter.body_width = 0  # Disable line wrapping
    markdown_text = converter.handle(html_text)
    return markdown_text

def get_html_from_url(url):
    response = requests.get(url)
    html = response.text
    return html

@click.command()
@click.argument('url')
def convert_to_markdown(url):
    html = get_html_from_url(url)
    markdown = html_to_markdown(html)
    print(markdown)

if __name__ == '__main__':
    convert_to_markdown()
