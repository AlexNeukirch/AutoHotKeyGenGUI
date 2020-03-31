#!/usr/bin/env Python3
import PySimpleGUI as sg
import pyperclip


sg.ChangeLookAndFeel('Dark')

# ------ Menu Definition ------ #
menu_def = [['File', ['Exit']],
            ['Help', 'About...'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('AutoHotKeygen', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Nazwa Hotkey')],
    [sg.InputText('', key='jeden')],
    [sg.Text('Temat ticketa')],
    [sg.InputText('', key='dwa')],
    # [sg.Text('Customer\'s Product* - do not use')],
    # [sg.InputCombo(('none', 'Hosting Web', 'Domain', 'Domain Zone', 'Email MXplan', 'Email PRO', 'Email Exchange', 'Inne...'), size=(20, 1), key='trzy'),
    #  sg.InputText('Tylko w przypadku: "Inne..."', key='cztery')],
    [sg.Frame(layout=[
    [sg.Radio('information', "RADIO1", default=True, key='piec', size=(10,1)),
     sg.Radio('change', "RADIO1", key='szesc'),
     sg.Radio('incident', "RADIO1", key='siedem')]], title='Classification*',title_color='red', relief=sg.RELIEF_SUNKEN)],
    [sg.Text('Typologia')],
    [sg.InputCombo(('forwarded to KeepBiz', 'MultiSite', 'DNS configuration', 'Lack of info', 'Manager nic update', 'Telesales: Info - product', 'Inne...'), size=(20, 1), key='osiem'),
     sg.InputText('Tylko w przypadku: "Inne..."', key='dziewiec')],
    [sg.Text('Treść')],
    [sg.Multiline(default_text='', size=(80, 5), key='dziesiec')],
    [sg.Text('_'  * 80)],
    [sg.Button('kopiuj do schowka', tooltip='Kopiuj do schowka'),
     sg.Button('Exit'),
     sg.Button('Reset')]
]

layoutAbout = [[sg.Text('AutoHotKeyGen v.0.6')],
                 [sg.Text('Program utworzony w celu ułatwienia pracy.')],
                 [sg.Button('Powrót')]
]


window = sg.Window('AutoHotKey', layout, default_element_size=(40, 1), grab_anywhere=False)
#event, values = window.read()

while True:
    event, values = window.read()

    #cProduct = values['trzy']
    typologia = values['osiem']

    if event == None or event == "Exit":
        break

    if event == "kopiuj do schowka":
        if values['piec'] == True and values['szesc'] == False and values['siedem'] == False:
            classification = "{tab}{tab}{tab}"
            classification2 = "5"

        elif values['piec'] == False and values['szesc'] == True and values['siedem'] == False:
            classification = "{tab}{tab}"
            classification2 = "6"

        elif values['piec'] == False and values['szesc'] == False and values['siedem'] == True:
            classification = "{tab}"
            classification2 = "7"

        # if values['trzy'] == 'Inne...':
        #     cProduct = values['cztery']

        if values['osiem'] == 'Inne...':
            typologia = values['dziewiec']

        if values['osiem'] == 'Telesales: Info - product':
            typologia = 'Product info sales telesales web'

        if values['osiem'] == 'forwarded to KeepBiz':
            typologia = 'transfer svi keepbiz'


        pyperclip.copy("::" + str(values['jeden']) + """1::\n
Send, """ + str(values['dwa']) + """
Send, ^a^c^v
Loop, 11 {
Send, {tab}
}
Send, {enter}""" + classification + """Pol{tab}{tab}low{tab}low
Loop, 18 {
Send, {tab}
}
Send, """ + str(typologia) + """
Loop, 3 {
Send, {tab}
}
Send, ^v{enter}""" + values['dziesiec'].replace("\n", "{enter}\n") + """
return\n
::""" + str(values['jeden']) + """2::\n
Send, """ + str(values['dwa']) + """
Send, ^a^c^v
Loop, 9 {
Send, {tab}
}
Send, {enter}""" + classification + """Pol{tab}{tab}low{tab}low
Loop, 18 {
Send, {tab}
}
Send, """ + str(typologia) + """
Loop, 3 {
Send, {tab}
}
Send, ^v{enter}""" + values['dziesiec'].replace("\n", "{enter}") + """
\nreturn""")

        sg.popup('Informacja',
                    'skrypt został zapisany w schowku')
        event = None

    if event == 'About...':
        windowAbout = sg.Window('About...', layoutAbout, grab_anywhere=True)
        event, values = windowAbout.read()
        if event == 'Powrót':
            windowAbout.close()

    if event == "Reset":
        window['jeden']('')
        window['dwa']('')
        #window['trzy']('none')
        #window['cztery']('Tylko w przypadku: "Inne..."')
        window['piec'](True)
        window['osiem']('Lack of info')
        window['dziewiec']('Tylko w przypadku: "Inne..."')
        window['dziesiec']('')

window.close()
#del window
