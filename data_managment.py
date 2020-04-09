import csv
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter


def data_reader(csv_file):
    f = open('Data/' + csv_file + '.csv', 'r')

    with f:
        reader = csv.reader(f, delimiter=",")
        headers = next(reader)
        array = []
        for row in reader:
            array.append(row[0])
        return array


def resize_img(image, maxwidth):
    wpercent = (maxwidth/float(image.size[0]))
    hsize = int((float(image.size[1]))*float(wpercent))
    if hsize > 740:
        hsize = 740
    image = image.resize((maxwidth, hsize), Image.ANTIALIAS)
    return image


def img_loader(dir):
    data = []
    for x in data_reader(dir):
        img = Image.open('Img/' + dir + '/' + x + '.png')
        data.append(ImageTk.PhotoImage(resize_img(img, 250)))
    return data


def generate_pdf(combo_stat, combo_race):
    if combo_stat == '' or combo_race == '':
        return messagebox.showinfo('Error', 'Campos vacios')

    save_as = filedialog.asksaveasfile(mode='w', defaultextension='.pdf')

    if save_as:
        pdf = canvas.Canvas(save_as.name)
        pdf.setTitle('Stat-Race')
        pdf.drawString(250, 850, combo_stat + ' ' + combo_race)
        pdf.setPageSize((660, 900))

        img_stat = Image.open('Img/Statblock/' + combo_stat + '.png')
        img_rez_stat = resize_img(img_stat, 260)
        pil_img_stat = ImageReader(img_rez_stat)
        if img_rez_stat.size[1] < 740:
            pdf.drawImage(pil_img_stat, 50, 840 - img_rez_stat.size[1])
        else:
            pdf.drawImage(pil_img_stat, 50, 100)

        img_race = Image.open('Img/Race/' + combo_race + '.png')
        img_rez_race = resize_img(img_race, 260)
        pil_img = ImageReader(img_rez_race)
        if img_rez_race.size[1] < 740:
            pdf.drawImage(pil_img, 330, 840 - img_rez_race.size[1])
        else:
            pdf.drawImage(pil_img, 330, 100)

        pdf.save()
        messagebox.showinfo('Exito', 'Archivo creado exitosamente')
        return
