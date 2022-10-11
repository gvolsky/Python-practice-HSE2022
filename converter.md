+ [Converter for insert into .md](#converter-for-insert-into-.md)

## Converter for insert into .md

Обертка кода для вставки в .md файл

```python
import sys
def converter(path, name):
    with open(path, encoding="utf-8") as f:
        with open(name, 'w+') as out:
            header, code = f.read().split('# ---end----')
            for line in header.split('\n'):
                if line.startswith('# title'):
                    line = line[8::]
                    out.write('+ [{}](#{})\n\n'.format(line, 
                                               '-'.join(line.lower().split())))
                    out.write('## ' + line + '\n\n')
                if line.startswith('# description'):
                    line = line[14::]
                    out.write(line + '\n\n')
            out.write('```python\n' + code.strip() + '\n```')
    
if __name__ == "__main__":
    path, name = sys.argv[1::]
    converter(path, name)
```
