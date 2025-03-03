#!/usr/bin/env python3

import os
import sys
import glob
import csv

def get_title_description(testcase: str):
    with open ('descriptions.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == testcase:
                return row[1], row[2]

def main(spec: str):
    with open ('metadata.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'title', 'description', 'specification',
                         'mapping', 'input_format1', 'input_format2',
                         'input_format3', 'output_format1', 'output_format2',
                         'output_format3', 'input1', 'input2', 'input3',
                         'output1', 'output2', 'output3', 'error'])
        for testcase in glob.glob('RML*'):
            print(testcase)
            title, description = get_title_description(testcase)
            error = 'false'
            input1 = ''
            input2 = ''
            input3 = ''
            input_format1 = ''
            input_format2 = ''
            input_format3 = ''
            output1 = ''
            output2 = ''
            output3 = ''
            output_format1 = ''
            output_format2 = ''
            output_format3 = ''

            # Input file
            if os.path.exists(os.path.join(testcase, 'student.csv')):
                input1 = 'student.csv'
                input_format1 = 'text/csv'

            # Mapping file
            if os.path.exists(os.path.join(testcase, 'mapping.ttl')):
               mapping_file = 'mapping.ttl'
            else:
                raise ValueError('Mapping file missing!')

            # Output files
            if os.path.exists(os.path.join(testcase, 'default.nq')):
                output1 = 'default.nq'
                output_format1 = 'application/n-quads'
            elif os.path.exists(os.path.join(testcase, 'output.nq')):
                output1 = 'output.nq'
                output_format1 = 'application/n-quads'
            else:
                error = 'true'

            writer.writerow([testcase, title, description, spec, mapping_file,
                             input_format1, input_format2, input_format3,
                             output_format1, output_format2, output_format3,
                             input1, input2, input3, output1, output2,
                             output3, error])
            lines = []
            # Title and description
            lines.append(f'## {testcase}\n\n')
            lines.append(f'**Title**: {title}\n\n')
            lines.append(f'**Description**: {description}\n\n')
            if error == 'true':
                error_html = 'Yes'
            else:
                error_html = 'No'
            lines.append(f'**Error expected?** {error_html}\n\n')

            # Input
            inputCount = ''

            for index, i in enumerate([input1, input2, input3]):
                if not i:
                    break

                if 'http://w3id.org/rml/resources' in i:
                    input_html = f'**Input{inputCount}**\n [{i}]({i})\n\n'
                else:
                    try:
                        with open(os.path.join(testcase, i)) as f:
                            input_html = f'**Input{inputCount}**\n```\n{f.read()}\n```\n\n'
                    except UnicodeDecodeError:
                        try:
                            with open(os.path.join(testcase, i), encoding='utf-16') as f:
                                input_html = f'**Input{inputCount}**\n```\n{f.read()}\n```\n\n'
                        except UnicodeDecodeError:
                            input_html = f'**Input{inputCount}**\n `{i}`\n\n'

                lines.append(input_html)
                inputCount = f' {index + 1}'

            # Mapping
            with open(os.path.join(testcase, mapping_file)) as f:
                mapping_html = f'**Mapping**\n```\n{f.read()}\n```\n\n'
                lines.append(mapping_html)

            # Output
            outputCount = ''
            if output2 or output3:
                outputCount = ' 1'

            for index, i in enumerate([output1, output2, output3]):
                if not i:
                    break

                if 'http://w3id.org/rml/resources' in i:
                    output_html = f'**Output{outputCount}**\n [{i}]({i})\n\n'
                else:
                    try:
                        with open(os.path.join(testcase, i)) as f:
                            output_html = f'**Output{outputCount}**\n```\n{f.read()}\n```\n\n'
                    except UnicodeDecodeError:
                        try:
                            with open(os.path.join(testcase, i), encoding='utf-16') as f:
                                output_html = f'**Output{outputCount}**\n```\n{f.read()}\n```\n\n'
                        except UnicodeDecodeError:
                            output_html = f'**Output{outputCount}**\n `{i}`\n\n'

                lines.append(output_html)
                outputCount = f' {index + 2}'


            with open(os.path.join(testcase, 'README.md'), 'w') as f:
                f.writelines(lines)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./make-metadata.py <IRI OF SPEC>')
        sys.exit(1)
    main(sys.argv[1])
