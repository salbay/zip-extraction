import PySimpleGUI as sg
import zip_extractor

sg.theme("Black")
label1 = sg.Text("Select archive:")
label2 = sg.Text("Select dest dir:")
inp_box1 = sg.InputText(tooltip="Enter todo",key="extract",size=30)
inp_box2 = sg.InputText(tooltip="Enter todo",key="destination",size=30)
button_chose1 = sg.FilesBrowse("Choose")
button_chose2 = sg.FolderBrowse("Choose")
button_exit = sg.Button("Exit",key="exit")
button_extract = sg.Button("Extract",key="button_extract")
output_label = sg.Text(key="outputLabel",text_color="green")
layout= [[label1,inp_box1,button_chose1],[label2,inp_box2,button_chose2],[button_extract,button_exit,output_label]]
window = sg.Window("My To-Do App",
                   layout=layout,
                   font=("Helvetica",20))


while True:
    event,values = window.read()
    match event:
        case sg.WINDOW_CLOSED:
            break
        case "button_extract":
            try:
                zip_extractor.extraction(values["extract"],values["destination"])
                window["outputLabel"].update("Extraction is completed.")
            except FileNotFoundError:
                sg.popup("You should select folder!",text_color="red",title="Warning!",font=("Helvetica",25))
        case "exit":
            window.Close()