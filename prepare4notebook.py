#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(
        description='This script converts as Myst markdown file to a markdown file.')
    parser.add_argument('filename', type=str)

    # no arguments given
    if len(sys.argv)==1:
        print('Provide a filename: prepare4notebook.py inputfile.md')
        sys.exit(1)

    return parser.parse_args()


def clean_myst_file(input_filename, output_filename):
    output_lines = []
    with open(input_filename) as file:
        inside_admonition = False
        inside_minisolution = False
        for line in file:

            if line.startswith('````'):
                if inside_minisolution:
                    inside_minisolution = False
                    continue
                else:
                    inside_minisolution = True

            if inside_minisolution:
                continue

            if '```{admonition}' in line:
                inside_admonition = True
            elif ':class: goals' in line and inside_admonition:
                pass
            elif ':class: miniexercise' in line and inside_admonition:
                output_lines.append('**Mini-Übung**\n')
            elif ':class: minisolution' in line and inside_admonition:
                inside_minisolution = True
            elif '```' in line and inside_admonition:
                inside_admonition = False
            else:
                output_lines.append(line)

    with open(output_filename, 'w') as output_file:
        for line in output_lines:
            output_file.write(line)
    return

def main():

    args = parse_command_line_arguments()
    input_filename = args.filename

    output_filename = input_filename.replace('.md', '_cleaned.md')
    clean_myst_file(input_filename, output_filename)


if __name__ == "__main__":
    main()