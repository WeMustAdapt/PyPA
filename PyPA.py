import wolframalpha
client = wolframalpha.Client("YOUR APP ID")

import wikipedia

import PySimpleGUI as sg

sg.theme('LightGreen1')	# Add a touch of color
# All the stuff inside your window.
layout = [ [sg.Text('Enter a command'), sg.InputText()],
[sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('PyPA', layout)

import pyttsx3
engine = pyttsx3.init()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences = 2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking('Wolfram Results:' + wolfram_res, 'Wikipedia Results:' + wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences = 2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print(values[0])

window.close()
