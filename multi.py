#Goals:
import sys
import json
Langs = {
    'python': '',
    'c': '',
    'c++': '',
    'c#': '',
    'ruby': '',
    'java': '',
    'swift': '',
    'nim': '',
}
commands = '''
Multi commands:
\tinstall :: Install a multi lang
\tuninstall :: Uninstall a multi lang
\tlist :: list multi langs in a specified category
\tversion :: list all data about your version of multi
\tupdate :: update multi if needed
** Multi for replit!
'''
versiondata = '''
Version Data:
\tVersion: 0.1.0
\tFor: replit
\tUses: nixOS
\tHubVersion: 
'''
with open('multi.multi.json','r') as m:
    stats = json.load(m)
    langs = stats['langs']
args = sys.argv
if len(args) == 1:
    print(commands)
    sys.exit()
if args[1] == 'list':
    note = '''
    Please provide one of the below:
    *   --installed, -I :: List all installed langs.
    *   --ninstalled, -N :: List all not installed langs.
    *   --all, -A :: List all langs
    '''
    if len(args) == 2:
        print(note)
        sys.exit()
        
    if args[2] == '--installed' or args[2] == '-I':
        output = 'Multi Installed Langs:'
        for k in langs.keys():
            if langs[k]:
                output = output + f'\n**    {k}'
        print(output)
    elif args[2] == '--ninstalled' or args[2] == '-N':
        output = 'Multi Not Installed Langs:'
        for k in langs.keys():
            if langs[k] == False:
                output = output + f'\n**    {k}'
        print(output) 
    elif args[2] == '--all' or args[2] == '-A':
        output = 'Multi Langs:\n\tInstalled:'
        for k in langs.keys():
            if langs[k]:
                output = output + f'\n\t**    {k}'
        output = output + '\n\tNot Installed:'
        for k in langs.keys():
            if not langs[k]:
                output = output + f'\n\t**    {k}'
        print(output)
    else:

        print(note)
        sys.exit()
elif args[1] == 'version':
    print(versiondata)
    sys.exit()
elif args[1] == 'update':
    pass

