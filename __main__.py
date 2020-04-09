from tkinter import Tk, Canvas, StringVar, Button, Scrollbar, W
from tkinter.ttk import Label, Combobox

import data_managment


def selected_item(combobox, image, data):
    image['image'] = data[combobox.current()]


def __init__(self):
    # Frames para colocar las imagenes
    # Frame Statblock
    self.frame_statblock = Canvas(root)
    self.frame_statblock.place(relwidth=1,
                               relheight=1)
    self.frame_statblock.grid(row=1,
                              column=0)
    # Frame Race
    self.frame_race = Canvas(root)
    self.frame_race.place(relwidth=1,
                          relheight=1)
    self.frame_race.grid(row=1,
                         column=1)
    # ---------------------------------------------------

    # Arrays que contienen las imagenes para desplegar, deben ser cargadas antes
    # de poder ser mostradas.
    # Encontrar alguna forma de cargarlas directamente del directorio
    # seria mejor y mas eficiente  (ᵕ̣̣̣̣̣ ہ ᵕ̣̣̣̣̣̣ ✿)

    data_stat = data_managment.img_loader('Statblock')
    data_race = data_managment.img_loader('Race')

    # ----------------------------------------------------

    # Creacion de combobox
    self.selected_statblock = StringVar()
    self.selected_race = StringVar()

    self.combobox_statblock = Combobox(root,
                                       textvariable=self.selected_statblock,
                                       values=data_managment.data_reader('Statblock'),
                                       width=35,
                                       state='readonly')
    self.combobox_statblock.grid(row=0, column=0)

    self.combobox_race = Combobox(root,
                                  textvariable=self.selected_race,
                                  values=data_managment.data_reader('Race'),
                                  width=35,
                                  state='readonly')
    self.combobox_race.grid(row=0,
                            column=1)
    # -----------------------------------------------------

    # Imagenes
    self.panel_statblock = Label(self.frame_statblock)
    self.panel_statblock.grid(row=1,
                              column=0)
    self.panel_race = Label(self.frame_race)
    self.panel_race.grid(row=1,
                         column=1)
    # -----------------------------------------------------

    # Asignar eventos a los combobox
    self.combobox_statblock.bind("<<ComboboxSelected>>",
                                 lambda e:
                                 selected_item(self.combobox_statblock,
                                               self.panel_statblock,
                                               data_stat)
                                 )
    self.combobox_race.bind("<<ComboboxSelected>>",
                            lambda e:
                            selected_item(self.combobox_race,
                                          self.panel_race,
                                          data_race)
                            )

    # Botones
    self.btn_pdf = Button(root,
                          text='Generar Pdf',
                          height=1)
    self.btn_pdf.bind("<Button-1>",
                      lambda e:
                      data_managment.generate_pdf(self.combobox_statblock.get(),
                                                  self.combobox_race.get())
                      )
    self.btn_pdf.grid(row=0,column=2)


if __name__ == '__main__':
    root = Tk()
    root.title('Stat - Race')
    root.geometry('800x600')
    font = ('Arial', 12)
    root.option_add("*Font", font)
    __init__(root)
    root.mainloop()
